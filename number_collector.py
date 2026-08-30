# number_collector.py

def get_number(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("That's not a valid number. Using 0 instead.")
        return 0

# Collect three numbers
num1 = get_number("Enter number 1: ")
num2 = get_number("Enter number 2: ")
num3 = get_number("Enter number 3: ")

# Compute results
numbers = [num1, num2, num3]
total = sum(numbers)
average = total / 3

# Output results
print(f"\nYour numbers: {num1}, {num2}, {num3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")