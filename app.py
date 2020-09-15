import numpy as np
import pandas as pd
import streamlit as st
import pickle

pickle_in=open('classifier.pkl','rb')
lm=pickle.load(pickle_in)
def predictions(hours):
    predict=lm.predict([[hours]])
    return predict

def main():
    st.title("Student Score")
    html_temp="""
    <div style="background-color:blue;padding:10px">
    <h1 style="color:black;text-align:center;">Students Score</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    result=""
    hrs=st.number_input("Hours of Study")
    if st.button("Predict"):
        result=predictions(hrs)
    st.success(f'Output:{result}')
if __name__ == "__main__":
    main()