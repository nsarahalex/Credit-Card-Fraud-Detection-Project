# Credit-Card-Fraud-Detection-Project

# Credit Card Fraud Detection Project

## Overview
An anomaly detection pipeline designed to identify potentially fraudulent credit card transactions within highly imbalanced datasets.

## Key Features
* **Data Profiling:** Automated calculation of class imbalance (fraud vs. legit).
* **Feature Engineering:** Implemented rule-based anomaly detection using multi-factor signals (Amount).
* **Performance:** Achieved precision-based filtering to reduce false positives for manual review.

## How to Run
1. Clone this repository.
2. Place `creditcard.csv` in the `/data` directory. [here](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
3. Run `python3 src/analyzer2.py` to generate the `flagged_transactions.csv` report.
