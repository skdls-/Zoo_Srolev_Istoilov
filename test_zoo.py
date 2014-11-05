import unittest
from zoo import Zoo
from animal import Animal


class TestZoo(unittest.TestCase):

    def setUp(self):
        animals = []
        capacity = 200
        budget = 1000
        self.my_zoo = Zoo(animals, capacity, budget)

    def test_init(self):
        self.assertListEqual(self.my_zoo.animals, [])
        self.assertEqual(self.my_zoo.capacity, 200)
        self.assertEqual(self.my_zoo.budget, 1000)
        self.assertEqual(self.my_zoo.DAILY_INCOME, 60)
        self.assertEqual(self.my_zoo.KILO_MEAT, 4)
        self.assertEqual(self.my_zoo.KILO_VEG_FOOD, 2)

    def test_accomodate(self):
        animal = Animal("cat", 2, "Kat", "male", 2, 15, False, 2, 2, 5)
        self.my_zoo.accomodate(animal)
        self.assertListEqual(self.my_zoo.animals, [animal])

    def test_calculate_incomes(self):
        animal = Animal("cat", 2, "Kat", "male", 2, 15, False, 2, 2, 5)
        self.my_zoo.accomodate(animal)
        self.my_zoo.calculate_income()
        self.assertEqual(self.my_zoo.budget, 1060)

    def test_calculate_outcome(self):
        animal = Animal("cat", 2, "Kat", "male", 2, 15, False, 2, 2, 5)
        self.my_zoo.accomodate(animal)
        self.my_zoo.calculate_outcome()
        self.assertEqual(self.my_zoo.budget, 998)

    def test_reproduce(self):
        animal = Animal("cat", 2, "Kat", "male", 2, 15, False, 2, 2, 5)
        self.my_zoo.accomodate(animal)
        animal = Animal("cat", 2, "Kate", "female", 3, 15, False, 2, 2, 5)
        self.my_zoo.accomodate(animal)
        self.my_zoo.reproduce()


if __name__ == '__main__':
    unittest.main()
