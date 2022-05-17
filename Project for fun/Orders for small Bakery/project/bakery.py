from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.food_names = set()
        self.drinks_names = set()
        self.table_numbers = set()
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):

        if name in self.food_names:
            raise Exception(f"{food_type} {name} is already in the menu!")

        all_food_types = {"Bread": Bread, "Cake": Cake}

        new_food = all_food_types[food_type](name, price)
        self.food_menu.append(new_food)
        self.food_names.add(name)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):

        if name in self.drinks_names:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        all_drinks_types = {"Tea": Tea, "Water": Water}

        new_drink = all_drinks_types[drink_type](name, portion, brand)
        self.drinks_menu.append(new_drink)
        self.drinks_names.add(name)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):

        if table_number in self.table_numbers:
            raise Exception(f"Table {table_number} is already in the bakery!")

        all_tabel_types = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

        new_table = all_tabel_types[table_type](table_number, capacity)
        self.tables_repository.append(new_table)
        self.table_numbers.add(table_number)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):

        if table_number not in self.table_numbers:
            return f"Could not find table {table_number}"

        table = [table for table in self.tables_repository if table.table_number == table_number][0]

        food_names_not_in_the_menu = []

        result = []
        result.append(f"Table {table_number} ordered:")

        for food_name in food_names:
            if food_name in self.food_names:
                searched_food_as_obj = [f for f in self.food_menu if f.name == food_name][0]
                table.order_food(searched_food_as_obj)
                result.append(f"{repr(searched_food_as_obj)}")
            else:
                food_names_not_in_the_menu.append(food_name)

        result.append(f"{self.name} does not have in the menu:")
        for item in food_names_not_in_the_menu:
            result.append(item)

        return '\n'.join(result)

    def order_drink(self, table_number: int, *drinks_names):

        if table_number not in self.table_numbers:
            return f"Could not find table {table_number}"

        table = [table for table in self.tables_repository if table.table_number == table_number][0]

        result = []
        drinks_names_not_in_the_menu = []

        result.append(f"Table {table_number} ordered:")

        for name in drinks_names:
            if name in self.drinks_names:
                searched_drink_as_obj = [d for d in self.drinks_menu if d.name == name][0]
                table.order_drink(searched_drink_as_obj)
                result.append(f"{repr(searched_drink_as_obj)}")
            else:
                drinks_names_not_in_the_menu.append(name)

        result.append(f"{self.name} does not have in the menu:")
        for item in drinks_names_not_in_the_menu:
            result.append(item)

        return '\n'.join(result)

    def leave_table(self, table_number: int):
        searched_table = [table for table in self.tables_repository if table.table_number == table_number][0]

        table_bill = searched_table.get_bill()
        self.total_income += table_bill
        searched_table.clear()

        return f"Table: {table_number}\n" + f"Bill: {table_bill:.2f}"

    def get_free_tables_info(self):
        free_tables_info = [t.free_table_info() for t in self.tables_repository if not t.is_reserved]
        return '\n'.join(free_tables_info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
