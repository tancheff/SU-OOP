class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


# = = = = = UNIT TESTS = = = = =

import unittest


class WorkerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_object_is_initialized_correctly(self):
        # Assert
        worker = Worker("Test", 1000, 60)
        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(60, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works(self):
        # Arrange
        worker = Worker("Test", 1000, 60)
        self.assertEqual(60, worker.energy)
        self.assertEqual(0, worker.money)

        # Act
        worker.work()

        # Assert
        self.assertEqual(59, worker.energy)
        self.assertEqual(worker.salary, worker.money)

        # Worker Works Again
        worker.work()
        self.assertEqual(58, worker.energy)
        self.assertEqual(worker.salary * 2, worker.money)

    def test_worker_has_no_energy_cannot_work(self):
        worker = Worker("Test", 1000, 0)

        self.assertEqual(0, worker.energy)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", ex.exception.args[0])

    def test_worker_energy_is_increased_when_resting(self):
        # Arrange
        worker = Worker("Test", 1000, 60)
        self.assertEqual(60, worker.energy)

        # Act
        worker.rest()
        self.assertEqual(61, worker.energy)

        worker.rest()
        self.assertEqual(62, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker("Test", 1000, 60)

        # Act
        self.assertEqual("Test has saved 0 money.",
                         f'{worker.name} has saved {worker.money} money.')


if __name__ == "__main__":
    unittest.main()
