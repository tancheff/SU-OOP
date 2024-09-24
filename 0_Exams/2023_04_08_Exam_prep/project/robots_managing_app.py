from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    ROBOT_TYPES = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        # self.robots: List[BaseRobot] = []
        # self.services: List[BaseService] = []
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")

        self.services.append(self.SERVICE_TYPES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        self.robots.append(self.ROBOT_TYPES[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = next(filter(lambda robot: robot.name == robot_name, self.robots), None)
        service = next(filter(lambda service: service.name == service_name, self.services), None)

        # if ((robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService")
        #         or (robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "PrimaryService")):
        #     return "Unsuitable service."

        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return "Unsuitable service."
        if isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot.name} to {service.name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        # robot: BaseRobot = next(filter(lambda robot: robot.name == robot_name, self.robots), None)
        service = next(filter(lambda service: service.name == service_name, self.services), None)

        robot = next(filter(lambda robot: robot.name == robot_name, service.robots), None)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot.name} from {service.name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = next(filter(lambda service: service.name == service_name, self.services), None)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str) -> str:
        service = next(filter(lambda service: service.name == service_name, self.services), None)

        total_price = sum([robot.price for robot in service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join([service.details() for service in self.services])
