from dotenv import load_dotenv
load_dotenv() #load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

##configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Correcting the model name and response handling
def get_gemini_response(question, prompt):
    # Assuming the API expects a single string, concatenate prompt and question
    combined_input = prompt[0] + " " + question  # Concatenate the prompt and the question
    model = genai.GenerativeModel('gemini-pro')
    # Pass the combined string directly, without wrapping it into a list
    response = model.generate_content(combined_input)
    return response.text


# Corrected function for fetching rows from the database
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()  # Corrected fetching of rows
    conn.close()  # Removed commit on a read operation
    return rows



prompt = [
    """
    Imagine yourself as an advanced SQL query generator with expertise in the healthcare domain. You have been provided with a SQL database named `patient.db`, which contains a table called `PATIENT`. This table includes the following columns: PatientID, FirstName, LastName, DateOfBirth, Gender, Phone, Email, Address, City, State, ZipCode, EmergencyContactName, EmergencyContactPhone, and DateRegistered. Your task is to translate English questions into precise SQL queries to retrieve information from the `PATIENT` table.

    For example,
    - If asked, "How many patients are registered in the database?", you should generate the SQL query: SELECT COUNT(*) FROM PATIENT;
    - For a question like "Show me the details of female patients born after 1980," your SQL query should be: SELECT * FROM PATIENT WHERE Gender='F' AND DateOfBirth > '1980-01-01';
    - If the question is, "Find all patients from 'Anytown' and their contact details," then produce the SQL command: SELECT FirstName, LastName, Phone, Email FROM PATIENT WHERE City='Anytown';

    Remember, your responses should directly translate the English inquiries into SQL commands without the use of code formatting symbols (like ```) at the beginning or end, nor should the word 'sql' appear in your outputs. Aim to assist efficiently by converting complex questions into accurate SQL queries, enhancing data retrieval and analysis in the healthcare sector.
    """
]

##streamlit app

st.set_page_config(page_title = "I can retrieve any SQL Query")
st.header("Gemini App to Retrieve SQL Query")

question= st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

# Revised streamlit display code
if submit:
    response = get_gemini_response(question, prompt)
    st.write(response)  # Using st.write() for display
    data = read_sql_query(response, "patient.db")
    st.subheader("The response is:")
    for row in data:
        st.write(row)  # Displaying each row using st.write()








