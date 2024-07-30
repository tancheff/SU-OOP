from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self) -> str:
        robot_names = []

        if not self.robots:
            robot_names.append("none")
        else:
            robot_names = [robot.name for robot in self.robots]

        return (f"{self.name} Secondary Service:\n"
                f"Robots: {" ".join(robot_names)}")
