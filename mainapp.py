import streamlit as st
from streamlit_option_menu import option_menu

session_state = st.session_state
if not hasattr(session_state, 'user_authenticated'):
    session_state.user_authenticated = False


with st.sidebar:
    Selected=option_menu(
        menu_title="Curify Disease prediction System",
        options=["Home", "Diseases",  "Account","Contact Us","About Us" ],
        default_index=0,    
         

    )
  
if Selected=="Home":
        import base64
        import streamlit as st
        import plotly.express as px



        import base64
        import streamlit.components.v1 as components
        import pandas as pd
        from PIL import Image
        import random
        import string
        import sklearn


 
        hide_menu_style = """
                <style>
                #MainMenu {visibility: hidden; }
                footer {visibility: hidden;}
                </style>
                """
        st.markdown(hide_menu_style, unsafe_allow_html=True)
        def add_bg_from_local(image_file):
                with open(image_file, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
                )
        add_bg_from_local('cell.jpg') 
        st.markdown("<h1 style='text-align: center; color: #212759; font-size: 200px; font-family: Arial; background-color: #e0e8f0; border-radius: 25px;'>Curify</h1>", unsafe_allow_html=True)
        st.markdown(" ")
        st.markdown("<h1 style='text-align:center; color: #ffffff; font-size: 20px; font-family: Arial;'>A program that detects diseases by using Machine Learning</h1>", unsafe_allow_html=True)


        
        
        
# Header
        
        st.markdown("<h1 style='text-align:left ; color:white; font-size:40px; font-family: Arial;'>Welcome to the Multiple Disease Prediction System</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:left ; color: #ffffff; font-size: 15px; font-family: Arial;'>Your one-stop solution for predicting multiple diseases.</h1>", unsafe_allow_html=True)
         
        
        
        st.markdown("<h1 style='text-align:left ; color: #ffffff; font-size: 25px; font-family: Arial;'>How to Get Started</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:left ; color: #ffffff; font-size: 15px; font-family: Arial;'>1. Navigate to the 'disease' page</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:left ; color: #ffffff; font-size: 15px; font-family: Arial;'>2. Enter your health information.</h1>", unsafe_allow_html=True) 
        st.markdown("<h1 style='text-align:left ; color: #ffffff; font-size: 15px; font-family: Arial;'>3. Click the 'Predict' button to see the results.:</h1>", unsafe_allow_html=True)
         

# Key Features
        #st.header("Key Features")
        st.markdown("<h1 style='text-align:left ; color: #ffffff; font-size: 25px; font-family: Arial;'>Key Features</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:left ; color: #ffffff; font-size: 15px; font-family: Arial;'>Our app offers the following features:</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:left ; color:  white; font-size: 15px; font-family: Arial;'>🔬 Accurate disease prediction using machine learning.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:left ; color: white; font-size: 15px; font-family: Arial;'>👩‍⚕️ User-friendly interface for health assessments.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:left ; color: #ffffff; font-size: 15px; font-family: Arial;'>🔒 Strict data privacy and security measures.</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:left ; color: #ffffff; font-size: 15px; font-family: Arial;'>📋 Predict multiple diseases with a single app.</h1>", unsafe_allow_html=True)
      #  st.write("Our app offers the following features:")
        
 
 

    # Important Notes
        
        #st.button("Get Started")

        # Footer
        #st.write("© 2023 Disease Prediction System")

     

if Selected=="Diseases"  :

    if st.session_state.user_authenticated:
        import pickle
        

       

        try:  
        


                diabetes_model = pickle.load(open( 'C:/Users/Arbaz Khan/Downloads/Multiple-Disease-Prediction-System-main/Multiple-Disease-Prediction-System-main/Saved models/diabetes_model.sav ',"rb"))
                heart_disease_model = pickle.load(open('C:/Users/Arbaz Khan/Downloads/Multiple-Disease-Prediction-System-main/Multiple-Disease-Prediction-System-main/Saved models/heart_disease_model.sav','rb'))
                parkinsons_model = pickle.load(open('C:/Users/Arbaz Khan/Downloads/Multiple-Disease-Prediction-System-main/Multiple-Disease-Prediction-System-main/Saved models/parkinsons_model.sav','rb'))

                

                with st.sidebar:
                    
                    selected = option_menu('Curify',
                                        ['Diabetes Prediction',"Heart Disease" ,"Parkinsons disease prediction"],
                                        icons = ['activity','heart','person'],
                                        default_index = 0)
                    
                    

                if(selected == 'Diabetes Prediction'):
                        import streamlit as st
                        from streamlit_option_menu import option_menu
                        import base64
                        import streamlit as st
                        import plotly.express as px

                        def add_bg_from_local(image_file):
                         with open(image_file, "rb") as image_file:
                            encoded_string = base64.b64encode(image_file.read())
                            st.markdown(
                            f"""
                            <style>
                            .stApp {{
                                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                                background-size: cover
                            }}
                            </style>
                            """,
                            unsafe_allow_html=True
                            )
                        add_bg_from_local('images.jpg')    
                                    
                        st.title('Diabetes Prediction using ML')
                        gender=st.radio("Select your gender",("Male","Female"))
                        if gender=="Male":
                             Pregnancies=0
                        else :     
                            Pregnancies = st.number_input('Number of Pregnancies')
                        Glucose = st.number_input('Glucose Level')
                        BloodPressure = st.number_input('Blood Pressure value')
                        SkinThickness = st.number_input('Skin Thickness value')
                        Insulin = st.number_input('Insulin Level')
                        BMI = st.number_input('BMI value')
                        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
                        Age = st.number_input('Age of the Person')
                        
                        
                         
                        
                        diab_diagnosis = ''
                        
                        
                        
                        if st.button('Diabetes Test Result'):
                            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                            
                            if (diab_prediction[0]==1):
                                diab_diagnosis = 'The person is Diabetic'
                                
                            else:
                                diab_diagnosis = 'The person is Not Diabetic'
                                
                                
                        st.success(diab_diagnosis)
                



                if(selected == 'Heart Disease'):
                    import streamlit as st
                    from streamlit_option_menu import option_menu
                    import base64
                    import streamlit as st
                    import plotly.express as px

                    def add_bg_from_local(image_file):
                     with open(image_file, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                        st.markdown(
                        f"""
                        <style>
                        .stApp {{
                            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                            background-size: cover
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                        )
                    add_bg_from_local('heart.png')
                #Page title
                    st.title('Heart Disease Prediction using ML')
                    
                    age = st.number_input('Age of the Person')
                    sex = st.number_input(' Gender of the Person',min_value=0,max_value=1)
                    cp = st.number_input('Chest pain types')
                    trestbps = st.number_input('Resting Blood Pressure')
                    chol = st.number_input('Serum Cholestoral in mg/dl')
                    fbs = st.number_input('Fasting blood sugar > 120 mg/dl')
                    restecg = st.number_input('Resting Electrocardiographic results')
                    thalach = st.number_input('Maximum Heart Rate achieved')
                    exang = st.number_input('Exercise Induced Angina')
                    oldpeak = st.number_input('ST depression induced by exercise')
                    slope = st.number_input('Slope of the peak exercise ST segment')
                    ca = st.number_input('Mjor vessels colored by flourosopy')
                    thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
                    
                    
                    #Code for prediction
                    heart_diagnosis = ''
                    
                    #Creating a button for prediction
                    
                    if st.button('Heart Test Result'):
                        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
                        
                        if (heart_prediction[0]==1):
                            heart_diagnosis = 'The person is suffering from Heart disease'
                            
                        else:
                            heart_diagnosis = 'The person is Not suffering from Heart disease'
            
            
                
                    st.success(heart_diagnosis)

                if(selected == 'Parkinsons disease prediction'):
                    import streamlit as st
                    from streamlit_option_menu import option_menu
                    import base64
                    import streamlit as st
                    import plotly.express as px

                    def add_bg_from_local(image_file):
                     with open(image_file, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                        st.markdown(
                        f"""
                        <style>
                        .stApp {{
                            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                            background-size: cover
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                        )
                    add_bg_from_local('images.jpg')

   
                    st.title('Parkinsons Prediction using ML')
                        

                    fo = st.text_input("MDVP Fo(Hz)")
                    fhi = st.text_input("MDVP Fhi(Hz)")
                    flo = st.text_input("MDVP Flo(Hz)")
                    Jitter_percent = st.text_input("MDVP Jitter(%)")
                    Jitter_Abs = st.text_input('MDVP Jitter(Abs)')
                    RAP = st.text_input('MDVP RAP')
                    PPQ = st.text_input('MDVP PPQ')
                    DDP = st.text_input('Jitter DDP')
                    Shimmer = st.text_input('MDVP Shimmer')
                    Shimmer_dB = st.text_input('MDVP Shimmer(dB)')
                    APQ3 = st.text_input('Shimmer APQ3')
                    APQ5 = st.text_input('Shimmer APQ5')
                    APQ = st.text_input('MDVP APQ')
                    DDA = st.text_input('Shimmer DDA')
                    NHR = st.text_input('NHR')
                    HNR = st.text_input('HNR')
                    RPDE = st.text_input('RPDE')
                    DFA = st.text_input('DFA')
                    spread1 = st.text_input('spread1')
                    spread2 = st.text_input('spread2')
                    D2 = st.text_input('D2')
                    PPE = st.text_input('PPE')
                        
                        
                    #Code for prediction
                    parkinsons_diagnosis = ''
                        
                    #Creating a button for prediction
                        
                    if st.button('Parkinsons Test Result'):
                            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
                            
                            if (parkinsons_prediction[0]==1):
                                parkinsons_diagnosis = 'The person is suffering from Parkinsons disease'
                                
                            else:
                                parkinsons_diagnosis = 'The person is Not suffering from Parkinsons disease'
                                
                                
                    st.success(parkinsons_diagnosis)
                    
                        
    
    
    

                 
                

        except  :
            st.warning("enter valid values")
    else:
        st.warning("Please login or sign up to access the this section.")
        
try:
    if Selected == "Account":
        import streamlit as st
        from streamlit_option_menu import option_menu
        import base64
        import streamlit as st
        import plotly.express as px

        def add_bg_from_local(image_file):
         with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            st.markdown(
                        f"""
                            <style>
                            .stApp {{
                                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                                background-size: cover
                            }}
                            </style>
                            """,
                            unsafe_allow_html=True
                            )
        add_bg_from_local('contact_us_2.jpg')
        
        import firebase_admin
        from firebase_admin import firestore
        from firebase_admin import credentials
        from firebase_admin import auth

        if not firebase_admin._apps:
            cred = credentials.Certificate("disease-prediction-5d958-242c417d5396.json")
            firebase_admin.initialize_app(cred)   

        st.title("Create your Account")

        if 'username' not in st.session_state:
            st.session_state.username = ''
        if 'useremail' not in st.session_state:
            st.session_state.useremail = ''

        def f():
            try:
                user = auth.get_user_by_email(email)
                print(user.uid)
                st.session_state.username = user.uid
                st.session_state.useremail = user.email

                # Set user_authenticated to True upon successful login
                st.session_state.user_authenticated = True

                st.session_state.signedout = True
                st.session_state.signout = True
            except:
                st.warning('Login Failed')

        def t():
            st.session_state.signout = False
            st.session_state.signedout = False
            st.session_state.username = ''
            st.session_state.useremail = ''

            # Set user_authenticated to False upon sign-out
            st.session_state.user_authenticated = False

        if "signedout" not in st.session_state:
            st.session_state["signedout"] = False
        if 'signout' not in st.session_state:
            st.session_state['signout'] = False

        if not st.session_state["signedout"]:
            choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')

            if choice == 'Sign up':
                username = st.text_input("Enter your unique username")

                if st.button('Create my account'):
                    user = auth.create_user(email=email, password=password, uid=username)

                    st.success('Account created successfully!')
                    st.markdown('Please Login using your email and password')
                    st.balloons()
            else:
                st.button('Login', on_click=f)

        #if st.session_state.signout:
        #  st.text('Name ' + st.sess
        if st.session_state.signout:
                    st.text('Name '+st.session_state.username)
                    st.text('Email id: '+st.session_state.useremail)
                    st.button('Sign out', on_click=t) 
except:
    print("Error Occured")                    
            
if Selected == "Contact Us":
    import streamlit as st
    st.header(":mailbox: Get In Touch With us!")


    contact_form = """
                <form action="https://formsubmit.co/rahil.apsit.5426@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required>
                    <input type="email" name="email" placeholder="Your email" required>
                    <textarea name="message" placeholder="Your message here"></textarea>
                    <button type="submit">Send</button>
                </form>
                """

    st.markdown(contact_form, unsafe_allow_html=True)

                # Use Local CSS File
    def local_css(file_name):
                    with open(file_name) as f:
                        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("Style.css")
if Selected=="About Us":
            

        import base64
        import streamlit.components.v1 as components
        import pandas as pd
        from PIL import Image
        import random
        import string
        import sklearn


        hide_menu_style = """
                        <style>
                        #MainMenu {visibility: hidden; }
                        footer {visibility: hidden;}
                        </style>
                        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)
        def add_bg_from_local(image_file):
                    with open(image_file, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read())
                    st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                    )
        add_bg_from_local('ab.jpg')
    

# Page title and description
        st.header('About Us')
        st.markdown('Welcome to our platform for advanced disease prediction.', unsafe_allow_html=True)

            # About Us section
        

        st.write(
                "At Curify, we are dedicated to improving healthcare through advanced disease prediction. "
                "Our team of passionate researchers, data scientists, and healthcare professionals has come together to develop a state-of-the-art system "
                "that aims to revolutionize the way diseases are detected and managed.",
                unsafe_allow_html=True
            )

        st.subheader('Our Mission')
        st.write(
                "- To provide accessible, affordable, and accurate disease prediction for everyone.\n"
                "- To empower individuals with the knowledge to take proactive steps toward better health.\n"
                "- To assist healthcare providers in delivering more personalized and effective care.",
                unsafe_allow_html=True
            )
        

        st.write(
                "Join us on our journey to make healthcare more proactive and personalized. "
                "Together, we can make a significant impact on the future of healthcare. Thank you for choosing us "
                "as your trusted partner in disease prediction.",
                unsafe_allow_html=True
            )

