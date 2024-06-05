from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition
from kivy.core.text import LabelBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem


# Classe que lida com o jogo
class Game(MDApp):
    def build(self):  # Função responsável por buildar a tela
        LabelBase.register(name='Merich',  # Carrega a fonte Merich
                   fn_regular='fonts/merich/Merich.otf')
        self.theme_cls.theme_style = "Dark"  # Seta o tema para dark
        return Builder.load_file('screens/screenssample.kv')


# Gerenciador de Telas
class ScreensManagement(ScreenManager):
    def go_to(self, page):
        self.transition = FadeTransition()
        self.current = page


# Telas
class HomeScreen(Screen):
    ...


## Tela importante, a responsável por quando o jogo está rolando
class GameScreen(Screen):
    ...


## Tela responsável por geranciar as configurações
class ConfigsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.dialog = None

    def show_difficulties_options(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Escolha a Dificuldade",
                type="confirmation",
                items=[
                ]
            )
            self.dialog.open()


# Classe Interface para melhor gerenciamento das Janelas
class Interface:
    def __init__(self):
        self.app = Game()
        self.screen_manager = ScreensManagement()

        self.screen_manager.add_widget(HomeScreen(name="home"))
        self.screen_manager.add_widget(GameScreen(name="game"))

        self.app.run()
