from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TennisPlayerTest(TestCase):
    def setUp(self):
        self.player = TennisPlayer("test_name", 18, 100)

    def test_initialisation(self):
        self.assertEqual(self.player.name, "test_name")
        self.assertEqual(self.player.age, 18)
        self.assertEqual(self.player.points, 100)
        self.assertEqual(self.player.wins, [])

    def test_name_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = "z"

        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_name_setter_successfully(self):
        self.player.name = "test_name_2"

        self.assertEqual(self.player.name, "test_name_2")

    def test_age_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 15

        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_age_setter_successfully(self):
        self.player.age = 25
        self.assertEqual(self.player.age, 25)

    def test_add_new_win_error(self):
        self.player.wins.append("USA Open")

        self.assertEqual(self.player.add_new_win("USA Open"),
                         "USA Open has been already added to the list of wins!")

    def test_add_new_win_successfully(self):
        self.player.add_new_win("USA Open")
        self.assertEqual(self.player.wins, ["USA Open"])

    def test_less_than_better(self):
        player_2 = TennisPlayer("test_name_2", 20, 150)

        self.assertEqual(self.player.__lt__(player_2),
                         "test_name_2 is a top seeded player and he/she is better than test_name")

    def test_less_than_worse(self):
        player_2 = TennisPlayer("test_name_2", 20, 50)

        self.assertEqual(self.player.__lt__(player_2),
                         "test_name is a better player than test_name_2")

    def test_str(self):
        self.player.wins.append("USA Open")

        result = f"Tennis Player: {self.player.name}\n" \
                 f"Age: {self.player.age}\n" \
                 f"Points: {self.player.points:.1f}\n" \
                 f"Tournaments won: {', '.join(self.player.wins)}"

        self.assertEqual(self.player.__str__(),
                         result)


if __name__ == "__main__":
    main()
