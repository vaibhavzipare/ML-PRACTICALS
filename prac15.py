import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Simple Streamlit App",
    page_icon="👋",
    layout="centered"
)

# Application title
st.title("Simple Streamlit App")

# Short description
st.write("Enter your name below to see a greeting.")

# Text input
name = st.text_input("Enter your name:")

# Display the entered text and greeting
if name:
    st.write("You entered:", name)
    st.success(f"Hello, {name}!")
else:
    st.info("Please enter your name in the text box above.")
