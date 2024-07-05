from unittest import TestCase
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("test_name", "test_type", "test_sound")

    def test_object_is_initialized(self):
        self.assertEqual(self.mammal.name, "test_name")
        self.assertEqual(self.mammal.type, "test_type")
        self.assertEqual(self.mammal.sound, "test_sound")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(),
                         "test_name makes test_sound")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "test_name is of type test_type ")


if __name__ == "__main__":
    main()





