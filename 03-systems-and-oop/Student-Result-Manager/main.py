"""
Student Result Manager
An Object-Oriented student grading and performance tracking system with JSON persistence.
"""
import json
from pathlib import Path
from typing import Dict, List, Optional

DATA_FILE = Path(__file__).parent / "data" / "students.json"


class Student:
    """Represents an individual student and their academic performance."""
    def __init__(self, name: str, roll_number: str, marks: Dict[str, float]):
        self.name = name.strip()
        self.roll_number = roll_number.strip().upper()
        self.marks = marks  # subject -> score

    @property
    def total_marks(self) -> float:
        return sum(self.marks.values())

    @property
    def percentage(self) -> float:
        if not self.marks:
            return 0.0
        return self.total_marks / len(self.marks)

    @property
    def grade(self) -> str:
        pct = self.percentage
        if pct >= 90:
            return "A+ (Outstanding)"
        elif pct >= 80:
            return "A (Excellent)"
        elif pct >= 70:
            return "B (Very Good)"
        elif pct >= 60:
            return "C (Good)"
        elif pct >= 50:
            return "D (Pass)"
        else:
            return "F (Fail)"

    @property
    def is_passed(self) -> bool:
        if not self.marks:
            return False
        return self.percentage >= 40.0 and all(score >= 35.0 for score in self.marks.values())

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            name=data["name"],
            roll_number=data["roll_number"],
            marks=data.get("marks", {})
        )


class StudentResultManager:
    """Manages student records, results calculation, and file persistence."""
    def __init__(self, storage_path: Path = DATA_FILE):
        self.storage_path = storage_path
        self.students: Dict[str, Student] = {}
        self.load_data()

    def load_data(self):
        if not self.storage_path.exists():
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            self.students = {}
            return

        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.students = {item["roll_number"]: Student.from_dict(item) for item in data}
        except Exception as e:
            print(f"[!] Warning: Could not load existing data ({e}). Starting with empty store.")
            self.students = {}

    def save_data(self):
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, "w", encoding="utf-8") as f:
            records = [student.to_dict() for student in self.students.values()]
            json.dump(records, f, indent=4)

    def add_student(self, name: str, roll_number: str, marks: Dict[str, float]) -> bool:
        roll = roll_number.strip().upper()
        if roll in self.students:
            return False
        self.students[roll] = Student(name, roll, marks)
        self.save_data()
        return True

    def get_student(self, roll_number: str) -> Optional[Student]:
        return self.students.get(roll_number.strip().upper())

    def remove_student(self, roll_number: str) -> bool:
        roll = roll_number.strip().upper()
        if roll in self.students:
            del self.students[roll]
            self.save_data()
            return True
        return False

    def get_all_students(self) -> List[Student]:
        return sorted(self.students.values(), key=lambda s: s.roll_number)

    def get_class_statistics(self) -> dict:
        total = len(self.students)
        if total == 0:
            return {"total": 0}

        percentages = [s.percentage for s in self.students.values()]
        passed = sum(1 for s in self.students.values() if s.is_passed)
        failed = total - passed

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": (passed / total) * 100,
            "class_average": sum(percentages) / total,
            "highest_score": max(percentages),
            "lowest_score": min(percentages),
        }


def print_student_card(student: Student):
    print("\n" + "=" * 45)
    print(f"  Student Report Card: {student.name}")
    print("=" * 45)
    print(f"  Roll Number : {student.roll_number}")
    print(f"  Status      : {'PASS' if student.is_passed else 'FAIL'}")
    print(f"  Grade       : {student.grade}")
    print(f"  Percentage  : {student.percentage:.2f}%")
    print("  Subject Scores:")
    for subj, score in student.marks.items():
        print(f"    - {subj:<15}: {score:.1f}")
    print("=" * 45)


def main():
    manager = StudentResultManager()

    while True:
        print("\n" + "=" * 45)
        print("     🎓 STUDENT RESULT MANAGER (OOP)")
        print("=" * 45)
        print("1. Add New Student Record")
        print("2. View All Students")
        print("3. Search Student Report Card")
        print("4. Remove Student Record")
        print("5. View Class Statistics")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            roll = input("Enter roll number (e.g. R01): ").strip()
            if not name or not roll:
                print("Error: Name and Roll Number are required.")
                continue

            marks = {}
            print("Enter subject marks (0-100). Type 'done' when finished:")
            while True:
                subj = input("  Subject name: ").strip()
                if subj.lower() in ("done", ""):
                    if marks:
                        break
                    print("  Please enter at least one subject.")
                    continue
                try:
                    score = float(input(f"  Marks for {subj}: ").strip())
                    if not (0 <= score <= 100):
                        print("  Score must be between 0 and 100.")
                        continue
                    marks[subj] = score
                except ValueError:
                    print("  Invalid score. Please enter a valid number.")

            success = manager.add_student(name, roll, marks)
            if success:
                print(f"✅ Student '{name}' ({roll}) recorded successfully!")
            else:
                print(f"[!] Error: Student with Roll Number '{roll}' already exists.")

        elif choice == "2":
            students = manager.get_all_students()
            if not students:
                print("\n[i] No student records available.")
            else:
                print("\n" + "-" * 65)
                print(f"{'Roll':<8} | {'Name':<20} | {'Percentage':<10} | {'Status':<6} | {'Grade'}")
                print("-" * 65)
                for s in students:
                    status = "PASS" if s.is_passed else "FAIL"
                    print(f"{s.roll_number:<8} | {s.name:<20} | {s.percentage:>8.2f}% | {status:<6} | {s.grade}")
                print("-" * 65)

        elif choice == "3":
            roll = input("Enter student roll number: ").strip()
            student = manager.get_student(roll)
            if student:
                print_student_card(student)
            else:
                print(f"No student record found for roll number '{roll}'.")

        elif choice == "4":
            roll = input("Enter roll number to delete: ").strip()
            if manager.remove_student(roll):
                print(f"✅ Record for roll number '{roll}' deleted.")
            else:
                print(f"No student found with roll number '{roll}'.")

        elif choice == "5":
            stats = manager.get_class_statistics()
            if stats["total"] == 0:
                print("\n[i] No student data to compute statistics.")
            else:
                print("\n" + "=" * 40)
                print("         Class Performance Overview")
                print("=" * 40)
                print(f"  Total Enrolled   : {stats['total']}")
                print(f"  Passed Students  : {stats['passed']}")
                print(f"  Failed Students  : {stats['failed']}")
                print(f"  Pass Rate        : {stats['pass_rate']:.1f}%")
                print(f"  Class Average    : {stats['class_average']:.2f}%")
                print(f"  Highest Score    : {stats['highest_score']:.2f}%")
                print(f"  Lowest Score     : {stats['lowest_score']:.2f}%")
                print("=" * 40)

        elif choice == "6":
            print("Exiting Student Result Manager. Goodbye!")
            break
        else:
            print("Invalid selection. Choose between 1 and 6.")


if __name__ == "__main__":
    main()
