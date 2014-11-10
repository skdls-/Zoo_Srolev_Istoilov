import json
import random
import string
from animal import Animal


class Zoo:
    DAILY_INCOME = 60
    KILO_MEAT = 4
    KILO_VEG_FOOD = 2
    SIX_MONTHS = 180

    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget

    def accomodate(self, animal):
        self.animals.append(animal)

    def calculate_income(self):
        for animal in self.animals:
            self.budget += Zoo.DAILY_INCOME

    def calculate_outcome(self):
        outcome = 0
        for animal in self.animals:
            if animal.food_type == "carnivore":
                outcome += Zoo.KILO_MEAT * animal.food_weight
            else:
                outcome += Zoo.KILO_VEG_FOOD * animal.food_weight

        return outcome

    def die(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def get_pregnant(self, species, animal):
        males = [animal.gender for animal in self.animals if animal.species == species and animal.age >= Zoo.SIX_MONTHS]
        has_male = "male" in males
        animal_is_female = animal.gender == "female"
        is_pregnant = animal.is_pregnant
        not_pregnant_time = animal.not_pregnant_for >= Zoo.SIX_MONTHS
        old_enough = animal.age > Zoo.SIX_MONTHS
        if has_male and animal_is_female and not is_pregnant and not_pregnant_time and old_enough:
            animal.is_pregnant = True
        else:
            animal.not_pregnant_for += 1

    def bear(self, animal):
        ready_to_bear = animal.pregnant_for == animal.gestation_period
        if animal.is_pregnant and ready_to_bear:
            newborn = self.add_newborn(animal)
            self.animals.append(newborn)
            animal.pregnant_for = 0
            animal.not_pregnant_for = 0
            animal.is_pregnant = False
            kid_string = "{}: {}, {}, kid of {} is born!\n"
            return kid_string.format(newborn.name, newborn.species, newborn.gender, animal.name)
        return ""

    def give_name(self, length):
        name = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return name

    def determine_gender(self):
        gender_percent = random.randint(0, 100)
        if gender_percent <= 50:
            gender = "male"
        else:
            gender = "female"

        return gender

    def add_newborn(self, animal):
        species = animal.species
        age = 0
        name = self.give_name(6)
        gender = self.determine_gender()
        weight = animal.newborn_average_weight
        newborn = Animal(species, age, name, gender, weight)
        return newborn

    def reproduce(self):
        all_animals = [animal.species for animal in self.animals]
        all_animals = set(all_animals)
        born_animals = ""
        for species in all_animals:
            for animal in self.animals:
                self.get_pregnant(species, animal)

                if animal.is_pregnant:
                    animal.pregnant_for += 1
                    animal.not_pregnant_for = 0

                born_animals += self.bear(animal)

        return born_animals

    def load_zoo(self, filename):
        file = open(filename, "r")
        load_data = json.loads(file.read())
        file.close()
        for animal in load_data:
            anim = Animal(animal["species"], animal["age"], animal["name"], animal["gender"], animal["weight"])
            self.animals.append(anim)

    def save(self, filename):
        dict = []
        for animal in self.animals:
            dict.append(animal.__dict__)
        file = open(filename, "w")
        json_text = json.dumps(dict, indent=4, separators=(',', ': '))
        file.write(json_text)

        file.close()

    def __str__(self):
        output = ""
        for animal in self.animals:
            name = animal.name
            species = animal.species
            age = animal.age / 30
            weight = animal.weight
            output += "{}: {}, {} months, {} kilograms\n".format(name, species, age, weight)

        return output
