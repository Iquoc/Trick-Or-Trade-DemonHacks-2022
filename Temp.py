import Data


#class for user data
class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
        self.inventory = {}
        self.preferred_candy = [False, False, False]

    def __str__(self):
        return f"{self.name} {self.password} {self.email}"

    def record_data(self, filename: str, data: dict):
        record = Data.create_data_process(filename)  # creates data object
        record.write(data)  # writes the data to be stored in the document

    def read_data(self, filename: str) -> dict:
      data = Data.create_data_process(filename)  # creates a data object using the file to be read
      data.read()  # reads the file
      return data.userbase  # returns the dictionary stored in the file

    def set_candy(self, candy, amount):
        self.inventory[candy] = amount

    def add_candy(self, candy, amount):
        self.inventory[candy] = self.inventory[candy] + amount

    def subtract_candy(self, candy, amount):
        self.inventory[candy] = self.inventory[candy] - amount

    def liked_candy(self,index):
        self.preferred_candy[index] = True
