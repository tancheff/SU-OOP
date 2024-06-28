class DVD:
    MONTHS = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    def __init__(self,
                 name: str,
                 id_number: int,
                 creation_year: int,
                 creation_month: str,
                 age_restriction: int):
        self.name = name
        self.id = id_number
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, id_number: int, name: str, date: str, age_restriction: int):
        DD, MM, YYYY = date.split(".")
        dvd_year = int(YYYY)
        dvd_month = cls.MONTHS.get(int(MM))

        return cls(name, id_number, dvd_year, dvd_month, age_restriction)

    def __repr__(self) -> str:
        # if self.is_rented:
        #     status = "rented"
        # else:
        #     status = "not rented"
        #
        # return (f"{self.id}: {self.name} ({self.creation_month} "
        #         f"{self.creation_year}) has age restriction "
        #         f"{self.age_restriction}. Status: {status}")
        return (f"{self.id}: {self.name} ({self.creation_month} "
                f"{self.creation_year}) has age restriction "
                f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}")
