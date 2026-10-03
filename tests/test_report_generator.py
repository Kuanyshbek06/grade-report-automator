import csv

from src.report_generator import calculate_result, generate_report


def test_calculate_result() -> None:
    assert calculate_result(100) == "Pass"
    assert calculate_result(50) == "Pass"
    assert calculate_result(49) == "Fail"
    assert calculate_result(0) == "Fail"


def test_generate_report(tmp_path) -> None:
    input_file = tmp_path / "grades.csv"
    output_file = tmp_path / "report.csv"

    input_file.write_text(
        "student_id,name,subject,score\n"
        "1,Aruzhan,Programming,80\n"
        "2,Daniyar,Programming,40\n",
        encoding="utf-8",
    )

    processed_count = generate_report(input_file, output_file)

    with output_file.open("r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    assert processed_count == 2
    assert output_file.exists()
    assert rows[0]["result"] == "Pass"
    assert rows[1]["result"] == "Fail"