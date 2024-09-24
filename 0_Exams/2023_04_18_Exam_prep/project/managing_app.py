from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = next(filter(lambda user: user.driving_license_number == driving_license_number, self.users), None)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        vehicle = next(
            filter(lambda vehicle: vehicle.license_plate_number == license_plate_number, self.vehicles), None)

        if vehicle_type not in self.VALID_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VALID_VEHICLES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        route_0 = next(
            filter(
                lambda route: route.start_point == start_point and
                              route.end_point == end_point and route.length > length, self.routes), None)
        if route_0:
            route_0.is_locked = True

        route_1 = next(
            filter(
                lambda route: route.start_point == start_point and
                              route.end_point == end_point and route.length == length, self.routes), None)
        if route_1:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        route_2 = next(
            filter(
                lambda route: route.start_point == start_point and
                              route.end_point == end_point and route.length < length, self.routes), None)

        if route_2:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        self.routes.append(Route(start_point, end_point, length, route_id))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = next(filter(lambda user: user.driving_license_number == driving_license_number, self.users), None)
        vehicle = next(
            filter(lambda vehicle: vehicle.license_plate_number == license_plate_number, self.vehicles), None)
        route = next(filter(lambda route: route.route_id == route_id, self.routes), None)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted(filter(lambda v: v.is_damaged is True, self.vehicles),
                                  key=lambda v: (v.brand, v.model))

        if count >= len(damaged_vehicles):
            count = len(damaged_vehicles)

            for vehicle in damaged_vehicles:
                vehicle.change_status()
                vehicle.recharge()

        else:
            for i in range(count):
                damaged_vehicles[i].change_status()
                damaged_vehicles[i].recharge()

        return f"{count} vehicles were successfully repaired!"

    def users_report(self):
        self.users.sort(key=lambda user: -user.rating)

        return "*** E-Drive-Rent ***\n" + '\n'.join(user.__str__() for user in self.users)

        # в JUDGE не минава:
        # return (f"*** E-Drive-Rent ***\n"
        #         f"{'\n'.join(user.__str__() for user in self.users)}")

        # в GUDGE мина с 1 грешка:
        # return (
        #         f"*** E-Drive-Rent ***\n"
        #         f"'\n'.join({[user.__str__() for user in self.users]}"
        # )

        # минава през проблем:
        # return "*** E-Drive-Rent ***\n" + '\n'.join(user.__str__() for user in self.users)

