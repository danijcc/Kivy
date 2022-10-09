from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor=(1,1,0,1)

class Mylbl(Widget):
    def Clicked(self):
        name = self.ids.input_text.text
        self.ids.Labelid.text = name
        self.ids.input_text.text = " "
        NotePd = open("We.text",'a')
        NotePd.write(f"{name}\n")
class MainClass(App):
    pass


MainClass().run()