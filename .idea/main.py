from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
from subprocess import call



class SmAgro(FloatLayout):
    def __init__(self, **kwargs):
        super(SmAgro, self).__init__(**kwargs)
        self.screen_list = []

    def call_External_Pog(self):
        call(['7w.sh'])

    def changeScreen(self, next_screen):

        if next_screen == "configuracoes":
            self.ids.kivy_screen_manager.current = "configuracoes_screen"

        if next_screen == "equipamentos":
            self.ids.kivy_screen_manager.current = "equipamento_screen"

        if next_screen == "sobre":
            self.ids.kivy_screen_manager.current = "about_screen"

        if next_screen == "voltar":
            self.ids.kivy_screen_manager.current = "start_screen"


class SMAgroApp(App):
    def __init__(self, **kwargs):
        super(SMAgroApp, self).__init__(**kwargs)
    def build(self):
        return SmAgro()


if __name__ == '__main__':
    SMAgroApp().run()
