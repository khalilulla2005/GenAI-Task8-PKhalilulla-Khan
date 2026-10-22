import streamlit as st
st.title("Product Entry Form")
with st.sidebar:
    st.header("Product Details")
    product_name = st.text_input("Product Name")
    category = st.selectbox("Category", ["Electronics", "Clothing", "Home", "Books", "Other"])
    price = st.number_input("Price ($)", min_value=0.0, step=0.5)
    add_product = st.button("Add Product")
if add_product:
    if product_name:
        st.success("Product added successfully!")
        st.write(f"**Name:** {product_name}")
        st.write(f"**Category:** {category}")
        st.write(f"**Price:** ${price:.2f}")
    else:
        st.error("Please enter a product name.")
