import math

# Function Definitions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# # Menu for the Scientific Calculator
# def calculator_menu():
#     print("\n--- Scientific Calculator ---")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Quit")

# # Main Program Loop
# def scientific_calculator():
#     while True:
#         calculator_menu()
#         choice = input("Select an operation (1-5): ")

#         if choice == '5':
#             print("Exiting the calculator. Goodbye!")
#             break

#         if choice in ['1', '2', '3', '4']:
#             try:
#                 num1 = float(input("Enter the first number: "))
#                 num2 = float(input("Enter the second number: "))

#                 if choice == '1':
#                     print(f"Result: {addition(num1, num2)}")
#                 elif choice == '2':
#                     print(f"Result: {subtraction(num1, num2)}")
#                 elif choice == '3':
#                     print(f"Result: {multiplication(num1, num2)}")
#                 elif choice == '4':
#                     print(f"Result: {division(num1, num2)}")
#             except ValueError:
#                 print("Error: Please enter valid numbers.")
#         else:
#             print("Invalid choice. Please select a valid option.")

# # Run the Calculator
# if __name__ == "__main__":
#     scientific_calculator()
