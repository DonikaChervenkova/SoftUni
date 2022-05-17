from project.decoration.base_decoration import BaseDecoration
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):

        def current_decor_type(decoration_obj):
            return decoration_obj.__class__.__name__

        all_decors_with_searched_type = [d for d in self.decorations if decoration_type == current_decor_type(d)]

        return all_decors_with_searched_type[0] if all_decors_with_searched_type else "None"
