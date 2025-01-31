# Databricks Notebook source

# COMMAND ----------
# This is a third dummy databricks notebook with several classes and functions

# COMMAND ----------
# Utility Functions

def greet(name, greeting="Hello"):
    """
    Generates a personalized greeting.

    Args:
      name (str): The name of the person to greet.
      greeting (str, optional): The greeting message. Defaults to "Hello".

    Returns:
        str: A greeting string.
    """
    return f"{greeting}, {name}!"


def is_even(number):
    """
    Checks if a number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0


def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n, or 1 if n is 0
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
      return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# COMMAND ----------
# Data Processing Classes

class StringAnalyzer:
    """
    A class to analyze strings.
    """

    def __init__(self, text):
        """
        Initializes the StringAnalyzer.

        Args:
          text (str): The text to analyze.
        """
        self.text = text

    def get_word_count(self):
        """
        Counts the number of words in the text.

        Returns:
            int: The number of words.
        """
        words = self.text.split()
        return len(words)

    def get_unique_words(self):
       """
        Returns a set of unique words in the text.

        Returns:
            set: A set of unique words
        """
       words = self.text.lower().split()
       return set(words)

    def reverse_string(self):
        """
        Reverses the string.

        Returns:
            str: The reversed string
        """
        return self.text[::-1]


class ListProcessor:
  """
  A class to process lists of numbers.
  """
  def __init__(self,numbers):
      """
      Initializes the ListProcessor.

      Args:
          numbers (list): The list of numbers to process.
      """
      self.numbers = numbers
  
  def sum_of_list(self):
      """
      Calculates the sum of numbers in the list.

      Returns:
          int: the sum of the list.
      """
      if not self.numbers:
         print("Warning: list is empty")
         return 0
      return sum(self.numbers)

  def filter_even(self):
    """
    Returns a new list with only even numbers

    Returns:
        list: List with only even numbers from the input
    """
    return [number for number in self.numbers if is_even(number)]

  def multiply_list(self, multiplier):
    """
    Multiply all elements in a list with a number

    Args:
        multiplier (int/float): The number to multiply with.

    Returns:
        list: new list with values multiplied by the multiplier.
    """
    return [number * multiplier for number in self.numbers]

# COMMAND ----------
# Example Usage

# Demonstrate utility functions
print(greet("Alice"))
print(greet("Bob", "Good morning"))
print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")

try:
  print(f"Factorial of 5: {factorial(5)}")
  print(f"Factorial of 0: {factorial(0)}")
  print(f"Factorial of -1: {factorial(-1)}")
except ValueError as e:
  print(f"Error {e}")



# Demonstrate StringAnalyzer
text_analyzer = StringAnalyzer("This is a sample text to test the analyzer class")
print(f"Word count: {text_analyzer.get_word_count()}")
print(f"Unique words: {text_analyzer.get_unique_words()}")
print(f"Reversed text: {text_analyzer.reverse_string()}")

# Demonstrate ListProcessor
numbers_processor = ListProcessor([1, 2, 3, 4, 5, 6])
print(f"Sum of numbers: {numbers_processor.sum_of_list()}")
print(f"Even numbers in the list: {numbers_processor.filter_even()}")
print(f"List multiplied by 2: {numbers_processor.multiply_list(2)}")

numbers_processor_2 = ListProcessor([])
print(f"Sum of numbers in an empty list: {numbers_processor_2.sum_of_list()}")