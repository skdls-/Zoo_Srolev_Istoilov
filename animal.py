from random import randint


class Animal:

    def __init__(self, species, age, name, gender, weight, life_expectancy, is_vegetarian, gestation_period, food_per_day, average_weight):

        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.life_expectancy = life_expectancy
        self.is_vegetarian = is_vegetarian
        self.gestation_period = gestation_period
        self.food_per_day = food_per_day
        if age == 0:
            self.newborn = True
        else:
            self.newborn = False

        self.average_weight = average_weight
        self.weight_age_ratio = weight / life_expectancy
        self.food_weight_ratio = food_per_day / weight
        if self.is_vegetarian:
            self.food_type = "carnivore"
        else:
            self.food_type = "herbivore"

        self.is_pregnant = False
        self.not_pregnant_for = 0
        self.pregnant_for = 0

    def grow(self, years, kilos):

        self.age += years
        self.weight += kilos

    def eat(self, food):

        self.weight += food

    def dead(self):
        random_int = randint(1, self.life_expectancy) / self.life_expectancy
        chance_of_dying = self.age / self.life_expectancy
        return random_int < chance_of_dying
