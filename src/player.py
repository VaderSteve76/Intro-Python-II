# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

    def __str__(self):
        return f'Current room : {self.current_room.name}'

    def item_list(self):
        return " ".join(str(item.name) for item in self.items)
