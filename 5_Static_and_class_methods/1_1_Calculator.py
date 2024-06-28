from typing import List


class Calculator:

    @staticmethod
    def add(*nums: int):
        return sum(nums)

    @staticmethod
    def subtract(*nums: List[int]):
        result = nums[0]*2
        for a in nums:
            result -= a

        return result

    @staticmethod
    def multiply(*nums: List[int]):
        result = 1
        for a in nums:
            result *= a

        return result

    @staticmethod
    def divide(*nums: List[int]):
        result = nums[0]**2
        for a in nums:
            result /= a

        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
