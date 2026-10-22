import streamlit as st
st.title("Simple Sales Dashboard")
sales = {"January": 1200, "February": 1500, "March": 900, "April": 2000}
selected_month = st.selectbox("Select a Month:", list(sales.keys()))
st.metric(label=f"Sales for {selected_month}", value=f"${sales[selected_month]}")
st.subheader("Overall Sales Chart")
st.bar_chart(sales)
