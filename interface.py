from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder


# App Principal
class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('screens/screenssample.kv')


# Gerenciador de Telas
class ScreensManagement(ScreenManager):
    def change_screen():
        ...


# Telas
class HomeScreen(Screen):
    ...


class GameScreen(Screen):
    ...


# Classe Interface para melhor gerenciamento das Janelas
class Interface:
    def __init__(self):
        self.app = App()
        self.screen_manager = ScreensManagement()

        self.screen_manager.add_widget(HomeScreen(name="home"))
        self.screen_manager.add_widget(GameScreen(name="game"))

        self.app.run()
