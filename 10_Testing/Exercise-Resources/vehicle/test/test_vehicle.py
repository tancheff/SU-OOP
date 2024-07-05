from unittest import TestCase
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(11.1, 22.2)

    def test_object_is_initialized(self):
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
        self.assertEqual(self.vehicle.fuel, 11.1)
        self.assertEqual(self.vehicle.capacity, 11.1)
        self.assertEqual(self.vehicle.horse_power, 22.2)

    def test_drive_without_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_successfully(self):
        self.vehicle.drive(2)
        self.assertEqual(self.vehicle.fuel, 11.1 - self.vehicle.fuel_consumption*2)

    def test_refuel_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_successfully(self):
        self.vehicle.drive(4)
        self.vehicle.refuel(5)
        self.assertEqual(self.vehicle.fuel, 11.1)

    def test_print_string(self):
        self.assertEqual(self.vehicle.__str__(),
                         f"The vehicle has {self.vehicle.horse_power} "
                         f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption")


if __name__ == "__main__":
    main()