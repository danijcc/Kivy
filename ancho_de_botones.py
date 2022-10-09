from kivy.app import App    
from kivy.uix.button import Button

class miButton(App):
    def build(self):
        return Button(text = 'Bienvenidos', pos = (300,350), size_hint = (.25, .18))

miButton().run()
