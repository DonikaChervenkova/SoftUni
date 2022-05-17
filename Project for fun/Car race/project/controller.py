from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race

all_valid_car_types = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in all_valid_car_types:

            searched_model = [car for car in self.cars if car.model == model]
            if searched_model:
                raise Exception(f"Car {model} is already created!")

            car = all_valid_car_types[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        searched_driver = [driver for driver in self.drivers if driver.name == driver_name]
        if searched_driver:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        searched_race = [r for r in self.races if r.name == race_name]
        if searched_race:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        try:
            driver = [d for d in self.drivers if d.name == driver_name][0]
        except IndexError:
            raise Exception(f"Driver {driver_name} could not be found!")

        try:
            car = [c for c in self.cars if c.__class__.__name__ == car_type and c.is_taken is False][-1]
        except IndexError:
            raise Exception(f"Car {car_type} could not be found!")

        # if driver own a car --> change it
        if driver.car:
            old_model = driver.car.model
            driver.car.free_the_car()
            driver.car = car
            car.take_the_car()
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        # if driver doesn`t own a car
        driver.car = car
        car.take_the_car()
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        try:
            race = [r for r in self.races if r.name == race_name][0]
        except IndexError:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = [d for d in self.drivers if d.name == driver_name][0]
        except IndexError:
            raise Exception(f"Driver {driver_name} could not be found!")

        # If the driver doesn't own a car
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        # If the driver has already participated in the race
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        # If they both exist and the driver owns a car and driver is NOT in the race
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        try:
            race = [r for r in self.races if r.name == race_name][0]
        except IndexError:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        # start race
        winners = race.get_top_3_fastest_drivers()
        return f"Driver {winners[0].name} wins the {race_name} race with a speed of {winners[0].car.speed_limit}.\n" +\
            f"Driver {winners[1].name} wins the {race_name} race with a speed of {winners[1].car.speed_limit}.\n" +\
            f"Driver {winners[2].name} wins the {race_name} race with a speed of {winners[2].car.speed_limit}."


