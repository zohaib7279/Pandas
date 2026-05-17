import streamlit as st

st.set_page_config(page_title="Payment System", page_icon="💳")

st.title("💳 Advanced Bill Payment System")

# History save karne ke liye
if "history" not in st.session_state:
    st.session_state.history = []

# Bill amount input
bill_amount = st.number_input("Enter Bill Amount", min_value=0.0)

# Payment method
payment_method = st.selectbox(
    "Select Payment Method",
    ["Cash", "Card"]
)

# Card details
if payment_method == "Card":
    card_name = st.text_input("Enter Card Holder Name")
    card_number = st.text_input("Enter Card Number")
    expiry = st.text_input("Expiry Date (MM/YY)")
    cvv = cvv = st.text_input("CVV", type="password")

# Pay button
if st.button("Pay Now"):

    final_amount = bill_amount
    discount = 0

    # Cash Discount
    if payment_method == "Cash":
        discount = bill_amount * 0.10
        final_amount = bill_amount - discount

    # Card Discount
    elif payment_method == "Card":
        discount = bill_amount * 0.05
        final_amount = bill_amount - discount

    # Save history
    st.session_state.history.append({
        "Bill Amount": bill_amount,
        "Payment Method": payment_method,
        "Discount": discount,
        "Final Amount": final_amount
    })

    # Output
    st.success("Payment Successful ✅")

    st.write(f"### Original Bill: {bill_amount}")
    st.write(f"### Discount: {discount}")
    st.write(f"### Final Amount: {final_amount}")

# View history
if st.button("View Payment History"):

    if st.session_state.history:
        st.write("## Payment History")

        for item in st.session_state.history:

            st.write("----------------------------")
            st.write(f"Bill Amount: {item['Bill Amount']}")
            st.write(f"Payment Method: {item['Payment Method']}")
            st.write(f"Discount: {item['Discount']}")
            st.write(f"Final Amount: {item['Final Amount']}")

    else:
        st.warning("No payment history found.")

# Delete history
if st.button("Delete History"):
    st.session_state.history.clear()
    st.error("History Deleted Successfully ❌")