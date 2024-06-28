numbers = [1, 2, 3, 4, 5, 6]

# Using filter to create an iterator
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Iterate through the filter object
print(even_numbers)
