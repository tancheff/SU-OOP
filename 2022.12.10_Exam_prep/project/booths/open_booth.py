from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)
        # self.delicacy_orders: List[Delicacy] = []
        # self.price_for_reservation: float = 0
        # self.is_reserved: bool = False

    def reserve(self, number_of_people: int) -> None:
        self.price_for_reservation = number_of_people * self.PRICE_PER_PERSON
        self.is_reserved = True
