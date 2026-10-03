import csv
from pathlib import Path


INPUT_FILE = Path("data/sample_grades.csv")
OUTPUT_FILE = Path("output/grade_report.csv")
PASSING_SCORE = 50


with INPUT_FILE.open("r", encoding="utf-8", newline="") as input_file:
    students = list(csv.DictReader(input_file))

for student in students:
    score = int(student["score"])
    student["result"] = "Pass" if score >= PASSING_SCORE else "Fail"

fieldnames = ["student_id", "name", "subject", "score", "result"]

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print(f"Report created: {OUTPUT_FILE}")