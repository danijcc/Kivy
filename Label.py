'''Comandos de instalacion: 
python -m pip install --upgrade pip wheel setuptools
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
pip install kivymd = https://pypi.org/project/kivymd/  
'''
from kivy.app import App
from kivy.uix.label import Label


class KivySaludo(App):
    def build(self):
       
       return Label(text = 'Hola Mundo')

if __name__ == "__main__":
   KivySaludo().run()