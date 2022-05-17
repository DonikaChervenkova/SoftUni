from project.people.child import Child
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += (room.expenses + room.room_cost)
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []

        for room in self.rooms:
            total_cost_per_room = room.expenses + room.room_cost
            if room.budget >= total_cost_per_room:
                room.budget -= total_cost_per_room
                result.append(f"{room.family_name} paid {total_cost_per_room:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return "\n".join(result)

    def status(self):
        result = ""

        result += f"Total population: {sum([r.members_count for r in self.rooms])}\n"
        for r in self.rooms:
            result += f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n"
            if hasattr(r, 'children'):
                counter = 0
                for c in r.children:
                    counter += 1
                    result += f"--- Child {counter} monthly cost: {c.get_monthly_expense():.2f}$\n"
            if hasattr(r, 'appliances'):
                result += f"--- Appliances monthly cost: {sum([item.get_monthly_expense() for item in r.appliances]):.2f}$\n"

        return result
