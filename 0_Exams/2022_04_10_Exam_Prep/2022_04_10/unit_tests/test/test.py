from project.movie import Movie
from unittest import TestCase


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("test_name", 2000, 5.5)

    def test_object_is_initialized(self):
        self.assertEqual(self.movie.name, "test_name")
        self.assertEqual(self.movie.year, 2000)
        self.assertEqual(self.movie.rating, 5.5)
        self.assertEqual(self.movie.actors, [])

    def test_new_name(self):
        self.movie.name = "new_name"
        self.assertEqual(self.movie.name, "new_name")

    def test_new_name_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_movie_year(self):
        self.movie.year = 2005
        self.assertEqual(self.movie.year, 2005)

    def test_movie_year_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 100

        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor(self):
        self.movie.add_actor("test_actor")
        self.assertEqual(self.movie.actors, ["test_actor"])

    def test_add_actor_error(self):
        self.movie.add_actor("test_actor")
        self.assertEqual(self.movie.add_actor("test_actor"),
                         "test_actor is already added in the list of actors!")

    def test_rating_better(self):
        test_movie_2 = Movie("test_name_2", 1999, 5.6)
        self.assertEqual(self.movie.__gt__(test_movie_2),
                         '"test_name_2" is better than "test_name"')

    def test_rating_worse(self):
        test_movie_2 = Movie("test_name_2", 1999, 5.4)
        self.assertEqual(self.movie.__gt__(test_movie_2),
                         '"test_name" is better than "test_name_2"')

    def test_repr(self):
        self.movie.actors = ["test_actor_1", "test_actor_2"]

        self.assertEqual(self.movie.__repr__(),
                         "Name: test_name\n"
                         "Year of Release: 2000\n"
                         "Rating: 5.50\n"
                         "Cast: test_actor_1, test_actor_2"
                         )
