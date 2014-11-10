from random import randint


class Animal:
    species_information = {
        "Elephant": {"average_weight": 5000, "life_expectancy": 50 * 365, "food_type": "herbivore", "gestation_period": 5 * 30, "newborn_average_weight": 100, "weight_age": 50, "food_weight": 0.1},
        "Horse": {"average_weight": 521, "life_expectancy": 15 * 365, "food_type": "herbivore", "gestation_period": 6 * 30, "newborn_average_weight": 15, "weight_age": 23, "food_weight": 0.1},
        "Cow": {"average_weight": 465, "life_expectancy": 10 * 365, "food_type": "herbivore", "gestation_period": 8 * 30, "newborn_average_weight": 10, "weight_age": 20, "food_weight": 0.1},
        "Wolf": {"average_weight": 36, "life_expectancy": 12 * 365, "food_type": "carnivore", "gestation_period": 3 * 30, "newborn_average_weight": 2, "weight_age": 2, "food_weight": 0.1},
        "Gorilla": {"average_weight": 207, "life_expectancy": 22 * 365, "food_type": "herbivore", "gestation_period": 9 * 30, "newborn_average_weight": 9, "weight_age": 11, "food_weight": 0.04},
        "Kangaroo": {"average_weight": 35, "life_expectancy": 25 * 365, "food_type": "herbivore", "gestation_period": 5 * 30, "newborn_average_weight": 1.5, "weight_age": 2, "food_weight": 0.3},
        "Koala": {"average_weight": 15, "life_expectancy": 30 * 365, "food_type": "herbivore", "gestation_period": 4 * 30, "newborn_average_weight": 1, "weight_age": 1, "food_weight": 0.4},
        "Sheep": {"average_weight": 55.5, "life_expectancy": 12 * 365, "food_type": "herbivore", "gestation_period": 2 * 30, "newborn_average_weight": 4, "weight_age": 5, "food_weight": 0.1},
        "Jaguar": {"average_weight": 100, "life_expectancy": 15 * 365, "food_type": "carnivore", "gestation_period": 13 * 30, "newborn_average_weight": 9, "weight_age": 7, "food_weight": 0.2},
        "Pig": {"average_weight": 192, "life_expectancy": 12 * 365, "food_type": "herbivore", "gestation_period": 5 * 30, "newborn_average_weight": 10, "weight_age": 10, "food_weight": 0.1},
    }

    def __init__(self, species, age, name, gender, weight,):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.average_weight = Animal.species_information[species]["average_weight"]
        self.life_expectancy = Animal.species_information[species]["life_expectancy"]
        self.food_type = Animal.species_information[species]["food_type"]
        self.gestation_period = Animal.species_information[species]["gestation_period"]
        self.newborn_average_weight = Animal.species_information[species]["newborn_average_weight"]
        self.weight_age = Animal.species_information[species]["weight_age"]
        self.food_weight = Animal.species_information[species]["food_weight"]
        self.is_pregnant = False
        self.not_pregnant_for = 180
        self.pregnant_for = 0

    def eat(self, food):
        self.weight += food
        if self.weight >= self.average_weight:
            self.weight = self.average_weight

    def dead(self):
        random_int = randint(1, self.life_expectancy) / self.life_expectancy
        chance_of_dying = self.age / self.life_expectancy
        return random_int < chance_of_dying
