class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if value.strip() == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        if len(self.movies_liked) > 0:
            liked_movies = []
            for movie in self.movies_liked:
                liked_movies.append(movie.details())
        else:
            liked_movies = "No movies liked."

        if len(self.movies_owned) > 0:
            owned_movies = []
            for movie in self.movies_owned:
                owned_movies.append(movie.details())
        else:
            owned_movies = "No movies owned."

        result = (f"Username: {self.username}, Age: {self.age}\n"
                  f"Liked movies:\n"
                  f"{'\n'.join(liked_movies)}\n"
                  f"Owned movies:\n"
                  f"{'\n'.join(owned_movies)}")

        return result
