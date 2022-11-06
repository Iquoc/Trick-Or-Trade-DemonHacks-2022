import tkinter as tk
from Temp import User
import Data


class StartMenu:

    def __init__(self):
        self.users = {}
        self.currentUser = 0
        self.candyTypes = ['Chocolate Bar', 'Lollipop', 'Mint']

        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Trick or Trade")

        self.nameVar = tk.StringVar()
        self.passwordVar = tk.StringVar()
        self.emailVar = tk.StringVar()
        self.welcomeLabel = tk.Label(self.root, text='Welcome')

    def run(self):
        clicked = tk.StringVar()
        clicked.set('------')

        dropMenuLable = tk.Label(self.root, text=" ")
        nameText = tk.Label(self.root, text='Username')
        nameEntry = tk.Entry(self.root, textvariable=self.nameVar)
        passwordText = tk.Label(self.root, text='Password')
        passwordEntry = tk.Entry(self.root, textvariable=self.passwordVar)
        emailText = tk.Label(self.root, text='Email')
        emailEntry = tk.Entry(self.root, textvariable=self.emailVar)
        signInButton = tk.Button(self.root, text='Sign In', command=self.sign_in)
        createAccButton = tk.Button(self.root, text='Create Account', command=self.create_account)

        self.welcomeLabel.grid(row=0, column=1)
        nameText.grid(row=1, column=0)
        nameEntry.grid(row=1, column=1)
        passwordText.grid(row=2, column=0)
        passwordEntry.grid(row=2, column=1)
        emailText.grid(row=3, column=0)
        emailEntry.grid(row=3, column=1)
        signInButton.grid(row=4, column=1)
        createAccButton.grid(row=5, column=1)

        self.root.mainloop()

    def clear_boxes(self):
        self.nameVar.set('')
        self.passwordVar.set('')
        self.emailVar.set('')

    def create_account(self):
        name = self.nameVar.get()
        password = self.passwordVar.get().strip()
        email = self.emailVar.get().strip()
        self.clear_boxes()
        valid = True
        if len(name) <= 0 or len(password) <= 0 or len(email) <= 0:
            valid = False
        if name in self.users:
            valid = False
        if valid is True:
            print("creating account #{}".format(len(self.users)))
            self.users[name] = User(name, password, email)

            # recordData(r'userbase.json', users)
            self.welcomeLabel.config(text='Account Created')
        else:
            self.welcomeLabel.config(text='Invalid input')

    def sign_in(self):
        name = self.nameVar.get()
        password = self.passwordVar.get()
        email = self.emailVar.get()
        self.clear_boxes()
        signedIn = False
        global currentUser
        if name not in self.users:
            self.welcomeLabel.config(text='Incorrect username')
        else:
            if self.users[name].password == password:
                currentUser = name
                # load_users_page()
                signedIn = True
            else:
                self.welcomeLabel.config(text='Incorrect password')


    # def show(self):
    #     dropMenuLable.config(text=clicked.get())

    # def load_users_page():
    #     welcomeText = 'Welcome, ' + users[currentUser].name
    #     welcomeLabel.config(text=welcomeText)
    #     candyListMenu = tk.OptionMenu(root, clicked, candyTypes)
    #     candyListMenu.grid(row=1, column=4)

