from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout 
from kivymd.uix.menu import MDDropdownMenu

Window.size = (350, 600)



class MainApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Orange"
		self.theme_cls.theme_style = "Dark"
		screen_manager = ScreenManager()
		screen_manager.add_widget(Builder.load_file("main.kv"))
		screen_manager.add_widget(Builder.load_file("login1.kv"))
		screen_manager.add_widget(Builder.load_file("signup.kv"))
		screen_manager.add_widget(Builder.load_file("home.kv"))
		screen_manager.add_widget(Builder.load_file("login.kv"))
		


		return screen_manager



	
MainApp().run()