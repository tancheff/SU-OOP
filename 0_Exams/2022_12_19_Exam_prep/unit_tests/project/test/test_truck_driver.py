from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTest(TestCase):
    def setUp(self):
        self.truck_driver = TruckDriver("test_name", 5.5)
        self.truck_driver.add_cargo_offer("Sofia", 1_000)

    def test_object_is_initialized(self):
        self.assertEqual(self.truck_driver.name, "test_name")
        self.assertEqual(self.truck_driver.money_per_mile, 5.5)
        self.assertEqual(self.truck_driver.available_cargos, {"Sofia": 1_000})
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_earned_money_getter(self):
        self.truck_driver.earned_money = 100
        self.assertEqual(self.truck_driver._TruckDriver__earned_money, 100)

    def test_earned_money_setter(self):
        with self.assertRaises(Exception) as ex:
            self.truck_driver.earned_money = -5

        self.assertEqual(f"{self.truck_driver.name} went bankrupt.", str(ex.exception))

    def test_add_existing_cargo_offer(self):
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Sofia", 1_000)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_new_cargo_offer(self):
        self.assertEqual(self.truck_driver.add_cargo_offer("Berlin", 2_000),
                         f"Cargo for 2000 to Berlin was added as an offer.")

        self.assertEqual(self.truck_driver.available_cargos,
                         {"Sofia": 1_000, "Berlin": 2_000})

    def test_drive_best_cargo_offer_value_error(self):
        self.truck_driver.available_cargos.clear()
        self.assertEqual(self.truck_driver.drive_best_cargo_offer(),
                         "There are no offers available.")

    def test_drive_best_cargo_location(self):
        self.assertEqual(self.truck_driver.drive_best_cargo_offer(),
                         f"{self.truck_driver.name} is driving 1000 to Sofia.")

        self.assertEqual(self.truck_driver.miles, 1_000)

    def test_eat(self):
        self.truck_driver.earned_money = 1_000
        self.truck_driver.eat(250)

        self.assertEqual(980, self.truck_driver.earned_money)

    def test_sleep(self):
        self.truck_driver.earned_money = 1_000
        self.truck_driver.sleep(1_000)

        self.assertEqual(955, self.truck_driver.earned_money)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 1_000
        self.truck_driver.pump_gas(1_500)

        self.assertEqual(500, self.truck_driver.earned_money)

    def test_repair_truck(self):
        self.truck_driver.earned_money = 10_000
        self.truck_driver.repair_truck(10_000)

        self.assertEqual(2_500, self.truck_driver.earned_money)

    def test_check_for_activities(self):
        self.truck_driver.earned_money = 100_000

        self.truck_driver.check_for_activities(10_000)

        self.assertEqual(88_250, self.truck_driver.earned_money)

    def test_check_for_activities_bankrupt(self):
        self.truck_driver.earned_money = 10_000

        with self.assertRaises(ValueError) as ex:
            self.truck_driver.check_for_activities(10_000)
            self.assertEqual("test_name went bankrupt.", str(ex.exception))

    def test_repr(self):
        self.assertEqual(f"{self.truck_driver.name} has {self.truck_driver.miles} miles behind his back.",
                         self.truck_driver.__repr__())


if __name__ == "__main__":
    main()
