import streamlit as st
import pandas as pd
import joblib

st.title("Customer Analytics Dashboard")

tab1, tab2 = st.tabs(["📊 Dashboard", "🔮 Churn Prediction"])

with tab1:
    rfm = pd.read_csv("rfm_segments.csv")
    
    st.subheader("Customer Segment Overview")
    segment_counts = rfm['segment'].value_counts()
    st.bar_chart(segment_counts)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", len(rfm))
    col2.metric("Total Revenue", f"£{rfm['monetary'].sum():,.0f}")
    col3.metric("Avg Customer Value", f"£{rfm['monetary'].mean():,.0f}")
    
    st.subheader("Top 10 Customers by Spend")
    st.dataframe(rfm.sort_values('monetary', ascending=False).head(10)[['Customer ID', 'monetary', 'frequency', 'segment']])

with tab2:
    st.write("Predict whether a customer is likely to churn based on their purchase behavior.")
    model = joblib.load("churn_model.pkl")

    frequency = st.number_input("Number of orders placed", min_value=0, value=5)
    monetary = st.number_input("Total amount spent (£)", min_value=0.0, value=500.0)
    avg_order_value = st.number_input("Average order value (£)", min_value=0.0, value=50.0)
    distinct_products = st.number_input("Number of distinct products bought", min_value=0, value=10)
    tenure_days = st.number_input("Customer tenure (days)", min_value=0, value=100)

    if st.button("Predict Churn Risk"):
        input_data = pd.DataFrame([[frequency, monetary, avg_order_value, distinct_products, tenure_days]],
                                    columns=['frequency', 'monetary', 'avg_order_value', 'distinct_products', 'tenure_days'])
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            st.error(f"⚠️ High churn risk — {probability*100:.1f}% probability")
        else:
            st.success(f"✅ Low churn risk — {probability*100:.1f}% probability")
