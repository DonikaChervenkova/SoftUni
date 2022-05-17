from abc import ABC, abstractmethod
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @staticmethod
    def get_fish_type(current_fish):
        return current_fish.__class__.__name__

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):

        if self.capacity <= len(self.fish):
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {self.get_fish_type(fish)} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = 'none'
        if self.fish:
            fish_names = ' '.join([f.name for f in self.fish])

        return f"{self.name}:\n" + f"Fish: {fish_names}\n" + f"Decorations: {len(self.decorations)}\n" + f"Comfort: {self.calculate_comfort()}"
    

