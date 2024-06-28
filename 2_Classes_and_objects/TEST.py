# Creating a nested dictionary
library_records = {
    "alice": {
        "1984": 14,
        "To Kill a Mockingbird": 21
    },
    "bob": {
        "The Great Gatsby": 7,
        "War and Peace": 30
    },
    "charlie": {
        "Moby Dick": 10,
        "Hamlet": 15
    }
}

# Printing the nested dictionary
print(library_records)
library_records.remove("charlie")
print(library_records)

# print(library_records["alice"])
# print(library_records["alice"]["1984"])