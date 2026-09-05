# Customer Churn Prediction & RFM Segmentation — Online Retail

🔗 **Live App:** https://customer-churn-rfm-analysis-6nwmjchz9aedyzvafis2zw.streamlit.app/

📄 **SQL Queries:** [queries.sql](./queries.sql)

## Problem
An online UK-based retailer needed to identify which customers were at risk of 
churning, and segment its customer base to prioritize retention efforts.

## Approach
- Cleaned and loaded ~197K transaction records (Online Retail II, UCI/Kaggle) into a PostgreSQL database (Neon)
- Wrote SQL queries (joins, window functions, date functions) to compute revenue trends and per-customer RFM (Recency, Frequency, Monetary) metrics
- Segmented ~3,000 customers into 6 groups (Champions, Loyal, At Risk, Lost, New, Needs Attention) using RFM scoring
- Built a churn prediction model (Random Forest) using a time-based train/test split to avoid data leakage — predicting churn using only pre-cutoff behavior
- Deployed an interactive Streamlit app for real-time churn risk prediction

## Key Insights
- UK accounts for ~92% of total revenue; customer analysis focused accordingly
- Top 20 customers alone generated over £1M in combined revenue
- 716 customers (24%) fall into the "Lost" segment — a clear retention target
- Model achieves 62% accuracy vs. a 57.5% baseline, using a leakage-free time-split validation (an earlier naive version scored 67% but was found to leak future information — corrected by rebuilding features with a proper time cutoff)
- `monetary` and `avg_order_value` were the strongest churn predictors — low spenders churn more, even if they order somewhat frequently

## Tech Stack
Python (pandas, scikit-learn) · SQL (PostgreSQL/Neon) · Streamlit · GitHub

## Video Walkthrough
[Add your Loom link here once recorded]
