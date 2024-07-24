def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            raise TypeError("Input must be a number.")

try:
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    print(f"The numbers you entered are {num1} and {num2}.")
except TypeError as e:
    print(e)