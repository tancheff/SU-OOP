def vowel_filter(function):
    VOWELS = ["a", "o", "e", "i", "u"]

    def wrapper():
        result = [letter.lower() for letter in function() if letter in VOWELS]

        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
