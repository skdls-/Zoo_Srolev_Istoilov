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
                outcome += self.KILO_MEAT
            else:
                outcome += self.KILO_VEG_FOOD

        self.budget -= outcome

    def die(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def generate_list_couples(self):
        all_animals = {}
        for animal in self.animals:
            if animal.species not in all_animals:
                all_animals[animal.species] = []

            all_animals[animal.species].append(animal.gender)

        return all_animals

    def add_newborn(self, species):
        gender = "male"
        weight = 0
        newborn = Animal(species, 0, "", gender, weight, life_expectancy, is_vegetarian, )
        return newborn

    def reproduce(self):
        all_animals = self.generate_list_couples()
        for species, gender_list in all_animals.items():
            if gender_list.count("males") > gender_list.count("females"):
                number_of_couples = gender_list.count("females")
            else:
                number_of_couples = gender_list.count("males")

                for couple in number_of_couples:
                    newborn = self.add_newborn(species)
                    self.animals.append(newborn)
