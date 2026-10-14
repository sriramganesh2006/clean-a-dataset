from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "student_data.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    original = pd.read_csv(DATA_PATH, skipinitialspace=True)
    df = original.copy()

    print("=== DATASET BEFORE CLEANING ===")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    print("\nMissing values by column:\n", df.isna().sum())
    print(f"\nDuplicate rows: {df.duplicated().sum()}")

    # Standardize whitespace in text fields.
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].map(
            lambda value: value.strip() if isinstance(value, str) else value
        )
        df[column] = df[column].replace("", pd.NA)

    # Convert numeric fields safely; invalid values become missing values.
    for column in ["Age", "Marks"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    duplicates_removed = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()

    # Fill missing numeric values with the median and text values with the mode.
    for column in df.columns:
        if df[column].isna().any():
            if pd.api.types.is_numeric_dtype(df[column]):
                df[column] = df[column].fillna(df[column].median())
            else:
                mode = df[column].mode(dropna=True)
                df[column] = df[column].fillna(mode.iloc[0] if not mode.empty else "Unknown")

    cleaned_path = OUTPUT_DIR / "cleaned_student_data.csv"
    df.to_csv(cleaned_path, index=False)

    missing = original.isna().sum()
    plt.figure(figsize=(9, 5))
    missing.plot(kind="bar")
    plt.title("Missing Values Before Cleaning")
    plt.xlabel("Column")
    plt.ylabel("Number of Missing Values")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    chart_path = OUTPUT_DIR / "missing_values_chart.png"
    plt.savefig(chart_path, dpi=150)
    plt.close()

    print("\n=== CLEANING SUMMARY ===")
    print(f"Duplicate rows removed: {duplicates_removed}")
    print(f"Remaining missing values: {int(df.isna().sum().sum())}")
    print(f"Cleaned CSV: {cleaned_path}")
    print(f"Chart: {chart_path}")
    print("\nCleaned dataset preview:\n", df.head())


if __name__ == "__main__":
    main()
