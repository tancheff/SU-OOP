# from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int) -> str:
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if not user:
            self.users_collection.append(User(username, age))
            return f"{username} registered successfully."
        else:
            raise Exception("User already exists!")

    def upload_movie(self, username: str, movie) -> str:
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if not user:
            raise Exception("This user does not exist!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie, **kwargs) -> str:
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if movie.owner != user:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for key, value in kwargs.items():
            if key == "title":
                movie.title = kwargs[key]
            elif key == "year":
                movie.year = kwargs[key]
            elif key == "age_restriction":
                movie.age_restriction = kwargs[key]

        return f"{user.username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie) -> str:
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != user:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{user.username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie):
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if movie.owner == user:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{user.username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{user.username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie):
        user = next(filter(lambda u: u.username == username, self.users_collection), None)

        if movie not in user.movies_liked:
            raise Exception(f"{user.username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{user.username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))

        result = []

        for movie in sorted_movies:
            result.append(movie.details())

        return "\n".join(result)

    def __str__(self):
        if not self.movies_collection:
            movies_info = "All movies: No movies."
        else:
            movies_info = f"All movies: {', '.join([m.title for m in self.movies_collection])}"

        if not self.users_collection:
            users_info = "All users: No users."
        else:
            users_info = f"All users: {', '.join([u.username for u in self.users_collection])}"

        return (f"{users_info}\n"
                f"{movies_info}")
