from kivy.app import App
from kivy.uix.label import Label

class KivyLabel(App):

    def build(self):

        return Label (text="[u][color=ff0066][b]Bienvenidos[/b][/color] a [i][color=ff9933] asCodigo [/i] Suscribete [/color][/u]", markup=True)


KivyLabel().run()
