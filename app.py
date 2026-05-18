import streamlit as st
import sqlite3
from datetime import datetime

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("bill_payment.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    bill_type TEXT,
    bill_amount REAL,
    payment_method TEXT,
    discount REAL,
    final_amount REAL,
    date TEXT
)
""")

conn.commit()

# ---------------- PAGE ---------------- #

st.set_page_config(
    page_title="Bill Payment System",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Advanced Bill Payment System")

st.write("Pay your bills easily")

# ---------------- INPUTS ---------------- #

customer_name = st.text_input(
    "Enter Customer Name"
)

bill_type = st.selectbox(
    "Select Bill Type",
    [
        "Electricity Bill",
        "Gas Bill",
        "Water Bill",
        "Internet Bill",
        "Mobile Load"
    ]
)

bill_amount = st.number_input(
    "Enter Bill Amount",
    min_value=0.0
)

payment_method = st.selectbox(
    "Select Payment Method",
    [
        "Cash",
        "Card"
    ]
)

# ---------------- CARD DETAILS ---------------- #

# ---------------- CARD DETAILS ---------------- #

if payment_method == "Card":

    st.subheader("💳 Card Details")

    card_company = st.selectbox(
        "Select Card Company",
        [
            "Visa",
            "MasterCard",
            "PayPak",
            "UnionPay",
            "American Express",
            "UBL Omni",
            "HBL Power",
            "Meezan Bank",
            "taqva islamic",
            "Alfalah Bank",
            "Bank Al Habib",
            "Bank of Punjab",
            "Bank Islami",
            "Faysal Bank",
            "Standard Chartered",
            "Askari Bank",
            "Silk Bank",
            "Soneri Bank",
            "MCB Bank",
            "Allied Bank",
            "JS Bank",
            "Summit Bank",
            "Bank Al Falah",
            "State Bank of Pakistan",
            "Habib Bank",
            "National Bank of Pakistan",
            "Dubai Islamic Bank",
            "Bank of Khyber",
            "Bank of Azad Jammu and Kashmir",
            "Bank of Gilgit Baltistan",
            "Bank of Baluchistan",
            "Bank of Sindh"
        ]
    )

    card_name = st.text_input(
        "Card Holder Name"
    )

    card_number = st.text_input(
        "Card Number"
    )

    expiry = st.text_input(
        "Expiry Date (MM/YY)"
    )

    cvv = st.text_input(
        "CVV",
        type="password"
    )

# ---------------- PAYMENT BUTTON ---------------- #

if st.button("Pay Bill"):

    if customer_name == "":
        st.error("Please enter customer name")

    elif bill_amount <= 0:
        st.error("Please enter valid bill amount")

    else:

        discount = 0
        final_amount = bill_amount

        # CASH DISCOUNT
        if payment_method == "Cash":

            discount = bill_amount * 0.10

            final_amount = bill_amount - discount

        # CARD DISCOUNT
        elif payment_method == "Card":

            discount = bill_amount * 0.05

            final_amount = bill_amount - discount

        # DATE
        payment_date = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        # SAVE DATA
        cursor.execute("""
        INSERT INTO payments(
            customer_name,
            bill_type,
            bill_amount,
            payment_method,
            discount,
            final_amount,
            date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (

            customer_name,
            bill_type,
            bill_amount,
            payment_method,
            discount,
            final_amount,
            payment_date

        ))

        conn.commit()

        # SUCCESS MESSAGE
        st.success("✅ Bill Paid Successfully")

        st.write("## 🧾 Payment Receipt")

        st.write(f"Customer Name: {customer_name}")

        st.write(f"Bill Type: {bill_type}")

        st.write(f"Original Bill: {bill_amount}")

        st.write(f"Payment Method: {payment_method}")

        st.write(f"Discount: {discount}")

        st.write(f"Final Amount: {final_amount}")

        st.write(f"Payment Date: {payment_date}")

# ---------------- HISTORY ---------------- #

st.subheader("📜 Payment History")

if st.button("View Payment History"):

    cursor.execute("""
    SELECT * FROM payments
    """)

    data = cursor.fetchall()

    if data:

        for row in data:

            st.write("--------------------------------")

            st.write(f"ID: {row[0]}")

            st.write(f"Customer: {row[1]}")

            st.write(f"Bill Type: {row[2]}")

            st.write(f"Bill Amount: {row[3]}")

            st.write(f"Payment Method: {row[4]}")

            st.write(f"Discount: {row[5]}")

            st.write(f"Final Amount: {row[6]}")

            st.write(f"Date: {row[7]}")

    else:
        st.warning("No payment history found")

# ---------------- DELETE HISTORY ---------------- #

if st.button("Delete Payment History"):

    cursor.execute("""
    DELETE FROM payments
    """)

    conn.commit()

    st.error("❌ Payment History Deleted")