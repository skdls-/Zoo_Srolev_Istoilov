import json
from animal import Animal


class Zoo:

    def __init__(self, animals, capacity, budget):
        self.DAILY_INCOME = 60
        self.KILO_MEAT = 4
        self.KILO_VEG_FOOD = 2
        self. animals = animals
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
            if animal.is_vegetarian:
                outcome += self.KILO_VEG_FOOD
            else:
                outcome += self.KILO_MEAT

        self.budget -= outcome

    def die(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

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


