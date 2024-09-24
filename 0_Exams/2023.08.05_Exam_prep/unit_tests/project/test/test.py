from project.second_hand_car import SecondHandCar
from unittest import TestCase


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("model", "type", 1_000, 555.5)

    def test_initialisation(self):
        self.assertEqual(self.car.model, "model")
        self.assertEqual(self.car.car_type, "type")
        self.assertEqual(self.car.mileage, 1_000)
        self.assertEqual(self.car.price, 555.5)
        self.assertEqual(self.car.repairs, [])

    def test_price_setter_success(self):
        self.car.price = 444.4
        self.assertEqual(self.car.price, 444.4)

    def test_price_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 0.5

        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

    def test_mileage_setter_success(self):
        self.car.mileage = 5_000
        self.assertEqual(self.car.mileage, 5_000)

    def test_mileage_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 50
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',
                         str(ex.exception))

    def test_set_promotional_price_error(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(2_000)
        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_set_promotional_price_success(self):
        self.assertEqual(self.car.set_promotional_price(100),
                         'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 100)

    def test_need_repair_error(self):
        self.assertEqual(self.car.need_repair(1000, "some random repair"),
                         'Repair is impossible!')

    def test_need_repair_success(self):
        self.assertEqual(self.car.need_repair(100, "changed carburetor"),
                         'Price has been increased due to repair charges.')

        self.assertEqual(self.car.price, 655.5)
        self.assertEqual(self.car.repairs, ["changed carburetor"])

    def test_greater_than_error(self):
        car_2 = SecondHandCar("model2", "type2", 12_000, 2_555.5)

        self.assertEqual(self.car.__gt__(car_2), 'Cars cannot be compared. Type mismatch!')

    def test_greater_than_success(self):
        car_2 = SecondHandCar("model", "type", 12_000, 2_555.5)

        self.assertEqual(self.car.__gt__(car_2), False)

    def test_str(self):
        result = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""

        self.assertEqual(self.car.__str__(), result)