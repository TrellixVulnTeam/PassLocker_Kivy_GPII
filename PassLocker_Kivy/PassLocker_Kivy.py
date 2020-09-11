import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
Window.size = (300, 100)

class LoginPage(GridLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)

        self.cols = 2
       
        self.add_widget(Label(text='Master Password : '))
        self.passwd = TextInput(multiline=False)
        self.add_widget(self.passwd)
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=''))
        self.btn_cancel = Button(text='Cancel')
        self.btn_cancel.bind(on_press=self.close_app)
        self.add_widget(self.btn_cancel)
        self.btn_login = Button(text='Login')
        self.btn_login.bind(on_press=self.login)
        self.add_widget(self.btn_login)


    def close_app(self, instance):
        App.get_running_app().stop()
        Window.close()

    def login(self, instance):
        passwd = self.passwd.text

        print("Your password is : " + passwd)

class LoginApp(App):
    def build(self):
        return LoginPage()
        self.title = 'PassLocker - Login'


if __name__ == "__main__":
    LoginApp().run()