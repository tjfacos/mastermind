import os

from modules.network.account import User
from modules.network.encrypt import encrypt

from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("./modules/ui/login.kv")

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user):
        self._user = user
    
    def logger(self):
        # print(self.root.ids.username.text, self.root.ids.password.text)
        if " " in self.root.ids.username.text+self.root.ids.password.text:
            self.root.ids.message_label.text = "No spaces allowed in entries"
            self.clear()
        else:
            self.user = User(
                self.root.ids.username.text,
                encrypt(self.root.ids.password.text)
            )
            
            self.user.verify()
            if self.user.signed_in:
                # print(f"Username: {self.user.username}")
                # print(f"Password: {self.user.password}")
                self.finalise()
            else:
                self.root.ids.message_label.text = "Sorry! Incorrect Username or Password"
                self.clear()

    def clear(self):
        self.root.ids.username.text = ""
        self.root.ids.password.text = ""

    def create_account(self):
        if " " in self.root.ids.username.text+self.root.ids.password.text:
            self.root.ids.message_label.text = "No spaces allowed in entries"
            self.clear()
        else:
            self.user = User(
                self.root.ids.username.text,
                encrypt(self.root.ids.password.text)
            )
            if self.user.create():
                self.finalise()
            else:
                self.root.ids.message_label.text = "Sorry! Username is taken!"
                self.clear()

    def no_login(self):
        self.user = User("", "")
        self.finalise()
    
    def finalise(self):
        #write acccount username and password to file account.txt
        #Then stop
        
        with open("account.txt", "w") as f:
            f.write(f"{self.user.username} {self.user.password}")
        
        self.stop()


def run_sign_in():
    app = MainApp()
    app.user = User("","")
    
    MainApp().run()
    

if __name__ == "__main__":
    run_sign_in()
    with open("account.txt", "r") as f:
        print(f.readline().split())
    

    
