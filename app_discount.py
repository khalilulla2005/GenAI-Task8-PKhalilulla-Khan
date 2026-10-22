import streamlit as st
st.title("Price Calculator")
price = st.number_input("Enter product price:", min_value=0.0, step=1.0)
discount = st.slider("Discount Percentage (%)", min_value=0, max_value=50, value=10)
if st.button("Calculate"):
    final_price = price - (price * (discount / 100))
    st.success(f"Original Price: ${price:.2f} | Discount: {discount}% | Final Price: ${final_price:.2f}")
    st.subheader("Before vs After Comparison")
    table_data = [["Before Discount", "After Discount"], [f"${price:.2f}", f"${final_price:.2f}"]]
    st.table(table_data)
