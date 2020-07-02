import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import use_model

Config.set('graphics', 'resizable', True)


# Create the App class
class UserApp(App):

    # defining build()
    def build(self):
        # Telling orientation
        box = BoxLayout(orientation='vertical', )

        self.lbl = Label(text='Geography', font_size='20sp')

        # Adding the text input
        self.txt = TextInput(font_size=30, size_hint_y=None, height=100)

        self.lbl2 = Label(text='Gender', font_size='20sp')

        # Adding the text input
        self.txt2 = TextInput(font_size=30, size_hint_y=None, height=100)

        self.lbl3 = Label(text='Age', font_size='20sp')

        # Adding the text input
        self.txt3 = TextInput(font_size=30, size_hint_y=None, height=100)

        self.lbl4 = Label(text='Expected Salary', font_size='20sp')

        # Adding Button and styling
        btn = Button(text="Submit", font_size="30sp", size_hint=(.5, .5), pos=(300, 250),
                     background_color=(.67, 1, .33, 1), color=(1, 1, 1, 1))

        btn.bind(on_press=self.button_clicked)

        box.add_widget(self.lbl)
        box.add_widget(self.txt)
        box.add_widget(self.lbl2)
        box.add_widget(self.txt2)
        box.add_widget(self.lbl3)
        box.add_widget(self.txt3)
        box.add_widget(self.lbl4)

        box.add_widget(btn)

        return box

    # Run the App

    def button_clicked(self, btn):
        geo = self.txt.text  # get input from textbox
        gen = self.txt2.text
        age = self.txt3.text

        geo = geo.lower()  # lowercase string
        gen = gen.lower()
        age = int(age)  # convert to int

        geo_num = 1  # number assigned to geography france
        gen_num = 1 # number asigned to gender female

        if geo == 'germany':
            geo_num = 2
        elif geo == 'spain':
            geo_num = 3

        if gen == 'male':
            gen_num = 2

        result = use_model.btn_click(self, geo_num, gen_num, age)
        self.lbl4.text = str(result)


if __name__ == "__main__":
    UserApp().run()
