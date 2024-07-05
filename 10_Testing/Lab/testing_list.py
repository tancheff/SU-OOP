from Lab.list import IntegerList
import unittest


class IntegerListTest(unittest.TestCase):
    def setUp(self):
        self.integerlist = IntegerList(1, 2, 3, 0.1, 0.2, "Test", True)

    def test_object_is_initialized(self):
        self.assertEqual([1, 2, 3], self.integerlist.get_data())
        # self.assertEqual(3, len(self.integerlist._IntegerList__data))

    def test_get_data(self):
        self.assertEqual([1, 2, 3], self.integerlist.get_data())

    def test_add_integer(self):
        self.integerlist.add(5)
        self.assertEqual(self.integerlist.get_data(), [1, 2, 3, 5])

    def test_add_not_integer(self):
        # Act
        with self.assertRaises(ValueError) as ex:
            self.integerlist.add("TEST")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_and_return_it(self):
        idx = len(self.integerlist.get_data()) - 1

        self.assertEqual(3, self.integerlist.remove_index(idx))

    def test_remove_index_out_of_range(self):
        idx = len(self.integerlist.get_data())
        with self.assertRaises(IndexError) as ex:
            self.integerlist.remove_index(idx)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_element(self):
        self.assertEqual(1, self.integerlist.get(0))

    def test_get_index_out_of_range(self):
        idx = len(self.integerlist.get_data())
        with self.assertRaises(IndexError) as ex:
            self.integerlist.get(idx)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert(self):
        self.integerlist.insert(0, 7)
        self.assertEqual([7, 1, 2, 3], self.integerlist.get_data())

    def test_insert_wrong_data_type(self):
        with self.assertRaises(ValueError) as ex:
            self.integerlist.insert(0, "TEST")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_index_out_of_range(self):
        idx = len(self.integerlist.get_data())

        with self.assertRaises(IndexError) as ex:
            self.integerlist.insert(idx, 7)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_biggest(self):
        self.assertEqual(3, self.integerlist.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.integerlist.get_index(1))


if __name__ == "__main__":
    unittest.main()
