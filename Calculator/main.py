# -*- coding: cp1251 -*-
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# Импорт модуля Config;
# Настройка дефолтных настроек программы.
from kivy.config import Config
Config.set('graphics', 'height', '520')
Config.set('graphics', 'width', '340')
Config.set('graphics', 'resizable', '0')

class CalculatorApp(App):
	def on_start(self):
		pass

	def build(self):
		bl = BoxLayout()
		gl = GridLayout()

		bl.add_widget(gl)

		return bl

if __name__ == '__main__':
	CalculatorApp().run()
