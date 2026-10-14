# Clean a Dataset — Internship Task 3

## Objective
Clean a student dataset with Python and Pandas by handling missing values, removing duplicate records, trimming text whitespace, converting numeric columns, and saving a cleaned CSV plus a missing-values chart.

## Technologies
- Python
- Pandas
- Matplotlib

## Project structure
```text
clean-a-dataset/
├── data/student_data.csv
├── output/ (generated files)
├── clean_dataset.py
├── requirements.txt
└── README.md
```

## Run on Windows
1. Install Python 3.10 or newer.
2. Open a terminal in this repository folder.
3. Install dependencies: `py -m pip install -r requirements.txt`
4. Run: `py clean_dataset.py`
5. Open `output/cleaned_student_data.csv` and `output/missing_values_chart.png`.

## Cleaning steps
1. Report missing values and duplicate rows.
2. Trim whitespace in text columns.
3. Convert Age and Marks to numeric values.
4. Remove duplicate rows.
5. Fill missing numeric values with the median and categorical values with the most frequent value.
6. Export the cleaned CSV and chart.

## Dataset note
The included CSV is a small sample dataset for demonstrating the workflow. For real datasets, inspect the data and choose cleaning rules appropriate to the problem.
