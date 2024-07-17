from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int) -> str or None:
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        musician = next(filter(lambda m: m.name == name, self.musicians), None)
        if musician:
            raise Exception(f"{musician.name} is already a musician!")

        self.musicians.append(self.VALID_MUSICIANS[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = next(filter(lambda b: b.name == name, self.bands), None)
        if band in self.bands:
            raise Exception(f"{band.name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = next(filter(lambda c: c.place == place, self.concerts), None)

        if concert:
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next(filter(lambda m: m.name == musician_name, self.musicians), None)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = next(filter(lambda b: b.name == band_name, self.bands), None)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician.name} was added to {band.name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands), None)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next(filter(lambda m: m.name == musician_name, band.members), None)

        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician.name} was removed from {band.name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands), None)
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        if self.check_band_members(band):
            return self.check_band_members(band)

        if self.check_band_skills(band, concert):
            return self.check_band_skills(band, concert)

        return self.calculate_profit(concert, band)


    def check_band_members(self, band: Band):
        isSinger = False
        isDrummer = False
        isGuitarist = False

        for member in band.members:
            if member.__class__.__name__ == "Singer":
                isSinger = True
            if member.__class__.__name__ == "Drummer":
                isDrummer = True
            if member.__class__.__name__ == "Guitarist":
                isGuitarist = True

        if not isSinger or not isDrummer or not isGuitarist:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

    def check_band_skills(self, band: Band, concert: Concert):
        # this method is called after band has been checked for presence
        #  of at least 1 drummer, guitarist & singer

        genre = concert.genre

        drummer_skill = {"Rock": ["play the drums with drumsticks"],
                         "Metal": ["play the drums with drumsticks"],
                         "Jazz": ["play the drums with drum brushes"]
                         }

        singer_skill = {"Rock": ["sing high pitch notes"],
                        "Metal": ["sing low pitch notes"],
                        "Jazz": ["sing high pitch notes", "sing low pitch notes"]
                        }

        guitar_skill = {"Rock": ["play rock"],
                        "Metal": ["play metal"],
                        "Jazz": ["play jazz"]
                        }

        correct_skills = True

        for member in band.members:
            if member.__class__.__name__ == "Drummer":
                if not set(drummer_skill[genre]).issubset(set(member.skills)):
                    correct_skills = False
            elif member.__class__.__name__ == "Singer":
                # print(member.__class__.__name__)
                # print(set(member.skills))
                # print(set(singer_skill[genre]))

                # тук трябва да е c .issubset() защото има list()
                if not set(singer_skill[genre]).issubset(set(member.skills)):
                    correct_skills = False
            else:
                if not set(guitar_skill[genre]).issubset(set(member.skills)):
                    correct_skills = False

        if not correct_skills:
            raise Exception(f"The {band.name} band is not ready to play at the concert!")


    def calculate_profit(self, concert: Concert, band: Band):
        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."











