# ---data model -----

students = {}


def add_student(name, scores):
    """Add a student and their score to the students dictionary."""
    students[name] = scores


def get_all_students():
    """Return the dictionary of all students and their scores."""
    return students


def calculate_average(scores):
    average_score = sum(scores) / len(scores)
    print(average_score)
    return average_score


def grade_letter(average):
    """Return a grade letter based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# ------Reporting ------

def display_report():
    """Display a formatted report of all students, averages, and grades."""
    all_students = get_all_students()

    if not all_students:
        print("\nNo students have been added yet.")
        return

    print("\n=== Student Report ===")
    print(f"{'Name':<20} {'Average':<10} {'Grade':<6}")
    print("-" * 40)

    for name, scores in all_students.items():
        avg = calculate_average(scores)
        grade = grade_letter(avg)
        print(f"{name:<20} {avg:<10.2f} {grade:<6}")

    print("-" * 40)
    print("End of Report.\n")

# ------CLI Main -----


def main():
    while True:
        print("\n=== Student Grader Tracker ===")
        print("1. Add Student")
        print("2. View Report")
        print("3. Exit")

        choice = input("Select an option: ").strip()
        if choice == "1":
            name = input("Enter student name: ").strip()
            scores = []
            while True:
                score_input = input("Enter score (or 'done' to finish): ").strip()
                if score_input.lower() == "done":
                    break
                try:
                    score = float(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid score. Please enter a number.")
            add_student(name, scores)
            print(f"Student {name} added with {len(scores)} scores.")
            print("Current students:", list(students.keys()))

        elif choice == "2":
            display_report()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
