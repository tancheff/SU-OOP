from project.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoreTest(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_initialisation(self):
        self.assertEqual(self.store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
                         )

    def test_add_toy_shelf_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("K", "test_name")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_already_exists(self):
        self.store.toy_shelf["A"] = "Iron Man"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Iron Man")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_shelf_is_taken(self):
        self.store.add_toy("A", "Iron Man")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Superman")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successfully(self):
        self.assertEqual(self.store.add_toy("A", "Iron Man"),
                         "Toy:Iron Man placed successfully!")

        self.assertEqual(self.store.toy_shelf["A"],
                         "Iron Man")

    def test_remove_toy_no_such_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("K", "Superman")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_no_such_toy(self):
        self.store.toy_shelf["A"] = "Iron Man"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Superman")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully(self):
        self.store.toy_shelf["A"] = "Iron Man"

        self.assertEqual(self.store.remove_toy("A", "Iron Man"),
                         "Remove toy:Iron Man successfully!")

        self.assertEqual(self.store.toy_shelf["A"], None)
