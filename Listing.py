import Item


class Listing:

    def __init__(self, candy_have: list[str], candy_want: list[str], username: str, location: str):
        self.inventory = []
        for ch in candy_have:
            self.inventory.append(Item.create_item(ch, username))
        self.want = []
        for cw in candy_want:
            self.want.append(cw)
        self.location = location

    def get_inventory(self):
        return self.inventory

    def get_want(self):
        return self.want

    def get_location(self):
        return self.location

    def add_have(self, item: Item):
        curr = self.inventory
        if item in curr:
            return 'Item is Already in Inventory'
        else:
            curr.append(item)
            return 'Successfully Added to Inventory'

    def add_want(self, item: Item):
        curr = self.want
        if item in curr:
            return 'Item is Already in Wants'
        else:
            curr.append(item)
            return 'Successfully Added to Wants'
