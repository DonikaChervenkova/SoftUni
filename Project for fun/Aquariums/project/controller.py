from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def get_item_type(current_obj):
        return current_obj.__class__.__name__

    def check_for_eq_fish_and_aquarium_type(self, current_fish, current_aquarium):
        if (self.get_item_type(current_fish) == "FreshwaterFish" and self.get_item_type(current_aquarium) == "FreshwaterAquarium") or \
                (self.get_item_type(current_fish) == "SaltwaterFish" and self.get_item_type(current_aquarium) == "SaltwaterAquarium"):
            return True
        return False

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_aquarium_types = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}

        if aquarium_type not in valid_aquarium_types:
            return "Invalid aquarium type."

        new_aquarium = valid_aquarium_types[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        valid_decoration_types = {"Ornament": Ornament, "Plant": Plant}

        if decoration_type not in valid_decoration_types:
            return "Invalid decoration type."

        new_decoration = valid_decoration_types[decoration_type]()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        searched_decoration = [d for d in self.decorations_repository.decorations if decoration_type == self.get_item_type(d)]

        if not searched_decoration:
            return f"There isn't a decoration of type {decoration_type}."

        searched_aquarium = [a for a in self.aquariums if aquarium_name == a.name]

        if searched_aquarium:
            decoration_to_insert = searched_decoration[0]
            aquarium = searched_aquarium[0]
            self.decorations_repository.remove(decoration_to_insert)
            aquarium.add_decoration(decoration_to_insert)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):

        valid_fish_types = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

        if fish_type not in valid_fish_types:
            return f"There isn't a fish of type {fish_type}."

        new_fish = valid_fish_types[fish_type](fish_name, fish_species, price)
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

        if aquarium.capacity <= len(aquarium.fish):
            return "Not enough capacity."

        if not self.check_for_eq_fish_and_aquarium_type(new_fish, aquarium):
            return "Water not suitable."

        aquarium.add_fish(new_fish)
        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        total_value_of_aquarium = sum([f.price for f in aquarium.fish]) + sum([d.price for d in aquarium.decorations])
        return f"The value of Aquarium {aquarium_name} is {total_value_of_aquarium:.2f}."

    def report(self):
        result = []

        for aquarium in self.aquariums:
            result.append(aquarium.__str__())
        return '\n'.join(result)

