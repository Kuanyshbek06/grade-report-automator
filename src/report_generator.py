import csv
from pathlib import Path


INPUT_FILE = Path("data/sample_grades.csv")
OUTPUT_FILE = Path("output/grade_report.csv")
PASSING_SCORE = 50


def calculate_result(score: int) -> str:
    """Return Pass when the score is at least 50, otherwise Fail."""
    return "Pass" if score >= PASSING_SCORE else "Fail"


def generate_report(input_path: Path, output_path: Path) -> int:
    """Read student grades and create a processed CSV report."""
    with input_path.open("r", encoding="utf-8", newline="") as input_file:
        students = list(csv.DictReader(input_file))

    for student in students:
        score = int(student["score"])
        student["result"] = calculate_result(score)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["student_id", "name", "subject", "score", "result"]

    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    return len(students)


def main() -> None:
    processed_count = generate_report(INPUT_FILE, OUTPUT_FILE)
    print(f"Report created: {OUTPUT_FILE}")
    print(f"Students processed: {processed_count}")


if __name__ == "__main__":
    main()