from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply, Food, Drink] = []

    def add_player(self, *players):
        added_player_names = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_player_names.append(player.name)
        return f"Successfully added: {', '.join(added_player_names)}"

    def add_supply(self, *supplies):
        for s in supplies:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):

        # find player
        searched_player = [p for p in self.players if p.name == player_name]
        if searched_player:
            player = searched_player[0]

            # if NO need sustain
            if not player.need_sustenance:
                return f"{player_name} have enough stamina."

            # if suppl is VALID
            if sustenance_type in ("Drink", "Food"):
                # FOOD
                if sustenance_type == "Food":
                    try:
                        food = [f for f in self.supplies if f.__class__.__name__ == sustenance_type][-1]
                    except IndexError:
                        raise Exception("There are no food supplies left!")

                    # get energy
                    new_stamina = player.stamina + food.energy
                    if new_stamina > 100:
                        new_stamina = 100
                    player.stamina = new_stamina
                    idx_of_food_to_remove = [idx for idx, f in enumerate(self.supplies) if f.__class__.__name__ == sustenance_type][-1]
                    self.supplies.pop(idx_of_food_to_remove)
                    return f"{player_name} sustained successfully with {food.name}."

                # Drink
                elif sustenance_type == "Drink":
                    try:
                        drink = [d for d in self.supplies if d.__class__.__name__ == sustenance_type][-1]
                    except IndexError:
                        raise Exception("There are no drink supplies left!")

                    # get energy
                    new_stamina = player.stamina + drink.energy
                    if new_stamina > 100:
                        new_stamina = 100
                    player.stamina = new_stamina
                    # self.supplies.remove(drink)
                    idx_of_drink_to_remove = [idx for idx, d in enumerate(self.supplies) if d.__class__.__name__ == sustenance_type][-1]
                    self.supplies.pop(idx_of_drink_to_remove)
                    return f"{player_name} sustained successfully with {drink.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_1 = [p for p in self.players if p.name == first_player_name][0]
        player_2 = [p for p in self.players if p.name == second_player_name][0]

        # check stamina
        if player_1.stamina == 0 and player_2.stamina == 0:
            return f"Player {player_1.name} does not have enough stamina.\n" + f"Player {player_2.name} does not have enough stamina."
        elif player_1.stamina == 0:
            return f"Player {player_1.name} does not have enough stamina."
        elif player_2.stamina == 0:
            return f"Player {player_2.name} does not have enough stamina."

        # DUEL
        first_player_to_hit = None
        second_player_to_hit = None

        if player_1.stamina < player_2.stamina:
            first_player_to_hit = player_1
            second_player_to_hit = player_2
        else:
            first_player_to_hit = player_2
            second_player_to_hit = player_1

        # first player hit second player
        damage_player_1 = first_player_to_hit.stamina * 0.5
        new_stamina_of_player_2 = second_player_to_hit.stamina - damage_player_1

        # if 2-nd player stamina <= 0
        if new_stamina_of_player_2 <= 0:
            new_stamina_of_player_2 = 0
            second_player_to_hit.stamina = 0
            return f"Winner: {first_player_to_hit.name}"

        # set new stamina to 2-nd
        second_player_to_hit.stamina = new_stamina_of_player_2

        # 2-nd player hit 1-st player
        damage_player_2 = second_player_to_hit.stamina * 0.5
        new_stamina_of_player_1 = first_player_to_hit.stamina - damage_player_2

        # if 1-st player stamina <= 0
        if new_stamina_of_player_1 <= 0:
            new_stamina_of_player_1 = 0
            first_player_to_hit.stamina = 0
            return f"Winner: {second_player_to_hit.name}"

        # set new stamina to 1-st
        first_player_to_hit.stamina = new_stamina_of_player_1

        # check winner
        if first_player_to_hit.stamina > second_player_to_hit.stamina:
            return f"Winner: {first_player_to_hit.name}"
        else:
            return f"Winner: {second_player_to_hit.name}"

    def next_day(self):
        for player in self.players:
            amount = player.age * 2
            new_stamina = player.stamina - amount

            if new_stamina <= 0:
                player.stamina = 0
            else:
                player.stamina = new_stamina

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))

        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)




