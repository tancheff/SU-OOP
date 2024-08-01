from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("007", "Military", 100, 5_000)

    def test_initialisation(self):
        self.assertEqual(self.robot.robot_id, "007")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 5_000)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.ALLOWED_CATEGORIES,
                         ['Military', 'Education', 'Entertainment', 'Humanoids'])
        self.assertEqual(self.robot.PRICE_INCREMENT, 1.5)

    def test_category_setter_success(self):
        self.robot.category = "Education"
        self.assertEqual(self.robot.category, "Education")

    def test_category_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "test_category"

        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'",
                         str(ex.exception))

    def test_price_setter_success(self):
        self.robot.price = 10_000
        self.assertEqual(self.robot.price, 10_000)

    def test_price_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = -5

        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_upgrade_existing_hardware(self):
        self.robot.hardware_upgrades.append("motherboard")

        self.assertEqual(self.robot.upgrade("motherboard", 2_000),
                         "Robot 007 was not upgraded.")

    def test_upgrade_new_hardware(self):
        self.assertEqual(self.robot.upgrade("motherboard", 5_000),
                         "Robot 007 was upgraded with motherboard.")

        self.assertEqual(self.robot.hardware_upgrades, ["motherboard"])
        self.assertEqual(self.robot.price, 12_500)

    def test_update_lower_version(self):
        self.robot.software_updates.append(2.5)

        self.assertEqual(self.robot.update(2.1, 20),
                         "Robot 007 was not updated.")

        self.assertEqual(self.robot.software_updates, [2.5])

    def test_update_not_enough_capacity(self):
        self.assertEqual(self.robot.update(2, 150),
                         "Robot 007 was not updated.")

        self.assertEqual(self.robot.software_updates, [])

    def test_update_success(self):
        self.assertEqual(self.robot.update(2.5, 80),
                         "Robot 007 was updated to version 2.5.")

        self.assertEqual(self.robot.software_updates, [2.5])
        self.assertEqual(self.robot.available_capacity, 20)

    def test_greater_than_greater(self):
        robot_2 = Robot("008", "Education", 110, 4_000)

        self.assertEqual(self.robot.__gt__(robot_2),
                         "Robot with ID 007 is more expensive than Robot with ID 008.")

    def test_greater_than_equal(self):
        robot_2 = Robot("008", "Education", 110, 5_000)

        self.assertEqual(self.robot.__gt__(robot_2),
                         "Robot with ID 007 costs equal to Robot with ID 008.")

    def test_greater_than_lower(self):
        robot_2 = Robot("008", "Education", 110, 6_000)

        self.assertEqual(self.robot.__gt__(robot_2),
                         "Robot with ID 007 is cheaper than Robot with ID 008.")





















