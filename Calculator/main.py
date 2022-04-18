# -*- coding: cp1251 -*-
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# Импорт модуля Config;
# Настройка дефолтных настроек программы.
from kivy.config import Config
Config.set('graphics', 'height', '520')
Config.set('graphics', 'width', '340')
Config.set('graphics', 'resizable', '0')

class CalculatorApp(App):
	def on_start(self):
		self.point = True
		self.forma = ''
		self.last_forma = ''

	def build(self):
		bl1 = BoxLayout(orientation = 'vertical', padding = 15, spacing = 10)
		bl2 = BoxLayout(orientation = 'horizontal', size_hint = [1, .6], spacing = 5)
		bl3 = BoxLayout(orientation = 'vertical', size_hint = [.25, 1], spacing = 4)
		gl1 = GridLayout(cols = 3, size_hint = [.75, 1], spacing = 4)
		gl2 = GridLayout(cols = 1, size_hint = [1, .6], spacing = 4)
		gl3 = GridLayout(cols = 1, size_hint = [1, .4], spacing = 4)
		self.lbl1 = Label(text = '', font_size = 15, halign = 'right', valign = 'center', size_hint = [1, .1], text_size = [310, 22])
		self.lbl2 = Label(text = '', font_size = 25, halign = 'right', valign = 'top', size_hint = [1, .3], text_size = [310, 126])

		bl1.add_widget(self.lbl1)
		bl1.add_widget(self.lbl2)
		bl1.add_widget(bl2)
		bl2.add_widget(gl1)
		bl2.add_widget(bl3)
		bl3.add_widget(gl2)
		bl3.add_widget(gl3)

		gl1.add_widget(Button(text = '+', on_press = self.add_operation))
		gl1.add_widget(Button(text = '-', on_press = self.add_operation))
		gl1.add_widget(Button(text = '/', on_press = self.add_operation))
		gl2.add_widget(Button(text = '*', on_press = self.add_operation))

		gl1.add_widget(Button(text = '7', on_press = self.add_number))
		gl1.add_widget(Button(text = '8', on_press = self.add_number))
		gl1.add_widget(Button(text = '9', on_press = self.add_number))
		gl2.add_widget(Button(text = 'С', on_press = self.delete_all))

		gl1.add_widget(Button(text = '4', on_press = self.add_number))
		gl1.add_widget(Button(text = '5', on_press = self.add_number))
		gl1.add_widget(Button(text = '6', on_press = self.add_number))
		gl2.add_widget(Button(text = '<<', on_press = self.backspace))

		gl1.add_widget(Button(text = '1', on_press = self.add_number))
		gl1.add_widget(Button(text = '2', on_press = self.add_number))
		gl1.add_widget(Button(text = '3', on_press = self.add_number))
		gl3.add_widget(Button(text = '=', on_press = self.calc))

		gl1.add_widget(Widget())
		gl1.add_widget(Button(text = '0', on_press = self.add_number))
		gl1.add_widget(Button(text = '.', on_press = self.add_number))

		return bl1

	def calc(self, instance):
		self.last_forma = self.forma + '='
		n = eval(self.forma)
		if (int(n) == n):
			n = int(n)
		self.forma = str(n)
		self.lbl2.text = self.forma
		self.lbl1.text = self.last_forma

	def add_number(self, instance):
		if (self.forma != ''):
			if ((self.forma[-1] == '0') and (instance.text != '.')):
				self.forma = self.forma[:-1]
			elif (((self.forma[-1] == '+') or (self.forma[-1] == '-') or (self.forma[-1] == '/') or (self.forma[-1] == '*')) and (instance.text == '.')):
				self.forma += '0'
		else:
			if ((self.forma == '0') and (instance.text != '.')):
				self.forma = ''
			elif ((self.forma == '') and (instance.text == '.')):
				self.forma = '0'

		if ((instance.text == '.') and (not self.point)):
			self.forma += ''
		else:
			if (instance.text == '.'):
				self.point = False
			self.forma += instance.text

		self.lbl2.text = self.forma

	def add_operation(self, instance):
		if ((self.forma[-1] == '+') or (self.forma[-1] == '-') or (self.forma[-1] == '/') or (self.forma[-1] == '*')):
			self.forma = self.forma[:-1]

		self.point = True
		self.forma += instance.text
		self.lbl2.text = self.forma

	def delete_all(self, instance):
		self.forma = ''
		self.last_forma = ''
		self.lbl2.text = self.forma
		self.lbl1.text = self.last_forma

	def backspace(self, instance):
		if (self.forma != ''):
			self.forma = self.forma[:-1]
		self.lbl2.text = self.forma

if __name__ == '__main__':
	CalculatorApp().run()
