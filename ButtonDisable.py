from kivy.uix.button import Button
from kivy.app import App
from functools import partial

class miButton(App):

    def disable(self, instance, *args):

        instance.disable = True

    def update(self, instance, *args):

        instance.text = "Estoy desabilitado"

    def build(self):

        mybtn = Button(text="Haz click para desactivar")

        mybtn.bind (on_press = partial(self.disable, mybtn))

        mybtn.bind (on_press = partial(self.update, mybtn))

        return mybtn


miButton().run()