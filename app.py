import streamlit as st

# Remember login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ==========================
# LOGIN
# ==========================

if not st.session_state.logged_in:

    st.title("💊 PharmaKart")
    st.write("Welcome to Medicare Pharmacy!")

    st.header("Pharmacist Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "pharmacist" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Incorrect username or password.")


# ==========================
# MAIN MENU
# ==========================

else:

    st.title("💊 PharmaKart")
    st.success("Login Successful!")
    st.write("Welcome, Pharmacist!")

    st.header("Main Menu")

    choice = st.selectbox(
        "Choose a medicine:",
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

        strength = st.selectbox(
            "Choose Strength:",
            ["325 mg - ₱4.50", "500 mg - ₱5.55"]
        )

        quantity = st.number_input(
            "Enter quantity:",
            min_value=1,
            step=1
        )

        st.write("Selected:", strength)
        st.write("Quantity:", quantity)


    elif choice == "Vitamin C":

        st.subheader("Vitamin C")

        strength = st.selectbox(
            "Choose Strength:",
            ["500 mg - ₱2.25", "1000 mg - ₱7.50"]
        )

        quantity = st.number_input(
            "Enter quantity:",
            min_value=1,
            step=1
        )

        st.write("Selected:", strength)
        st.write("Quantity:", quantity)


    elif choice == "Atorvastatin":

        st.subheader("Atorvastatin")

        strength = st.selectbox(
            "Choose Strength:",
            ["20 mg - ₱17.25", "40 mg - ₱24.50"]
        )

        quantity = st.number_input(
            "Enter quantity:",
            min_value=1,
            step=1
        )

        st.write("Selected:", strength)
        st.write("Quantity:", quantity)


    elif choice == "Amlodipine":

        st.subheader("Amlodipine")

        strength = st.selectbox(
            "Choose Strength:",
            ["5 mg - ₱6.25", "10 mg - ₱9.50"]
        )

        quantity = st.number_input(
            "Enter quantity:",
            min_value=1,
            step=1
        )

        st.write("Selected:", strength)
        st.write("Quantity:", quantity)
