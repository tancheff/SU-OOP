from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TruckDriverTest(TestCase):
    def setUp(self):
        self.truck_driver = TruckDriver("test_name", 5.5)
        self.truck_driver.add_cargo_offer("Sofia", 1000)

    def test_object_is_initialized(self):
        self.assertEqual(self.truck_driver.name, "test_name")
        self.assertEqual(self.truck_driver.money_per_mile, 5.5)
        self.assertEqual(self.truck_driver.available_cargos, {"Sofia": 1000})
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_earned_money_getter(self):
        self.assertEqual(self.truck_driver._TruckDriver__earned_money, 0)

    def test_earned_money_setter(self):
        with self.assertRaises(Exception) as ex:
            self.truck_driver.earned_money = -5

        self.assertEqual(f"{self.truck_driver.name} went bankrupt.", str(ex.exception))

    def test_add_existing_cargo_offer(self):
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Sofia", 1000)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_new_cargo_offer(self):
        self.truck_driver.add_cargo_offer("Berlin", 2000)

        self.assertEqual(self.truck_driver.available_cargos,
                         {"Sofia": 1000, "Berlin": 2000})

    def test_add_new_cargo_offer_return_message(self):
        self.assertEqual(self.truck_driver.add_cargo_offer("Berlin", 2000),
                         f"Cargo for 2000 to Berlin was added as an offer.")

    def test_drive_best_cargo_offer_value_error(self):
        self.truck_driver.available_cargos.clear()
        # print(self.truck_driver.drive_best_cargo_offer())
        #
        # with self.assertRaises(ValueError) as ex:
        #     self.truck_driver.drive_best_cargo_offer()

        # self.assertEqual("There are no offers available.", str(ex.exception))

        self.assertEqual("There are no offers available.", self.truck_driver.drive_best_cargo_offer())

    def test_drive_best_cargo_location(self):
        self.assertEqual(self.truck_driver.drive_best_cargo_offer(),
                         f"{self.truck_driver.name} is driving 1000 "
                         f"to Sofia.")

        earned_money = 1000 * 5.5
        miles = 1000

        # self.assertEqual(earned_money, self.truck_driver.earned_money)
        self.assertEqual(self.truck_driver.miles, miles)

    def test_eat(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.eat(250)

        self.assertEqual(980, self.truck_driver.earned_money)

    def test_sleep(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.sleep(1000)

        self.assertEqual(955, self.truck_driver.earned_money)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.pump_gas(1500)

        self.assertEqual(500, self.truck_driver.earned_money)

    def test_repair_truck(self):
        self.truck_driver.earned_money = 10000
        self.truck_driver.repair_truck(10000)

        self.assertEqual(2500, self.truck_driver.earned_money)

    def test_check_for_activities(self):
        self.truck_driver.earned_money = 100_000

        self.truck_driver.check_for_activities(10000)

        self.assertEqual(88250, self.truck_driver.earned_money)

    def test_check_for_activities_bankrupt(self):
        self.truck_driver.earned_money = 10_000

        with self.assertRaises(ValueError) as ex:
            self.truck_driver.check_for_activities(10000)
            self.assertEqual("test_name went bankrupt.", str(ex.exception))

    def test_repr(self):
        self.assertEqual(f"{self.truck_driver.name} has {self.truck_driver.miles} miles behind his back.",
                         self.truck_driver.__repr__())


if __name__ == "__main__":
    main()
