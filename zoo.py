import json
import random
import string
from animal import Animal


class Zoo:

    def __init__(self, animals, capacity, budget):
        self.DAILY_INCOME = 60
        self.KILO_MEAT = 4
        self.KILO_VEG_FOOD = 2
        self.animals = animals
        self.capacity = capacity
        self.budget = budget

    def accomodate(self, animal):
        self.animals.append(animal)

    def calculate_income(self):
        for animal in self.animals:
            self.budget += 60

    def calculate_outcome(self):
        outcome = 0
        for animal in self.animals:
            if animal.food_type == "carnivore":
                outcome += self.KILO_MEAT * animal.food_weight_ratio
            else:
                outcome += self.KILO_VEG_FOOD * animal.food_weight_ratio

        self.budget -= outcome

    def die(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

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
        gender = self.determine_gender()
        name = self.give_name(6)
        weight = 0
        average_weight = animal.average_weight
        life_expectancy = animal.life_expectancy
        is_vegetarian = animal.is_vegetarian
        gestation_period = animal.gestation_period
        food_per_day = animal.food_per_day
        average_weight = animal.average_weight
        newborn = Animal(species, 0, name, gender, weight, life_expectancy, is_vegetarian, gestation_period, food_per_day, average_weight)
        return newborn

    def reproduce(self):
        all_animals = [animal.species for animal in self.animals]
        all_animals = set(all_animals)
        for species in all_animals:
            for animal in self.animals:
                males = [animal.gender for animal in self.animals if animal.species == species]
                has_male = "male" in males
                animal_is_female = animal.gender == "female"
                pregnant = animal.is_pregnant is False
                is_not_pregnant = animal.not_pregnant_for >= 182
                if has_male and animal_is_female and pregnant and is_not_pregnant:
                        animal.is_pregnant = True
                        animal.pregnant_for += 1
                        animal.not_pregnant_for = 0
                else:
                    animal.not_pregnant_for += 1

                if animal.is_pregnant and animal.pregnant_for == animal.gestation_period:
                    newborn = self.add_newborn(animal)
                    self.animals.append(newborn)


    def load_zoo(self, filename):

        with open(filename, 'r') as load_zoo:
            load_data = json.load(load_zoo)
            loaded_zoo = Zoo(load_data, 50, 1000)
            for animal in load_data:
                anim = Animal(animal["name"], animal["gender"], animal["weight"], animal["life_expectancy"], animal["is_vegetarian"], animal["gestation_period"], animal["food_per_day"], animal["average_weight"])
                loaded_zoo.accomodate(anim)
            return loaded_zoo

    def save(self, filename):

        #"name": filename
        dict = {"name": filename, "animals": []}
        for animal in self.animals:
            dict["animals"].append(animal.__dict__)
        file = open(filename, "w")
        json_text = json.dumps(dict, indent=4, separators=(',', ': '))
        file.write(json_text)

        file.close()
