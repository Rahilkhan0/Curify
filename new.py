import streamlit as st

# Create a list of buttons
buttons = ["Home", "About", "Contact Us", "Login"]

# Create a column for the buttons
col = st.columns(len(buttons))[1:]

# Add each button to the column, with a horizontal margin of 10px
for button in buttons:
    style={"margin-left": "10px"}
    st.button(button, key=button,)
