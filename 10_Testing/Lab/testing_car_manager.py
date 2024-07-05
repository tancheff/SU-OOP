from Lab.car_manager import Car
import unittest


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car("test_make", "test_model",
                       10, 222)

    def test_object_initialization(self):
        # self.car.make = "test_make"
        self.assertEqual(self.car.make, "test_make")

    def test_make_getter(self):
        self.assertEqual("test_make", self.car.make)

    def test_make_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_getter(self):
        self.assertEqual("test_model", self.car.model)

    def test_model_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_consumption_getter(self):
        self.assertEqual(10, self.car.fuel_consumption)

    def test_consumption_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_capacity_getter(self):
        self.assertEqual(self.car.fuel_capacity, 222)

    def test_capacity_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_amount_getter(self):
        self.assertEqual(0, self.car.fuel_amount)

    def test_amount_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_positive_val(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_negative_val(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_more_than_capacity(self):
        self.car.refuel(self.car.fuel_capacity + 10)
        self.assertEqual(self.car.fuel_capacity, self.car.fuel_capacity)

    def test_drive_enough_fuel(self):
        self.car.refuel(30)
        self.car.drive(50)
        self.assertEqual(25, self.car.fuel_amount)

    def test_car_drive_not_enough_fuel(self):
        self.car.refuel(30)

        with self.assertRaises(Exception) as ex:
            self.car.drive(500)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
