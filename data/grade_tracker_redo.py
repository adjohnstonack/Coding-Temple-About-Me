import csv

def load_students(filepath):
    """Load student records from a CSV file and return a list of dictionaries."""
    try:
        with open(filepath, newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: Could not find file at {filepath}")
        return []


def calculate_average(grades):
    """Calculate the average of a list of grade strings, skipping empty values."""
    valid = []

    for g in grades:
        if g.strip() != "":
            valid.append(float(g))

    if not valid:
        return None

    avg = sum(valid) / len(valid)
    return round(avg, 1)


def get_letter_grade(average):
    """Convert a numeric average into a letter grade."""
    if average is None:
        return "N/A"
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def generate_report(students):
    """Generate a full class report dictionary."""
    report = {
        "total_students": len(students),
        "class_average": None,
        "highest_average": None,
        "lowest_average": None,
        "grade_distribution": {
            "A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0
        },
        "results": []
    }

    averages = []

    for student in students:
        grades = [
            student["math"],
            student["science"],
            student["english"],
            student["history"]
        ]

        avg = calculate_average(grades)
        letter = get_letter_grade(avg)

        report["results"].append({
            "name": student["student_name"],
            "average": avg,
            "letter": letter
        })

        if avg is not None:
            averages.append(avg)

        report["grade_distribution"][letter] += 1

    if averages:
        report["class_average"] = round(sum(averages) / len(averages), 1)
        report["highest_average"] = max(averages)
        report["lowest_average"] = min(averages)

    return report


def write_report(report, filepath):
    """Write a formatted report to a text file."""
    with open(filepath, "w") as f:
        f.write("GRADE REPORT\n")
        f.write("====================\n\n")

        f.write(f"Total students: {report['total_students']}\n")
        f.write(f"Class average: {report['class_average']}\n")
        f.write(f"Highest average: {report['highest_average']}\n")
        f.write(f"Lowest average: {report['lowest_average']}\n\n")

        f.write("Grade Distribution:\n")
        for grade, count in report["grade_distribution"].items():
            f.write(f"  {grade}: {count}\n")

        f.write("\nIndividual Results:\n")
        for r in report["results"]:
            f.write(f"{r['name']}: {r['average']} ({r['letter']})\n")