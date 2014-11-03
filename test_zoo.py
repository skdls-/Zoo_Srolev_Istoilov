import unittest
from zoo import Zoo


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
        self.my_zoo.accomodate("antilope")
        self.assertListEqual(self.my_zoo.animals, ["antilope"])

    def test_calculate_incomes(self):
        self.my_zoo.calculate_income()
        self.assertEqual(self.my_zoo.budget, 1060)

if __name__ == '__main__':
    unittest.main()
