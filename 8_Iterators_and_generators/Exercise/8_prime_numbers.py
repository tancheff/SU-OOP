from math import sqrt


def get_primes(numbers: list):
    for number in numbers:
        if number <= 1:
            continue

        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                break

        else:
            yield number


# from typing import List
#
#
# class get_primes:
#     DIVISION_NUMBERS = [2, 3, 5, 7]
#
#     def __init__(self, num: List[int]):
#         self.num = num
#         self.idx = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while True:
#             is_prime = True
#
#             self.idx += 1
#             if self.idx >= len(self.num):
#                 raise StopIteration
#
#             current_num = self.num[self.idx]
#             if current_num < 2:
#                 continue
#
#             if current_num in get_primes.DIVISION_NUMBERS:
#                 return current_num
#
#             for n in get_primes.DIVISION_NUMBERS:
#                 if current_num % n == 0:
#                     is_prime = False
#
#             if not isinstance(current_num, int):
#                 is_prime = False
#
#             if is_prime:
#                 return current_num


print(list(get_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 13, 15, 20, 21, 22])))
print("=========================================")
print(list(get_primes([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71])))
print("=========================================")
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print("=========================================")
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
print("=========================================")
print(list(get_primes([])))
