from abc import ABC, abstractmethod


class Rule(ABC):
    @abstractmethod
    def execute(self, file):
        pass


REQUIRED_HEADERS = set(["name", "age", "address", "job"])


class HeaderRule(Rule):
    def execute(self, file_obj):
        if REQUIRED_HEADERS.issubset(file_obj.headers):
            return True

        return False


class NameRule(Rule):
    def execute(self, file_obj):
        all_names = file_obj["name"].all()
        for name in all_names:
            try:
                first, last = name.split()
                return True
            except:
                return False


class AgeRule(Rule):
    def execute(self, file_obj):
        all_ages = file_obj["age"].all()
        for age in all_ages:
            if age < 10:
                return False


RULES = [HeaderRule, NameRule]


class FileReceiver:
    def __init__(self):
        self.file = None

    def upload(self, file):
        self.file = file

    def process(self, rules):
        for rule in rules:
            rule.execute()

    def display_result(self):
        pass


class File:
    pass


fr = FileReceiver
file = File()
fr.upload(file)
fr.process_file(rule=RULES)

"""
Идеята на класа е да комбинира RULES за да хване някакъв pattern (като фасада), да се разбере къде има 
грешки и да се запишат.
в зависимост от това дали има или няма грешки файла да се запише в базата.
Има n обекти/правила служещи за различни цели за верификация на данните от файла.

Абстрактен клас, който насилва с полиморфизъм execute-a;
Конкретна имплементация
Обект, който има n на брой такива (т.е. execute-a?)
Метод, който да извика итеративно  всеки един от тези Rules и да ги execute-не.
"""
