import streamlit as st

# Set the title of the web app
st.title("User Information Form")

# Create a form with a unique key
with st.form(key="user_info_form"):

    # Text input for user's name
    name = st.text_input("Enter your name: ")

    # Number input for user's age
    age = st.number_input("Enter your age: ", min_value=0, step=1)

    # Print values to terminal (not displayed on Streamlit page)
    print(name, age)

    # Submit button for the form
    st.form_submit_button()