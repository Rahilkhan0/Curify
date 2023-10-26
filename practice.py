import streamlit as st
import pickle
from streamlit_option_menu import option_menu
from flask import flask
import opencv

# Load the diabetes prediction model
diabetes_model = pickle.load(open('C:/Users/Arbaz Khan/Downloads/Multiple-Disease-Prediction-System-main/Multiple-Disease-Prediction-System-main/Saved models/diabetes_model.sav', 'rb'))

# Define a custom Contact Us page function
def contact_us():
    st.title("Contact Us Page")
    st.write("Please fill out the form below to contact us.")
    st.read()

    # Create or load session state to store form data
    if "contact_form" not in st.session_state:
        st.session_state.contact_form = {
            "name": "",
            "email": "",
            "subject": "",
            "message": ""
        }

    # Create input fields for contact information
    name = st.text_input("Name", st.session_state.contact_form["name"])
    email = st.text_input("Email", st.session_state.contact_form["email"])
    subject = st.text_input("Subject", st.session_state.contact_form["subject"])
    message = st.text_area("Message", st.session_state.contact_form["message"], height=200)
    rollno = st.text_area("Message", st.session_state.contact_form["message"], height=200)

    # Store the form data in session_state
    st.session_state.contact_form["name"] = name
    st.session_state.contact_form["email"] = email
    st.session_state.contact_form["subject"] = subject
    st.session_state.contact_form["message"] = message

    # Create a button to submit the form
    if st.button("Submit"):
        # You can add your logic here to handle the form submission
        st.success("Thank you for your message! We will get back to you soon.")

# Define a custom Disease Prediction page function
def disease_prediction():
    st.title('Diabetes Prediction using ML')

    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Not Diabetic'

        st.success(diab_diagnosis)

# Define functions to render different pages
def home():
    st.title("Home Page")
    st.write("Welcome to our website!")

def login():
    st.title("Login Page")
    # Add your login form or content here

def about_us():
    st.title("About Us Page")
    # Add information about your organization or team here

# Create a sidebar for navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", ["Home", "Login", "Contact Us", "About Us", "Disease Prediction"])

# Add style to highlight the selected page in the main navigation
style = "background-color: #f0f0f0; padding: 5px 10px; border-radius: 5px;"
selected_style = "background-color: #0078d4; color: white; padding: 5px 10px; border-radius: 5px;"

# Display the selected page based on sidebar navigation
if selected_page == "Home":
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">Home</a></div>', unsafe_allow_html=True)
    home()
else:
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">Home</a></div>', unsafe_allow_html=True)

if selected_page == "Login":
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">Login</a></div>', unsafe_allow_html=True)
    login()
else:
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">Login</a></div>', unsafe_allow_html=True)

if selected_page == "Contact Us":
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">Contact Us</a></div>', unsafe_allow_html=True)
    contact_us()
else:
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">Contact Us</a></div>', unsafe_allow_html=True)

if selected_page == "About Us":
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">About Us</a></div>', unsafe_allow_html=True)
    about_us()
else:
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">About Us</a></div>', unsafe_allow_html=True)

if selected_page == "Disease Prediction":
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">Disease Prediction</a></div>', unsafe_allow_html=True)
    disease_prediction()
else:
    st.sidebar.markdown(f'<div style="{style}"><a href="#" style="text-decoration: none; color: #333;">Disease Prediction</a></div>', unsafe_allow_html=True)
