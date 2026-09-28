import csv

def load_students(filepath):
    students = []
    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print(f"Error: Could not find file at {filepath}")
        return []
    return students

def calculate_average(grades):
    valid_grades = []
    for g in grades:
        if g.strip() !="":
            try:
                valid_grades.append(float(g))
            except ValueError:
                continue
            if not valid_grades:
                return None

            avg = sum(valid_grades) / len(valid_grades)
            return round(avg, 1)
        
def get_letter_grade(average):
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def generate_report(students):
    report = {
        "total_students": len(students),
        "class_average": None,
        "highest_average": None,
        "lowest_average": None,
        "grade_distribution":{
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "F": 0,
            "N/A": 0
        },
        "students": []
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

        report["students"].append({
            "name" : student["student_name"],
            "average": avg,
            "grade" :letter
        })

        if avg is not None:
            averages.append(avg)

            report["grade_distribution"][letter] += 1

    if averages:
        report["class_average"] = round(sum(averages)/len(averages), 1),
        report["highest_average"] = max(averages),
        report["lowest_average"] = min(averages)

    return report
    
    
def write_report(report, filepath):
        with open(filepath, "w") as f:
            f.write("STUDENT GRADE REPORT\n")
            f.write("====================\n\n")

            f.write(f"Total Students: {report['total_students']}\n")
            f.write(f"Class Average: {report['class_average']}\n")
            f.write(f"Highest Average: {report['highest_average']}\n")
            f.write(f"Lowest Average: {report['lowest_average']}\n\n")

            f.write("Grade Distribution:\n")
            for grade, count in report["grade_distribution"].items():
             f.write(f"  {grade}: {count}\n")

            f.write("\nIndividual Student Results:\n")
            f.write("---------------------------\n")

            for student in report["students"]:
             f.write(f"{student['name']}: {student['average']} ({student['grade']})\n")
    


# ============================================================
# MAIN — do not modify
# ============================================================

def main():
    print("Loading student data...")
    students = load_students("students.csv")
    print(f"Loaded {len(students)} students.")

    print("Generating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")

    print("\nGrade Distribution:")
    for grade, count in sorted(report["grade_distribution"].items()):
        print(f"  {grade}: {count}")

    print("\nTop 5 students:")
    sorted_students = sorted(
        [s for s in report["students"] if s["average"] is not None],
        key=lambda s: s["average"],
        reverse=True
    )
    for s in sorted_students[:5]:
        print(f"  {s['name']:<20} {s['average']:.1f}  ({s['grade']})")

    write_report(report, "grade_report.txt")
    print("\nReport written to grade_report.txt")


if __name__ == "__main__":
    main()
