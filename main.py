# Databricks Notebook source
# MAGIC %run ./data_processor
# MAGIC %run ./other_folder/string_analyzer
# MAGIC %run ./average
# MAGIC %run /another_folder/printer

# COMMAND ----------
# This is a second databricks notebook which reuses the classes and functions from the first notebook

# COMMAND ----------
# Example Usage: Reusing DataProcessor Class

# Create an instance of the DataProcessor class
dp = DataProcessor([1, 2, 3])
new_input_numbers = [10, 20, 30, 40]
new_processor = DataProcessor(new_input_numbers)

new_processor_2 = DataProcessor(new_input_numbers)

new_processor_2.

s = StringAnalyzer("hello world")
s.get_unique_words()


lp = ListProcessor(numbers)
lp.sum_of_list()

s.get_word_count(self)
# Process the data
new_processor.square_numbers()
new_processor.add_constant(5)

# Get the processed data
new_processed_numbers = new_processor.get_processed_data()

# Print the new processed data
print(f"New processed numbers: {new_processed_numbers}")

# COMMAND ----------
# Example Usage: Reusing calculate_average function

# Calculate average of new data
new_average = calculate_average(new_processed_numbers)

if new_average is not None:
  print(f"The average of the new processed data: {new_average}")
else:
  print("Could not calculate average as input list was empty")


# COMMAND ----------
# Example with more complex data

# Create a new instance with more complex input
complex_input = [1.5, 2.5, 3.5, 4.5, 5.5]
complex_processor = DataProcessor(complex_input)
complex_processor.

# Process the complex data
complex_processor.square_numbers()
complex_processor.add_constant(-2)
complex_processed_data = complex_processor.get_processed_data()

# Print results
print(f"Complex processed data: {complex_processed_data}")

# Calculate and print average
complex_average = calculate_average(complex_processed_data)

if complex_average is not None:
    print(f"Average of complex processed data: {complex_average}")
else:
    print("Could not calculate average as input list was empty")


# COMMAND ----------
# Example with different constant value

#Create an instance
diff_const_processor = DataProcessor(new_input_numbers)

#Process the data
diff_const_processor.add_constant(-10)

#Get the data
diff_const_numbers = diff_const_processor.get_processed_data()

#Print the data
print(f"Processed numbers with add constant function: {diff_const_numbers}")

#Calculate average
diff_const_average = calculate_average(diff_const_numbers)
if diff_const_average is not None:
    print(f"The average of the processed numbers: {diff_const_average}")
else:
    print("Could not calculate average as input list was empty")