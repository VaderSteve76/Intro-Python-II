class Item:
    def __init__(self, name, t):
        self.name = name
        self.type = t

    def __str__(self):
        return f'Item Name: {self.name}'
