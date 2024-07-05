class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


# = = = = = UNIT TESTS = = = = =

import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Test")

    # NB! този метод го няма в условието на задачата !!!
    def test_object_is_initialized(self):
        self.assertEqual(self.cat.name, "Test")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_size_increases_after_eating(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        self.cat.eat()

        self.assertEqual(1, self.cat.size)
        self.assertTrue(self.cat.fed)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_after_being_fed(self):
        # Arrange
        self.cat.eat()

        # Act
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_cannot_sleep_if_not_fed(self):
        self.assertFalse(self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

        self.assertFalse(self.cat.fed)

    def test_cat_not_sleepy_after_sleeping(self):
        self.cat.fed = True
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    # NB! този метод го няма в условието на задачата !!!
    def test_cat_is_not_hungry_can_go_to_sleep(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
