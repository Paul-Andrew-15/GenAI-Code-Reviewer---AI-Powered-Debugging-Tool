import streamlit as st
import google.generativeai as ai

ai.configure(api_key="my api key")

sys_prompt = """You are a helpful AI Python code reviewer. 
                Students and Programmers will ask you doubts and ask you to debug the python code.
                You are expected to reply in as much detail as possible of the error and Provide the corrected code. 
                In case if a student provide any code outside the python code or any other concepts other than python code, 
                politely decline and tell them to provide code related to python only.
                In the output use header as Code review and explain the error, add two sub heading as bug report and Corrected code.
                Always include a helpful statement at the end saying that 
                'In case if your query is not resolved, feel free to click on this link:
                https://docs.python.org/3/"""

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("AI Python Code Reviewer")

user_input = st.text_area(label="Enter your Code", placeholder="Type your code here......")

btn_click = st.button("Debug!")

if btn_click:
    if user_input.strip():
        response = gemini_model.generate_content(user_input)
        st.write(response.text)
    else:
        st.warning("Please enter Python code before clicking 'Debug!'.")
