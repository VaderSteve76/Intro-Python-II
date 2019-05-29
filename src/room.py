# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, descritpion):
        self.name = name
        self.description = descritpion
        self.items = []
