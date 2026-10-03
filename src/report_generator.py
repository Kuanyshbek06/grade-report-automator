import argparse
import csv
from pathlib import Path


INPUT_FILE = Path("data/sample_grades.csv")
OUTPUT_FILE = Path("output/grade_report.csv")
PASSING_SCORE = 50
REQUIRED_COLUMNS = {"student_id", "name", "subject", "score"}


def calculate_result(score: int) -> str:
    """Return Pass when the score is at least 50, otherwise Fail."""
    return "Pass" if score >= PASSING_SCORE else "Fail"


def parse_score(value: str | None) -> int:
    """Convert a score to an integer and validate its range."""
    try:
        score = int(value)
    except (TypeError, ValueError):
        raise ValueError("Score must be an integer") from None

    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")

    return score


def generate_report(input_path: Path, output_path: Path) -> int:
    """Read student grades and create a validated CSV report."""
    with input_path.open("r", encoding="utf-8", newline="") as input_file:
        reader = csv.DictReader(input_file)
        available_columns = set(reader.fieldnames or [])
        missing_columns = REQUIRED_COLUMNS - available_columns

        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(f"Missing required columns: {missing}")

        students = list(reader)

    for student in students:
        try:
            score = parse_score(student.get("score"))
            student["result"] = calculate_result(score)
            student["error"] = ""
        except ValueError as error:
            student["result"] = "Invalid"
            student["error"] = str(error)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "student_id",
        "name",
        "subject",
        "score",
        "result",
        "error",
    ]

    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=fieldnames,
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(students)

    return len(students)


def parse_arguments(
    arguments: list[str] | None = None,
) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Validate student grades and generate a CSV report."
    )

    parser.add_argument(
        "--input",
        type=Path,
        default=INPUT_FILE,
        help=f"Input CSV file (default: {INPUT_FILE})",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_FILE,
        help=f"Output CSV file (default: {OUTPUT_FILE})",
    )

    return parser.parse_args(arguments)


def main() -> None:
    args = parse_arguments()
    processed_count = generate_report(args.input, args.output)

    print(f"Report created: {args.output}")
    print(f"Students processed: {processed_count}")


if __name__ == "__main__":
    main()