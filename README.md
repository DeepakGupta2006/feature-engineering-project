# 🧩 Feature Engineering with Pandas

A Python project demonstrating **Feature Engineering** — the process of creating new, more meaningful columns (features) from raw data to make it more useful for analysis, reporting, or machine learning.

---

## 📌 Overview

Raw data by itself is often not very useful. This project takes a simple raw dataset — containing things like date of birth, height, weight, signup date, and purchase date — and automatically **derives new, insightful features** from it using Python and pandas.

It's a hands-on, beginner-friendly example of one of the most important steps in any data science or machine learning pipeline: **turning raw facts into meaningful signals.**

---

## 🎯 What is Feature Engineering?

Feature engineering is the process of using domain knowledge to create new input variables (features) from existing raw data, in order to:
- Improve the performance of machine learning models
- Make data more interpretable for humans
- Reveal patterns that aren't obvious in the raw columns alone

> 💡 In many real-world projects, **better features improve results more than a better algorithm does.**

---

## ⚙️ Features This Project Creates

| New Feature | Derived From | Description |
|---|---|---|
| `age` | `date_of_birth` | Precise age in years, calculated as of today |
| `birth_year`, `birth_month`, `birth_weekday` | `date_of_birth` | Individual date components extracted |
| `age_group` | `age` | Bins age into categories: Teen, Young Adult, Adult, Middle Age, Senior |
| `bmi` | `height_cm`, `weight_kg` | Body Mass Index — combines two raw columns into one health metric |
| `days_since_signup` | `signup_date` | Customer tenure in days |
| `days_signup_to_purchase` | `signup_date`, `purchase_date` | Time taken to convert from signup to purchase |
| `is_adult` | `age` | Boolean flag — True/False |
| `is_recent_customer` | `days_since_signup` | Boolean flag for customers who signed up within the last 2 years |

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **pandas** — data manipulation and analysis

---

## 📂 Project Structure

```
feature-engineering-project/
│
├── feature_engineering.py     # Main script — loads data, creates features, saves output
├── engineered_features.csv    # Output file generated after running the script
├── README.md                  # Project documentation (this file)
└── .gitignore                 # Files/folders excluded from Git tracking
```

---

## 🚀 Getting Started

### 1. Clone this repository
```bash
git clone https://github.com/yourusername/feature-engineering-project.git
cd feature-engineering-project
```

### 2. Install dependencies
```bash
pip install pandas
```

### 3. Run the script
```bash
python feature_engineering.py
```

### 4. View the output
- Results print directly to your terminal
- A file named `engineered_features.csv` is created in the same folder — open it in Excel, Google Sheets, or any spreadsheet tool

---

## 📊 Example Output

| name | age | age_group | bmi | is_adult | days_since_signup |
|---|---|---|---|---|---|
| Alice | 36 | Adult | 22.04 | True | 1300 |
| Bob | 40 | Adult | 25.88 | True | 1500 |
| Charlie | 26 | Young Adult | 25.36 | True | 900 |
| Diana | 48 | Middle Age | 21.48 | True | 2000 |

*(Sample values — actual numbers depend on the date the script is run.)*

---

## 📥 Using Your Own Dataset

Replace the sample data section inside `feature_engineering.py`:

```python
data = {...}
df = pd.DataFrame(data)
```

with:

```python
df = pd.read_csv("your_file.csv")
```

Make sure your CSV has columns named (or renamed to):
- `date_of_birth`
- `height_cm`
- `weight_kg`
- `signup_date`
- `purchase_date`

If your column names differ, either rename them in your CSV or update the script accordingly:

```python
df.rename(columns={
    'DOB': 'date_of_birth',
    'account_created': 'signup_date',
    'order_date': 'purchase_date'
}, inplace=True)
```

---

## ✅ Data Validation

Before trusting the output, the script checks for missing/invalid values:

```python
print(df.isna().sum())
```

Make sure your date columns are properly formatted as `YYYY-MM-DD` before running the script, or they may fail to convert.

---

## 🧠 Key Learning Concepts Demonstrated

- Converting raw text into proper datetime objects
- Deriving new numeric features via calculations (age, BMI)
- Extracting components from datetime columns
- Creating time-delta features (days between two dates)
- Binning continuous variables into categories (`pd.cut`)
- Creating boolean flag features
- Exporting cleaned/enriched data to CSV

---

## 🔮 Possible Extensions

- Add more engineered features (e.g. income brackets, purchase frequency)
- Use `scikit-learn` pipelines (`ColumnTransformer`) for production-ready ML workflows
- Visualize the engineered features with `matplotlib` or `seaborn`
- Automate this as part of a larger ETL/data pipeline

---

## 📄 License

This project is open for learning and personal use. Feel free to fork, modify, and build on it.

---

## 🙋 Author

Created as a learning project to demonstrate practical feature engineering techniques using Python and pandas.
