import unittest 
from animal import Animal


class TestAnimal(unittest.TestCase):

    def setUp(self):

        self.my_animal = Animal("cat", 5, "Cattie", "female", 4, 15, True)

    def test_init(self):

        self.assertEqual(self.my_animal.species, "cat")
        self.assertEqual(self.my_animal.age, 5)
        self.assertEqual(self.my_animal.name, "Cattie")
        self.assertEqual(self.my_animal.gender, "female")
        self.assertEqual(self.my_animal.weight, 4)
        self.assertEqual(self.my_animal.life_expectancy, 15)
        self.assertTrue(self.my_animal.is_vegetarian)

    def test_grow(self):

        self.my_animal.grow(2, 2)
        self.assertEqual(self.my_animal.age, 7)
        self.assertEqual(self.my_animal.weight, 6)

    def test_eat(self):

        self.my_animal.eat(5000)
        self.assertEqual(self.my_animal.weight, 5004)

if __name__ == '__main__':
    unittest.main()
