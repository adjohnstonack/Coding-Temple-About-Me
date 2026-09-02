scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

grade_counts = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}
for score in scores:
    if 90 <= score <= 100:
        grade_counts["A"] += 1
    elif 80 <= score <= 89:
        grade_counts["B"] += 1
    elif 70 <= score <= 79:
        grade_counts["C"] += 1
    elif 60 <= score <= 69:
        grade_counts["D"] += 1
    else: 
        grade_counts["F"] += 1

total_scores = len(scores)
average_score = sum(scores) / total_scores
highest_score = max(scores)
lowest_score = min(scores)

passing = sum(1 for s in scores if s >= 60)
failing = sum(1 for s in scores if s < 60)

print("Score Summary")
print("=============")
print(f"Total scores: {total_scores}")
print(f"Average score: {average_score:.1f}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Passing (60+): {passing}")
print(f"Failing (<60): {failing}")
print("\nGrade distribution:")
for grade, count in grade_counts.items():
    print(f"{grade}: {count}")

# Allow user to add more scores
while True:
    user_input = input("\nEnter a new score (or 'done' to finish): ")

    if user_input.lower() == "done":
        break

    try:
        new_score = int(user_input)
        if 0 <= new_score <= 100:
            scores.append(new_score)
            average_score = sum(scores) / len(scores)
            print(f"Updated average score: {average_score:.1f}")
        else:
            print("Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

