import tkinter as tk
import Data

root = tk.Tk()
root.geometry("800x600")
root.title("Trick or Trade")


nameVar = tk.StringVar()
passwordVar = tk.StringVar()
emailVar = tk.StringVar()
welcomeLabel = tk.Label(root, text = 'Welcome')

#dictionary key = name, value = Object
userbase = Data(r'userbase.json')
userbase.read()
users = userbase.get_userbase()
currentUser = 0
candyTypes = ['Chocolate Bar', 'Lollipop', 'Mint']

#class for user data
class User:
  def __init__(self, name, password, email):
    self.name = name
    self.password = password
    self.email = email
    self.inventory = {}
    self.preferedCandy = [False, False, False]

  def __str__(self):
    return f"{self.name} {self.password} {self.email}"

  def setCandy(self, candy, amount):
    self.inventory[candy] = amount

  def addCandy(self, candy, amount):
    self.inventory[candy] = self.inventory[candy] + amount

  def subtractCandy(self, candy, amount):
    self.inventory[candy] = self.inventory[candy] - amount

  def likedCandy(self,index):
    self.preferedCandy[index] = True

def clearBoxes():
  nameVar.set('')
  passwordVar.set('')
  emailVar.set('')

def createAccount():
  name = nameVar.get()
  password = passwordVar.get().strip()
  email = emailVar.get().strip()
  clearBoxes()
  valid = True
  if len(name) <= 0 or len(password) <= 0 or len(email) <= 0:
    valid = False
  if name in users:
    valid = False
  if(valid):
    print("creating account #{}".format(len(users)))
    users[name] = User(name, password, email)

    recordData(r'userbase.json', users)
    welcomeLabel.config(text = 'Account Created')
  else:
    welcomeLabel.config(text = 'Invalid input')

def signIn():
  name = nameVar.get()
  password = passwordVar.get()
  email = emailVar.get()
  clearBoxes()
  signedIn = False
  global currentUser
  if name not in users:
    welcomeLabel.config(text='Incorrect username')
  else:
    if users[name].password == password:
      currentUser = name
      loadUsersPage()
      signedIn = True
    else:
      welcomeLabel.config(text = 'Incorrect password')

clicked = tk.StringVar()
clicked.set('------')
dropMenuLable = tk.Label( root , text = " " )
def show():
  dropMenuLable.config(text=clicked.get())
def loadUsersPage():
  welcomeText = 'Welcome, ' + users[currentUser].name
  welcomeLabel.config(text=welcomeText)
  candyListMenu = tk.OptionMenu(root, clicked, candyTypes)
  candyListMenu.grid(row = 1, column = 4)




nameText = tk.Label(root, text = 'Username')
nameEntry = tk.Entry(root, textvariable = nameVar)
passwordText = tk.Label(root, text = 'Password')
passwordEntry = tk.Entry(root, textvariable = passwordVar)
emailText = tk.Label(root, text = 'Email')
emailEntry = tk.Entry(root, textvariable = emailVar)
signInButton = tk.Button(root, text = 'Sign In', command = signIn)
createAccButton = tk.Button(root, text = 'Create Account', command = createAccount)

welcomeLabel.grid(row=0, column=1)
nameText.grid(row=1,column=0)
nameEntry.grid(row=1,column=1)
passwordText.grid(row=2,column=0)
passwordEntry.grid(row=2,column=1)
emailText.grid(row=3, column = 0)
emailEntry.grid(row=3, column = 1)
signInButton.grid(row=4, column=1)
createAccButton.grid(row=5, column=1)

root.mainloop()
