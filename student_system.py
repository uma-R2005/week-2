import logging

logging.basicConfig(
    filename='student_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


students = {
    "101": {"name": "Alice", "attendance": 0, "grade": None},
    "102": {"name": "Bob", "attendance": 0, "grade": None},
    "103": {"name": "Charlie", "attendance": 0, "grade": None}
}


def manage_student():
    try:
        student_id = input("Enter student ID: ").strip()
        if student_id not in students:
            raise KeyError("Student ID not found.")

        student = students[student_id]
        print(f"\nWelcome {student['name']}")

        print("\n1. Mark Attendance")
        print("2. Update Grade")
        choice = input("Choose an option: ")

        if choice == '1':
            student["attendance"] += 1
            logging.info(f"Attendance marked for {student['name']} (ID: {student_id})")
            print("✅ Attendance marked.")

        elif choice == '2':
            grade = input("Enter grade (A/B/C/D/F): ").strip().upper()
            if grade not in ['A', 'B', 'C', 'D', 'F']:
                raise ValueError("Invalid grade format.")
            student["grade"] = grade
            logging.info(f"Grade updated for {student['name']} (ID: {student_id}) to {grade}")
            print("✅ Grade updated.")

        else:
            print("Invalid choice.")
            logging.warning(f"Invalid menu choice by user for student ID {student_id}")

    except KeyError as ke:
        print("❌ Error:", ke)
        logging.error(f"Invalid student ID attempt: {ke}")

    except ValueError as ve:
        print("❌ Error:", ve)
        logging.error(f"Grade entry error: {ve}")

    finally:
        logging.info("Student management operation completed.\n")

if __name__ == "__main__":
    manage_student()
