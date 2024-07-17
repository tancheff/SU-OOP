from project.band_members.musician import Musician


class Guitarist(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @property
    def available_skills(self):
        return ["play metal",
                "play rock",
                "play jazz"
                ]

    def learn_new_skill(self, new_skill: str) -> str:
        return super().learn_new_skill(new_skill)
