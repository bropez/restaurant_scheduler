import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class AllHolder(BoxLayout):
    pass


class RestaurantApp(App):

    def build(self):
        return AllHolder()


if __name__ == '__main__':
    RestaurantApp().run()
