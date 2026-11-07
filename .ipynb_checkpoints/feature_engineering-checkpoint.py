"""
A complete, runnable example of Feature Creation:
combining/deriving new features from existing columns.

Run with:  python feature_engineering.py
"""

import pandas as pd
from datetime import datetime


# STEP 1: Load your data

# Replace this block with: df = pd.read_csv("your_file.csv")
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Deepak'],
    'date_of_birth': ['1990-05-15', '1985-11-02', '2000-01-30', '2006-10-21'],
    'height_cm': [165, 178, 172, 160],
    'weight_kg': [60, 82, 75, 61],
    'purchase_date': ['2024-01-10', '2024-03-15', '2024-06-20', '2025-08-01'],
    'signup_date': ['2023-01-01', '2022-06-15', '2023-11-01', '2024-03-10']
}
df = pd.DataFrame(data)


# STEP 2: Convert date-like text columns to real dates

date_cols = ['date_of_birth', 'purchase_date', 'signup_date']
for col in date_cols:
    df[col] = pd.to_datetime(df[col])

# STEP 3: Helper function for precise age calculation

def calculate_age(dob, ref_date=None):
    if ref_date is None:
        ref_date = pd.Timestamp(datetime.now().date())
    age = ref_date.year - dob.year
    if (ref_date.month, ref_date.day) < (dob.month, dob.day):
        age -= 1
    return age


# STEP 4: Create derived features

today = pd.Timestamp(datetime.now().date())

# Age from date of birth
df['age'] = df['date_of_birth'].apply(calculate_age)

# Date part extraction
df['birth_year'] = df['date_of_birth'].dt.year
df['birth_month'] = df['date_of_birth'].dt.month
df['birth_weekday'] = df['date_of_birth'].dt.day_name()

# Tenure / time-between-dates features
df['days_since_signup'] = (today - df['signup_date']).dt.days
df['days_signup_to_purchase'] = (df['purchase_date'] - df['signup_date']).dt.days

# Combining two numeric columns -> BMI
df['bmi'] = (df['weight_kg'] / ((df['height_cm'] / 100) ** 2)).round(2)

# Binning a continuous feature into categories
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 18, 30, 45, 60, 100],
    labels=['Teen', 'Young Adult', 'Adult', 'Middle Age', 'Senior']
)


df['is_adult'] = df['age'] >= 18
df['is_recent_customer'] = df['days_since_signup'] < 730


# STEP 5: Check for missing/invalid values before trusting results

print("Missing values per column:")
print(df.isna().sum())
print()


# STEP 6: View the result

print("Final DataFrame with engineered features:")
print(df.to_string(index=False))


# STEP 7: Save the result

df.to_csv("engineered_features.csv", index=False)
print("\nSaved output to engineered_features.csv")