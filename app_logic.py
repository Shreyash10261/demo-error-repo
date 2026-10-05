def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    """
    if not numbers:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    return total / count

def fetch_user_data(users, user_id):
    """
    Fetches a user from a dictionary by ID.
    """
    return users.get(user_id)

def string_to_int(string_val):
    """
    Converts a string to an integer.
    """
    try:
        return int(string_val)
    except ValueError:
        return 0
