from typing import List

from project.driver import Driver


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers: List[Driver] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

    def get_top_3_fastest_drivers(self):
        top_3_speed_limits_of_cars = sorted([d.car.speed_limit for d in self.drivers], reverse=True)[:3]
        top_3_drivers = []
        for speed_limit in top_3_speed_limits_of_cars:
            for driver in self.drivers:
                if driver.car.speed_limit == speed_limit:
                    driver.number_of_wins += 1
                    top_3_drivers.append(driver)
                    break
        return top_3_drivers
