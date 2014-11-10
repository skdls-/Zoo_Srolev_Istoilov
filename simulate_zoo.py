from zoo import Zoo
from animal import Animal


class SimulateZoo:
    DAYS_IN_WEEK = 7
    DAYS_IN_MONTH = 30
    DAYS_IN_YEAR = 365

    def __init__(self, zoo):
        self.zoo = zoo

    def simulate(self, command):
        command[1] = int(command[1])
        if command[2] == "years":
            days = command[1] * SimulateZoo.DAYS_IN_YEAR
        elif command[2] == "weeks":
            days = command[1] * SimulateZoo.DAYS_IN_WEEK
        elif command[2] == "months":
            days = command[1] * SimulateZoo.DAYS_IN_MONTH
        else:
            days = command[1]

        for day in range(days):
            for animal in self.zoo.animals:
                animal.eat(5)
                animal.age += 1
                if animal.age == animal.life_expectancy:
                    print("{} {} died!".format(animal.name, animal.species))
                    self.zoo.die(animal)

            outcome = self.zoo.calculate_outcome()
            if outcome > self.zoo.budget:
                print("Bankrupt!")
            else:
                self.zoo.budget -= outcome

            newborns = self.zoo.reproduce()
            if len(newborns) > 0:
                print(newborns)

            self.zoo.calculate_income()

        print(self.zoo)

    def move_to_habitat(self, species, name):
        for animal in self.zoo.animals:
            if animal.name == name and animal.species == species:
                self.zoo.animals.remove(animal)

    def get_input(self):
        command = input("Enter command> ")
        command = command.split(" ")
        return command

    def interface(self):
        command = self.get_input()
        while command[0] != "exit":
            if command[0] == "see_animals":
                print(self.zoo)
                command = self.get_input()
            elif command[0] == "accomodate":
                species = command[0]
                name = command[1]
                age = command[2]
                weight = command[3]
                gender = ""
                new_animal = Animal(species, age, name, gender, weight)
                gender = new_animal.determine_gender()
                new_animal.gender = gender
                self.zoo.accomodate(new_animal)
            elif command[0] == "move_to_habitat":
                self.move_to_habitat(command[1], command[2])
                command = self.get_input()
            elif command[0] == "simulate":
                self.simulate(command)
                command = self.get_input()
            else:
                print("Bad input!")
                command = self.get_input()
        else:
            print("Goodbye!")


def main():
    park = Zoo([], 10, 10)
    park.load_zoo("test_dogs.txt")
    simulation = SimulateZoo(park)
    simulation.interface()

if __name__ == '__main__':
    main()
