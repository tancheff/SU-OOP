# place order
# receive order
# start cooking
# cutting
# boiling


class Cook:
    def slice(self):
        print("slicing")

    def cut(self):
        print("cutting")

    def boil(self):
        print("boiling")


class Waitress:
    def __init__(self, name: str):
        self.name = name

    def gather_reques(self):
        pass

    def place_order(self):
        pass


class Restaurant:
    def __init__(self, name: str, cook: Cook, waitress: Waitress):
        self.name = name
        self.cook = cook
        self.waitress = waitress

    def execute_order(self):
        self.waitress.place_order()
        self.cook.cut()
        self.cook.slice()
        self.cook.boil()


class Client:
    pass


w = Waitress("Test")
c = Cook()
res = Restaurant("KFC", c, w)
res.execute_order()