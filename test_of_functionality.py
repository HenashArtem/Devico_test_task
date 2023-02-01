import unittest
from animal_legs import AnimalsCounter


class TestAnimalCounter(unittest.TestCase):

    def setUp(self):
        self.animals_counter = AnimalsCounter()

    def test_of_legs_counting(self):
        self.assertEqual(self.animals_counter.get_total_number_of_animals_legs(), 132)


if __name__ == "__main__":
    unittest.main()


