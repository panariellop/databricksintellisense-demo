# Databricks Notebook source

# COMMAND ----------
# This is a dummy databricks notebook to demonstrate classes and functions

# COMMAND ----------
# Define a simple class

class DataProcessor:
    """
    A simple class for processing data.
    """

    def __init__(self, input_data):
        """
        Constructor to initialize the DataProcessor.

        Args:
            input_data (list): The initial data to be processed.
        """
        self.data = input_data
        self.processed_data = []

    def square_numbers(self):
        """
        Squares each number in the input data and stores in the processed data.
        """
        self.processed_data = [x**2 for x in self.data]

    def add_constant(self, constant):
        """
        Adds a constant value to each number in the processed data.

        Args:
            constant (int or float): The constant value to add.
        """
        if not self.processed_data:
            print("Warning: No processed data available, running square numbers function...")
            self.square_numbers()
        self.processed_data = [x + constant for x in self.processed_data]
    def add_2_constants(self, constant, constant2):
        """
        Adds a constant value to each number in the processed data.

        Args:
            constant (int or float): The constant value to add.
        """
        if not self.processed_data:
            print("Warning: No processed data available, running square numbers function...")
            self.square_numbers()
        self.processed_data = [x + constant + constant2 for x in self.processed_data]
    
    def get_processed_data(self):
      """
      Returns processed data.
      """
      return self.processed_data

# COMMAND ----------
# Define a simple function


# COMMAND ----------
# Example Usage

# Create an instance of the DataProcessor class
input_numbers = [1, 2, 3, 4, 5]
processor = DataProcessor(input_numbers)

# Process the data
processor.square_numbers()
processor.add_constant(10)

# Get the processed data
processed_numbers = processor.get_processed_data()

# Print the processed data
print(f"Processed numbers: {processed_numbers}")


# Calculate the average using the function
average_value = calculate_average(processed_numbers)

if average_value is not None:
    print(f"Average of the processed numbers: {average_value}")
else:
    print("Could not calculate average due to empty list.")

# Example with empty list
empty_numbers = []
average_value_empty = calculate_average(empty_numbers)
if average_value_empty is not None:
    print(f"Average of empty list {average_value_empty}")
else:
    print("Could not calculate average due to empty list.")

# Example with only add_constant function
input_numbers_2 = [6,7,8]
processor2 = DataProcessor(input_numbers_2)
processor2.add_constant(2)
processed_numbers_2 = processor2.get_processed_data()
print(f"Processed numbers from processor 2: {processed_numbers_2}")