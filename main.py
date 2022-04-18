from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
	def build(self):
		al = AnchorLayout(anchor_x = 'left', anchor_y = 'bottom')
		gl = GridLayout(cols = 3, rows = 5, padding = [20], spacing = [5], size_hint = [None, None], size = [180, 180])

		for i in range(9):
			if ((i == 0) or (i == 2) or (i == 6) or (i == 8)):
				gl.add_widget(Button(text = '',
					background_down = '',
					background_color = [0, 0, 0, 0],
					size_hint = [None, None],
					size = [50, 50]))
			else:
				gl.add_widget(Button(text = str(i),
					size_hint = [None, None],
					size = [50, 50]))
		al.add_widget(gl)
# idi nahuy
		return al

if __name__ == '__main__':
	MyApp().run()
