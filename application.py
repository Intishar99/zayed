import streamlit as st

# Hardcoded credentials (for demonstration purposes)
valid_username = "demo"
valid_password = "password"

def login():
    st.title("Login Page")

    # Get user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Check if credentials are valid
    if st.button("Login"):
        if username == valid_username and password == valid_password:
            st.success("Login successful!")
            # Redirect to the landing page or perform further actions
        else:
            st.error("Invalid credentials. Please try again.")

if __name__ == "__main__":
    login()
