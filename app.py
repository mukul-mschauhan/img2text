import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
# Load the Environment
load_dotenv()
# Configure the GenAI Secret Key
genai.configure(api_key = os.getenv("GOOGLE_API-KEY"))

##Designing the Page
st.title("Image to Text Application")
user_input = st.text_input("Input Prompt:")
uploaded_file = st.file_uploader("Upload the Image...", 
                                 type = ["jpg", "jpeg", "png"])

# Display the Image on the Page
from PIL import Image
img = ""
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption = "Uploaded_Image", use_column_width=True)
    
## Function for Evaluating the Image and Annotating it.
def gemini_response(user_input, img):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if user_input!="":
        response = model.generate_content([user_input, img])
    else:
        response = model.generate_content(img)
    return response.text

# Create Submit Button and Map the GenAI Function
submit = st.button("Submit")

if submit:
    response = gemini_response(user_input=user_input, img=img)
    st.subheader("The Response is: ")
    st.write(response)


#st.sidebar.title("Model Diagnostics")
#st.sidebar.markdown("Click to know more")
#univ_analysis = st.sidebar.button("Univariate Analysis")

#if univ_analysis:
    #st.write("This is Working")





