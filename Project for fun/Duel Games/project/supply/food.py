from project.supply.supply import Supply


class Food (Supply):
    def __init__(self, name: str, energy=25):
        super().__init__(name, energy)

    def details(self):
        # Hint: override the method in the child classes.
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"