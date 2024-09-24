from abc import ABC, abstractmethod

# from project.user import User


class Movie(ABC):
    def __init__(self, title: str, year: int, owner, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes: int = 0
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value: str):
        if value.strip() == "":
            raise ValueError("The title cannot be empty string!")

        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, user):
        if user.__class__.__name__ != "User":
            raise ValueError("The owner must be an object of type User!")

        # user.movies_owned.append(self)
        self.__owner = user

    @abstractmethod
    def details(self):
        pass
