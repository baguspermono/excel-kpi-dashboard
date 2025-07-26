import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="KPI Dashboard", layout="wide")

# Title
st.title("📊 Excel KPI Dashboard App")
st.markdown("Upload your Excel file to view a summary dashboard.")

# Upload section
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("Raw Data Preview")
    st.dataframe(df)

    # Basic KPIs
    total_revenue = df['Revenue'].sum()
    total_expenses = df['Expenses'].sum()
    total_profit = df['Profit'].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${total_revenue:,.0f}")
    col2.metric("Total Expenses", f"${total_expenses:,.0f}")
    col3.metric("Total Profit", f"${total_profit:,.0f}")

    # Time series chart
    st.subheader("📈 Revenue and Profit Over Time")
    fig, ax = plt.subplots(figsize=(10, 4))
    df_sorted = df.sort_values("Date")
    ax.plot(df_sorted['Date'], df_sorted['Revenue'], marker='o', label='Revenue')
    ax.plot(df_sorted['Date'], df_sorted['Profit'], marker='s', label='Profit')
    ax.set_ylabel("Amount ($)")
    ax.set_xlabel("Date")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Category breakdown
    st.subheader("📊 Revenue by Category")
    fig2, ax2 = plt.subplots()
    sns.barplot(data=df, x='Category', y='Revenue', ax=ax2)
    ax2.set_title("Revenue by Category")
    st.pyplot(fig2)

    # Option to download filtered data
    st.download_button(
        label="📥 Download Processed Data",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='cleaned_kpi_data.csv',
        mime='text/csv'
    )
else:
    st.info("👈 Upload an Excel file to get started.")