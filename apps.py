import streamlit as st

st.title("Calculator")

a = st.number_input("Enter first number:", step=1)
b = st.number_input("Enter second number:", step=1)

operation = st.selectbox(
    "Enter operation",
    ["+", "-", "*", "/"]
)

if st.button("Calculate"):

    if operation == "+":
        st.success(f"Result: {a + b}")

    elif operation == "-":
        st.success(f"Result: {a - b}")

    elif operation == "*":
        st.success(f"Result: {a * b}")

    elif operation == "/":
        if b != 0:
            st.success(f"Result: {a / b}")
        else:
            st.error("Error: Division by zero is not allowed.")