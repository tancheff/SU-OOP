class Phone:
    def __init__(self, color, size):
        self.color = color
        self.size = size


adnroid = Phone("blue", 3.5)
iOS = Phone("black", 5)

print(adnroid.__dict__)
print(iOS.size)

class Person:
    def __init__(self, height, age):
        self.height = height
        self.age = age

Ivan = Person(185, 25)
print(Ivan.__dict__)