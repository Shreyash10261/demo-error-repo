def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    """
    # Intentional bug: if the list is empty, len(numbers) is 0, causing a ZeroDivisionError
    total = sum(numbers)
    count = len(numbers)
    return total / count

def fetch_user_data(users, user_id):
    """
    Fetches a user from a dictionary by ID.
    """
    # Intentional bug: does not use .get(), will throw KeyError if user_id doesn't exist
    return users[user_id]

def string_to_int(string_val):
    """
    Converts a string to an integer.
    """
    # Intentional bug: Will throw ValueError if string_val is not numeric
    return int(string_val)
