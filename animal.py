from random import randint


class Animal:

    def __init__ (self, species, age, name, gender, weight, life_expectancy, is_vegetarian):

        self.species = species
        self.age = age
        self.name = name
        self. gender = gender
        self. weight = weight
        self.life_expectancy = life_expectancy
        self.is_vegetarian = is_vegetarian

    def grow(self, years, kilos):

        self.age += years
        self.weight += kilos

    def eat(self, food):

        self.weight += food

    def dead(self):
        random_int = randint(1, self.life_expectancy) / self.life_expectancy
        chance_of_dying = self.age / self.life_expectancy
        return random_int < chance_of_dying
