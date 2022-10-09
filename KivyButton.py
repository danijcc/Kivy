from kivy.uix.button import Button
from kivy.app import App
class miButton(App):

    def build(self):

        return Button(text = 'Entrar', background_color = (155,0,51,53))

miButton().run()