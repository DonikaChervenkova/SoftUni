class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def names_of_attendees(self):
        return ", ".join([person.name for person in self.people])

    def numbers_of_guests(self):
        return len(self.people)


party = Party()

command = input()
while command != "End":
    name = command
    person = Person(name)
    party.invite(person)

    command = input()

print(f"Going: {party.names_of_attendees()}")
print(f"Total: {party.numbers_of_guests()}")