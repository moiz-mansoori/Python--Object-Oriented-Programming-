# # Multiplication Table Program
# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} x {i} = {int(a) * i}")
# except:
#     print("An error occurred")

# print("Some important lines of code")
# print("End of program")


# # Handling Multiple Exceptions
# try:
#     num = int(input("Enter a number: "))
#     a = [5, 3]
#     print(a[num])
# except ValueError:
#     print("Invalid input: Please enter a valid number")
# except IndexError:
#     print("Index error: Index is out of range")
# except IndentationError:
#     print("Indentation error: Check the code indentation")


# # User Input Validation with Raise
# a = input("Enter any number between 4 to 9: ")
# if a == "quit":
#     print(a)
# else:
#     a = int(a)
#     if a < 4 or a > 9:
#         raise ValueError("Value should be between 4 and 9")


    # # Custom Exception Example

# class CustomError(Exception):
#     pass

# def example_function(value):
#     if value < 0:
#         raise CustomError("Negative values are not allowed.")

# try:
#     value = int(input("Enter a positive number: "))
#     example_function(value)
# except CustomError as ce:
#     print("Custom Error:", ce)



# Creating a Custom Exception Class
# class MyCustomError(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#         self.error_message = message  # Store the error message

#     def get_error_message(self):
#         return self.error_message


# # Example Usage of MyCustomError
# def example_function(value):
#     if value < 0:
#         raise MyCustomError("Negative values are not allowed.")


# try:
#     value = int(input("Enter a positive number: "))
#     example_function(value)
# except MyCustomError as custom_error:
#     print("Custom Error:", custom_error.get_error_message())
