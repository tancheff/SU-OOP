class ReversedMath:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num - other.num

    def __sub__(self, other):
        return self.num + other.num

    def __str__(self):
        return "I am reversed!"


n1 = ReversedMath(5)
n2 = ReversedMath(6)
print(n1 + n2)
print(n1 - n2)
print(n1)
