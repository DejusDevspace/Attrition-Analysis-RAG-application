import pandas as pd
import streamlit as st

def main():
    df = pd.read_csv("./data/HR-Employee-Attrition.csv")

    st.set_page_config(
        page_title="Analysis Chatbot",
        page_icon=":books:",
    )
    st.title("Attrition Analysis Chatbot")