
      import streamlit as st

st.title("💊 PharmaKart")
st.write("Welcome to Medicare Pharmacy!")

st.header("Pharmacist Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if username == "pharmacist" and password == "1234":
        st.success("Login Successful!")
        st.write("Welcome, Pharmacist", username)

        st.header("Main Menu")

        choice = st.selectbox(
            "Choose an option:",
            [
                "Select a medicine",
                "Paracetamol",
                "Vitamin C",
                "Atorvastatin",
                "Amlodipine"
            ]
        )

        if choice == "Paracetamol":
            st.subheader("Paracetamol")
            st.write("325 mg - ₱4.50")
            st.write("500 mg - ₱5.55")

        elif choice == "Vitamin C":
            st.subheader("Vitamin C")
            st.write("500 mg - ₱2.25")
            st.write("1000 mg - ₱7.50")

        elif choice == "Atorvastatin":
            st.subheader("Atorvastatin")
            st.write("20 mg - ₱17.25")
            st.write("40 mg - ₱24.50")

        elif choice == "Amlodipine":
            st.subheader("Amlodipine")
            st.write("5 mg - ₱6.25")
            st.write("10 mg - ₱9.50")

    else:
        st.error("Incorrect username or password.")
