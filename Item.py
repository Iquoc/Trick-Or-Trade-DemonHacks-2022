

class Item:

    def __init__(self, candy: str, username: str):
        self.candy = candy
        self.user = username

    def get_candy(self):
        return self.candy

    def get_user(self):
        return self.user


def create_item(candy: str, username: str) -> Item:
    return Item(candy, username)
