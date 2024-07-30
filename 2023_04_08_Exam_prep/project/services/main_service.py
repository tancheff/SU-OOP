from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)
        # self.robots: List[BaseRobot] = []

    def details(self) -> str:
        robot_names = []

        if not self.robots:
            robot_names.append("none")
        else:
            robot_names = [robot.name for robot in self.robots]

        return (f"{self.name} Main Service:\n"
                f"Robots: {" ".join(robot_names)}")
