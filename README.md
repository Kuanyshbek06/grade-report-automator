# Grade Report Automator

A Python automation tool that reads student grades from a CSV file,
calculates pass/fail results, and generates a processed report.

## Features

- Reads student data from CSV
- Calculates Pass or Fail based on the score
- Creates the output directory automatically
- Generates a new CSV report
- Includes automated tests with pytest
- Runs tests automatically with GitHub Actions

## Project Structure

```text
grade-report-automator/
├── .github/
│   └── workflows/
│       └── tests.yml
├── data/
│   └── sample_grades.csv
├── output/
├── src/
│   ├── __init__.py
│   └── report_generator.py
├── tests/
│   └── test_report_generator.py
├── .gitignore
├── README.md
└── requirements.txt