from project.trip import Trip
from unittest import TestCase


class TripTest(TestCase):
    def setUp(self):
        self.trip = Trip(5_000, 5, True)

    def test_initialisation(self):
        self.assertEqual(self.trip.budget, 5_000)
        self.assertEqual(self.trip.travelers, 5)
        self.assertEqual(self.trip.is_family, True)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})

    def test_travelers_setter_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual("At least one traveler is required!", str(ve.exception))

    def test_travelers_setter_success(self):
        self.trip.travelers = 8
        self.assertEqual(self.trip.travelers, 8)

    def test_family_setter_true(self):
        self.trip.is_family = True
        self.assertEqual(self.trip.is_family, True)
        self.assertEqual(self.trip.travelers, 5)

    def test_family_setter_true_but_not_enough_people(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertEqual(self.trip.travelers, 1)
        self.assertEqual(self.trip.is_family, False)

    def test_family_setter_false_enough_people(self):
        self.trip.travelers = 4
        self.trip.is_family = False
        self.assertEqual(self.trip.travelers, 4)
        self.assertEqual(self.trip.is_family, False)

    def test_book_a_trip_not_in_destinations(self):
        self.assertEqual(self.trip.book_a_trip("Sofia"),
                         'This destination is not in our offers, please choose a new one!')

    def test_book_a_destination_not_enough_money(self):
        self.assertEqual(self.trip.book_a_trip("Brazil"),
                         'Your budget is not enough!')

    def test_book_a_destination_successful(self):
        self.assertEqual(self.trip.book_a_trip("Bulgaria"),
                         "Successfully booked destination Bulgaria! Your budget left is 2750.00")
        self.assertEqual(self.trip.budget, 2750)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {"Bulgaria": 2250})

    def test_booking_status_no_bookings(self):
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})
        self.assertEqual(self.trip.booking_status(),
                         "No bookings yet. Budget: 5000.00")

    def test_booking_status_info(self):
        self.trip.budget = 200_000
        self.trip.travelers = 10
        self.trip.is_family = False
        self.trip.book_a_trip("Australia")  # 5_700
        self.trip.book_a_trip("Brazil")     # 6_200

        self.assertEqual(self.trip.budget, 81_000)
        self.assertEqual(self.trip.booked_destinations_paid_amounts,
                         {"Australia": 57_000, "Brazil": 62_000})

        self.assertEqual(self.trip.booking_status(),
                         "Booked Destination: Australia\n"
                         "Paid Amount: 57000.00\n"
                         "Booked Destination: Brazil\n"
                         "Paid Amount: 62000.00\n"
                         "Number of Travelers: 10\n"
                         "Budget Left: 81000.00")
