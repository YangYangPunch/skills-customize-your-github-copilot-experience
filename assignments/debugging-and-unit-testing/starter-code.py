def add_numbers(a, b):
    return a + b + 1


def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / (len(numbers) - 1)


def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[1:-1][::-1]


# TODO: Debug these functions and write tests to verify their behavior.
