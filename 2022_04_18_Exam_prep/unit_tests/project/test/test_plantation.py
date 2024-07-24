import unittest

from project.plantation import Plantation
from unittest import TestCase


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(50)
        self.plantation.plants["rose"] = [1, 1, 1, 1, 1]
        self.plantation.workers.append("Mario")

    def test_initialization(self):
        self.assertEqual(self.plantation.size, 50)
        self.assertEqual(self.plantation.plants, {"rose": [1, 1, 1, 1, 1]})
        self.assertEqual(self.plantation.workers, ["Mario"])

    def test_size_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Mario")

        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_successfully(self):
        worker = "Ivan"

        self.assertEqual(self.plantation.hire_worker(worker),
                         f"{worker} successfully hired.")

    def test_len(self):
        self.plantation.plants["sunflower"] = [1, 1, 1, 1, 1, 1]
        self.assertEqual(len(self.plantation), 11)

    def test_planting_wrong_worker(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Pesho", "tomato")

        self.assertEqual("Worker with name Pesho is not hired!", str(ex.exception))

    def test_planting_full_plantation(self):
        self.plantation.size = 0

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Mario", "tomato")

        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_successfully(self):
        self.plantation.plants["Pesho"] = []
        self.plantation.workers.append("Pesho")
        # print(self.plantation.plants)

        self.assertEqual(self.plantation.planting("Pesho", "tomato"),
                         "Pesho planted tomato.")

    def test_planted_first_plant(self):
        self.plantation.workers.append("Pesho")
        self.assertEqual(self.plantation.planting("Pesho", "tomato"),
                         "Pesho planted it's first tomato.")

    def test_str_method_no_plants(self):
        """Test the __str__ method when there are no plants"""
        plantation = Plantation(size=50)
        plantation.hire_worker("Charlie")
        expected_output = (
            "Plantation size: 50\n"
            "Charlie"
        )
        self.assertEqual(str(plantation), expected_output)

    def test_str_method_no_workers(self):
        """Test the __str__ method when there are no workers"""
        plantation = Plantation(size=75)
        expected_output = (
            "Plantation size: 75\n"
        )
        self.assertEqual(str(plantation), expected_output)

    def test_str_method_empty_plantations(self):
        self.plantation.workers.append("Pesho")
        result = ''
        result += f'Size: {self.plantation.size}\n'
        result += f'Workers: {", ".join(self.plantation.workers)}'


        self.assertEqual(result.strip(), self.plantation)

    def test_str_method_multiple_plants_per_worker(self):
        """Test the __str__ method with multiple plants per worker"""
        plantation = Plantation(size=100)
        plantation.hire_worker("Eve")
        plantation.planting("Eve", "Fern")
        plantation.planting("Eve", "Cactus")
        expected_output = (
            "Plantation size: 100\n"
            "Eve\n"
            "Eve planted: Fern, Cactus"
        )
        self.assertEqual(str(plantation), expected_output)

    def test_str_method_no_plants_for_some_workers(self):
        """Test the __str__ method when some workers have no plants"""
        plantation = Plantation(size=100)
        plantation.hire_worker("Frank")
        plantation.hire_worker("Grace")
        plantation.planting("Frank", "Lily")
        expected_output = (
            "Plantation size: 100\n"
            "Frank, Grace\n"
            "Frank planted: Lily"
        )
        self.assertEqual(str(plantation), expected_output)


if __name__ == '__main__':
    unittest.main()
