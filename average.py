def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers or None if empty list.
    """
    if not numbers:
      print("Warning: Input list is empty")
      return None
    return sum(numbers) / len(numbers)