from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    AMOUNT_TO_INCREASE_SIZE_BY_EATING = 3
    SIZE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.SIZE, price)