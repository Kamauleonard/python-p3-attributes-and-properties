#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    pass
    def __init__(self, name="None", breed=""):
        self._name = name
        self.breed = breed

        if not name:
            print("Name must be string between 1 and 25 characters.")
        elif not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        elif not 1 <= len(name) <= 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name


    def get_name(self):
        return self._name

    def set_name(self, value):
        if not value:
            print("Name must be string between 1 and 25 characters.\n")
        elif not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.\n")
        else:
            self._name = value

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value != "" and value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self._breed = None
        else:
            self._breed = value


    breed = property(get_breed, set_breed)
