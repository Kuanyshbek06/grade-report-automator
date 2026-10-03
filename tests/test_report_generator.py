import csv

import pytest

from src.report_generator import (
    calculate_result,
    generate_report,
    parse_score,
)


def test_calculate_result() -> None:
    assert calculate_result(100) == "Pass"
    assert calculate_result(50) == "Pass"
    assert calculate_result(49) == "Fail"
    assert calculate_result(0) == "Fail"


def test_parse_score_accepts_valid_values() -> None:
    assert parse_score("0") == 0
    assert parse_score("50") == 50
    assert parse_score("100") == 100


@pytest.mark.parametrize(
    "invalid_score",
    [None, "", "abc", "-1", "101"],
)
def test_parse_score_rejects_invalid_values(invalid_score) -> None:
    with pytest.raises(ValueError):
        parse_score(invalid_score)


def test_generate_report(tmp_path) -> None:
    input_file = tmp_path / "grades.csv"
    output_file = tmp_path / "report.csv"

    input_file.write_text(
        "student_id,name,subject,score\n"
        "1,Aruzhan,Programming,80\n"
        "2,Daniyar,Programming,40\n"
        "3,Aliya,Programming,105\n",
        encoding="utf-8",
    )

    processed_count = generate_report(input_file, output_file)

    with output_file.open("r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    assert processed_count == 3
    assert rows[0]["result"] == "Pass"
    assert rows[1]["result"] == "Fail"
    assert rows[2]["result"] == "Invalid"
    assert rows[2]["error"] == "Score must be between 0 and 100"


def test_generate_report_rejects_missing_columns(tmp_path) -> None:
    input_file = tmp_path / "grades.csv"
    output_file = tmp_path / "report.csv"

    input_file.write_text(
        "name,score\n"
        "Aruzhan,80\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        generate_report(input_file, output_file)

    assert not output_file.exists()