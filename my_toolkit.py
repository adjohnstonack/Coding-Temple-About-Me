#A small toolkit of utility functions for working with numbers, lists, and text.

#Average calculation
def calculate_average(numbers):
    if not numbers:
        return 0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)   # FIXED: moved outside loop

#Max_min calculation
def find_max_and_min(numbers):
    if not numbers:
        return (None, None)
    max_value = numbers[0]
    min_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
    return (max_value, min_value)   # FIXED: moved outside loop

#Count occurrences calculation
def count_occurrences(items, target):
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count   # FIXED: moved outside loop

#Palindrome calculation
def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char != " ":
            cleaned += char.lower()
    return cleaned == cleaned[::-1]

#Takes a report title and a list of scores
def create_report(title, scores):
    avg = calculate_average(scores)
    max_val, min_val = find_max_and_min(scores)

    report = (
        f"=== {title} ===\n"
        f"Total Scores: {len(scores)}\n"
        f"Average Score: {avg:.2f}\n"
        f"Highest Score: {max_val}\n"
        f"Lowest Score: {min_val}\n"
    )
    return report

#Provided data
if __name__ == "__main__":
    # Required tests
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    print("\n--- EDGE CASE TESTS ---")

    # Empty list tests
    print("Average of empty list:", calculate_average([]))
    print("Max/Min of empty list:", find_max_and_min([]))

    # count_occurrences edge cases
    print("Count occurrences (multiple matches):", count_occurrences([1, 2, 2, 2, 3], 2))
    print("Count occurrences (no matches):", count_occurrences([1, 3, 5], 2))

    # is_palindrome edge cases
    print("Palindrome (spaces):", is_palindrome("A man a plan a canal Panama"))
    print("Palindrome (single letter):", is_palindrome("x"))
    print("Palindrome (mixed case):", is_palindrome("RaceCar"))
    print("Palindrome (empty string):", is_palindrome(""))

    # create_report edge case
    print("\nEmpty score report:")
    print(create_report("Empty Report", []))
