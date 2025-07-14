
from dotenv import load_dotenv 
load_dotenv() 
import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash") 

def my_output(query):
    response = model.generate_content(query) 
    return response.text 

#### UI Development using streamlit 

st.set_page_config(page_title="TechAI")
st.header("TechAI") 
input = st.text_input("Input " , key = "input")  
submit = st.button("Submit Query") 

if submit :
    response = my_output(input) 
    st.subheader("After deep thinking... here’s the answer:")
    st.write(response)
