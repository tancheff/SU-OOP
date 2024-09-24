from project.soccer_player import SoccerPlayer
from unittest import TestCase


class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player = SoccerPlayer("Testname", 20, 200, "PSG")

    def test_initialisation(self):
        self.assertEqual(self.player.name, "Testname")
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.goals, 200)
        self.assertEqual(self.player.team, "PSG")
        self.assertEqual(self.player.achievements, {})

    def test_name_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Pesho"
        self.assertEqual("Name should be more than 5 symbols!", str(ve.exception))

    def test_age_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 15
        self.assertEqual("Players must be at least 16 years of age!", str(ve.exception))

    def test_goals_setter_correction(self):
        self.player.goals = -5
        self.assertEqual(self.player.goals, 0)

    def test_team_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.team = "LOKO PLVD"
        self.assertEqual(f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!",
                         str(ve.exception))

    def test_change_team_invalid_team(self):
        self.assertEqual(self.player.change_team("LOKO PLVD"),
                         "Invalid team name!")

        self.assertEqual(self.player.team, "PSG")

    def test_change_name_success(self):
        self.assertEqual(self.player.change_team("Barcelona"),
                         "Team successfully changed!")

        self.assertEqual(self.player.team, "Barcelona")

    def test_add_new_achievement_existing(self):
        self.player.achievements["Golden Shoe"] = 1

        self.assertEqual(self.player.add_new_achievement("Golden Shoe"),
                         f"Golden Shoe has been successfully added to the achievements collection!")

        self.assertEqual(self.player.achievements, {"Golden Shoe": 2})

    def test_add_new_achievement_that_doesnt_exist(self):
        self.player.achievements["Golden Shoe"] = 1

        self.assertEqual(self.player.add_new_achievement("MVP Award"),
                         f"MVP Award has been successfully added to the achievements collection!")

        self.assertEqual(self.player.achievements, {"Golden Shoe": 1, "MVP Award": 1})

    def test_less_than_lesser(self):
        player_2 = SoccerPlayer("Testname2", 30, 300, "PSG")

        self.assertEqual(self.player.__lt__(player_2),
                         "Testname2 is a top goal scorer! S/he scored more than Testname.")

    def test_less_than_greater(self):
        player_2 = SoccerPlayer("Testname2", 20, 100, "PSG")

        self.assertEqual(self.player.__lt__(player_2),
                         "Testname is a better goal scorer than Testname2.")
