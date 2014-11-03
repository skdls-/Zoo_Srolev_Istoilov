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
