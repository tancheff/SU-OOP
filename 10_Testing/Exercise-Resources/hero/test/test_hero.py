from unittest import TestCase
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Test", 11, 22.5, 33.5)
        self.enemy_hero = Hero("Test2", 11, 22.5, 33.5)

    def test_object_is_initialized(self):
        self.assertEqual("Test", self.hero.username)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(22.5, self.hero.health)
        self.assertEqual(33.5, self.hero.damage)

    def test_battle_same_name(self):
        new_enemy_hero = Hero("Test", 11, 22.5, 33.5)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(new_enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_without_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest",
                         str(ex.exception))

    def test_battle_enemy_hero_has_no_health(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest",
                         str(ex.exception))

    def test_battle_draw(self):
        new_enemy_hero = Hero("Test2", 11, 22.5, 33.5)
        self.assertEqual(self.hero.battle(new_enemy_hero), "Draw")

        self.assertLess(self.hero.health, 0)
        self.assertLess(new_enemy_hero.health, 0)

    def test_battle_win(self):
        new_enemy_hero = Hero("Test2", 2, 1.1, 2.2)
        self.assertEqual(self.hero.battle(new_enemy_hero), "You win")

        # self.assertLess(enemy_hero.health, 0)
        self.assertEqual(self.hero.level, 12)
        self.assertEqual(self.hero.health, 22.5 - new_enemy_hero.damage * new_enemy_hero.level + 5)
        self.assertEqual(self.hero.damage, 38.5)

    def test_battle_loose(self):
        new_enemy_hero = Hero("Test2", 11, 2200.5, 33.5)
        self.assertEqual(self.hero.battle(new_enemy_hero), "You lose")

        self.assertLess(self.hero.health, 0)

        self.assertEqual(new_enemy_hero.level, 12)
        self.assertEqual(new_enemy_hero.health, 2200.5 - self.hero.damage * self.hero.level + 5)
        self.assertEqual(new_enemy_hero.damage, 38.5)

    def test_print_class_hero(self):
        self.assertEqual(self.hero.__str__(),
                         f"Hero {self.hero.username}: "
                         f"{self.hero.level} lvl\n"
                         f"Health: {self.hero.health}\n"
                         f"Damage: {self.hero.damage}\n"
                         )


if __name__ == "__main__":
    main()
