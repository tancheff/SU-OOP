from unittest import TestCase
from project.vehicles.passenger_car import PassengerCar


class TestPassengerCarClass(TestCase):
    def test_correct_drive(self):
        self.car1 = PassengerCar('Tesla', 'X', 'Vili123')
        self.car2 = PassengerCar('Toyota', 'Prius', 'Alex123')

        self.car1.drive(450)
        self.assertEqual(self.car1.battery_level, 0)
        self.assertEqual(self.car2.battery_level, 100)

        self.car2.drive(100)
        self.assertEqual(self.car1.battery_level, 0)
        self.assertEqual(self.car2.battery_level, 78)

        self.car2.drive(100)
        self.assertEqual(self.car1.battery_level, 0)
        self.assertEqual(self.car2.battery_level, 56)


# if "name" == 'main':
#     main()