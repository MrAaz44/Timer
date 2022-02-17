from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.clock import *
from kivy.uix.label import Label
from kivy.properties import *
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
class pop(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.7,.7)
        b = BoxLayout()
        self.add_widget(b)
        self.a = Label(text=str(app.süre))
        b.add_widget(self.a)
        bt = Button(text="restart")
        b.add_widget(bt)
        bt.bind(on_release=self.aa)
    def aa(self,ğ):
        self.dismiss()
        app.süre = 0
class main(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.saat = Label(text=str(app.süre),font_size=100,size_hint_y=.9)
        self.add_widget(self.saat)
        a = BoxLayout(size_hint_y=.1)
        self.add_widget(a)
        self.dvm = Switch(size_hint_x=.7)
        a.add_widget(self.dvm)
        self.btn = Button(text="Done",size_hint_x=.3)
        a.add_widget(self.btn)
        self.btn.bind(on_release=self.sa)
        Clock.schedule_interval(self.kont, 1)
    def kont(self,b):
        if self.dvm.active == False:
            app.süre += 1
            self.saat.text = str(app.süre)
        else:
            pass
    def sa(self,b):
        self.dvm.active = True
        pop().open()
class app(App):
    süre = NumericProperty(0)
    def build(self):
        return main()
if __name__ == "__main__":
    app = app()
    app.run()