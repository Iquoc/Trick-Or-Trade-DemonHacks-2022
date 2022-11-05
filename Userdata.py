
#use tree if big data set
users = []
currentUser = None
class User:
  def __init__(self, name, password, email):
    self.name = name
    self.password = password
    self.email = email
    self.inventory = {}

  def __str__(self):
    return f"{self.name} {self.password} {self.email}"
    #print("{} {} {}".format(self.name, self.password, self.email))

  def setCandy(self, candy, amount):
    self.inventory[candy] = amount

  def addCandy(self, candy, amount):
    self.inventory[candy] = self.inventory[candy] + amount

  def subtractCandy(self, candy, amount):
    self.inventory[candy] = self.inventory[candy] - amount

def createAccount():
  name = input("name: ")
  password = input("password: ")
  email = input("email: ")
  users.append(User(name, password,email))

def signIn():
  signedIn = False
  while(signedIn == False):
    name = input("username: ")
    for i in range(len(users)):
      if users[i].name == name:
        while(signedIn == False):
          password = input("password: ")
          if(users[i].password == password):
            signedIn = True
          if(password.lower() == "exit"):
            break
          else:
            print("Incorrect password")
        break
    if(signedIn == False):
      print("User Not Found")


createAccount()
signIn()
print(len(users))
for _ in range(len(users)):
  print(users[_])