import streamlit as st

# Page title and styling
st.title("Academic Navigator using smart chatbot system")
st.markdown(
    """
    <style>
        .container {
            width: 300px;
            padding: 16px;
            background-color: white;
            margin: 0 auto;
            border: 1px solid black;
            border-radius: 4px;
        }
        input[type='text'], input[type='password'], select {
            width: calc(100% - 30px);
            padding: 15px;
            margin: 5px 0 22px 0;
            border: none;
            background: #f1f1f1;
        }
        input[type='text']:focus, input[type='password']:focus, select:focus {
            background-color: #ddd;
            outline: none;
        }
        .registerbtn {
            background-color: #4CAF50;
            color: white;
            padding: 16px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
            opacity: 0.9;
        }
        .registerbtn:hover {
            opacity:1;
        }
        .title {
            text-align: center;
            margin-bottom: 20px;
            font-size: 24px;
            font-weight: bold;
            color: #333;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        #group-of-study {
            display: none;
        }
    </style>
    """
)

# Sign up form
with st.container():
    st.header("Sign up")
    st.write("Please fill in this form to create an account.")
    st.markdown("---")
    
    # Input fields
    name = st.text_input("Name", required=True)
    dob = st.date_input("Date of Birth", required=True)
    city = st.selectbox("City", ["Ariyalur", "Chengalpattu", "Chennai"], required=True)
    standard = st.radio("Standard", ["10th", "12th", "ITI"], index=0)
    
    if standard == "12th":
        st.markdown("<b>Group of Study</b>", unsafe_allow_html=True)
        group = st.selectbox("Group of Study", ["Arts", "Pure Science", "Computer Application", "Bio mathematics", "Computer Biology", "Commerce"], required=True)
    
    phone = st.text_input("Phone Number", required=True)
    email = st.text_input("Email", required=True)
    interests = st.text_input("Interests", required=True)
    password = st.text_input("Password", type="password", required=True)
    confirm_password = st.text_input("Confirm Password", type="password", required=True)
    
    # Submit button
    if st.button("Submit", key="register"):
        # Perform registration logic here (e.g., validate input, save to database)
        st.success("Registration successful!")

# Copyright notice
st.markdown("---")
st.markdown("&copy; gptc karur")
