import streamlit as st

# Hardcoded credentials (for demonstration purposes)
valid_username = "demo"
valid_password = "password"

class LandingPage:
    @staticmethod
    def show():
        st.title("Welcome to Your Mental Health Tracker")

        # Add buttons for options
        option = st.radio("Choose an option:", ["Schedule an Appointment", "Daily Diary"])

        if option == "Schedule an Appointment":
            LandingPage.schedule_appointment()
        elif option == "Daily Diary":
            LandingPage.daily_diary()

    @staticmethod
    def schedule_appointment():
        st.header("Schedule an Appointment")
        st.write("This feature is coming soon!")

    @staticmethod
    def daily_diary():
        st.header("Daily Diary")

        # Questions about mental health on a Likert scale
        questions = [
            "How would you rate your overall mood today?",
            "On a scale of 1 to 10, how well did you sleep last night?",
            "How would you rate your stress level today?",
            "How motivated do you feel today?",
            "On a scale of 1 to 10, how satisfied are you with your day?"
        ]

        # Display Likert scale questions
        for i, question in enumerate(questions, start=1):
            response = st.slider(question, 1, 10, 5, key=f"question_{i}")

def login():
    st.title("Login Page")

    # Get user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Check if credentials are valid
    if st.button("Login"):
        if username == valid_username and password == valid_password:
            st.success("Login successful!")

            # Clear login page content
            st.text("")

            # Show the landing page
            LandingPage.show()

if __name__ == "__main__":
    login()
