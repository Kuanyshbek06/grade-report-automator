# Grade Report Automator

[![CI](https://github.com/Kuanyshbek06/grade-report-automator/actions/workflows/tests.yml/badge.svg)](https://github.com/Kuanyshbek06/grade-report-automator/actions/workflows/tests.yml)

A Python automation tool that reads student grades from a CSV file, validates the data, calculates pass/fail results, and generates a processed report.

## Features

- Reads student data from CSV
- Supports custom input and output file paths
- Calculates Pass or Fail based on the score
- Creates the output directory automatically
- Generates a new CSV report
- Validates required CSV columns
- Detects missing, non-numeric, and out-of-range scores
- Records validation errors without stopping the entire process
- Includes automated tests with pytest
- Runs tests and Docker builds automatically with GitHub Actions

## Project Structure

```text
grade-report-automator/
├── .github/
│   └── workflows/
│       └── tests.yml
├── data/
│   └── sample_grades.csv
├── src/
│   ├── __init__.py
│   └── report_generator.py
├── tests/
│   └── test_report_generator.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## Installation

Create a virtual environment:

```powershell
python -m venv .venv
```

Install the dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Usage

Run the report generator using the default input and output paths:

```powershell
.\.venv\Scripts\python.exe src/report_generator.py
```

The generated report will be saved to:

```text
output/grade_report.csv
```

You can also provide custom input and output paths:

```powershell
.\.venv\Scripts\python.exe src/report_generator.py --input data/sample_grades.csv --output output/custom_report.csv
```

View all available command-line options:
