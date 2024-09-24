from project.band_members.musician import Musician


class Singer(Musician):
    # MUSICIAN_SKILLS = ["sing high pitch notes", "sing low pitch notes"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @property
    def available_skills(self):
        return ["sing high pitch notes",
                "sing low pitch notes"
                ]

    def learn_new_skill(self, new_skill: str) -> str:
        return super().learn_new_skill(new_skill)


# s = Singer("test_name", 16)
#
# print(s.name)
# print(s.age)
# print(s.skills)
# s.learn_new_skill("sing high pitch notes")
# print(s.skills)
#
# print(s.__class__.__name__ == "Singer")
#
# if __name__ == "__main__":
#     main()