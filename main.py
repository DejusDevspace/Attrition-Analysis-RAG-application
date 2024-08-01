import pandas as pd
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents.agent_types import AgentType
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    df = pd.read_csv("./data/HR-Employee-Attrition.csv")

    st.set_page_config(
        page_title="Analysis Chatbot",
        page_icon=":books:",
    )
    st.title("Attrition Analysis Chatbot")
    st.subheader('Uncover Insights from Attrition Data!')
    st.markdown(
        """
        This chatbot was created to answer questions from a set of Attrition data.
        Ask a question and the chatbot will respond with appropriate Analysis.
        """
    )

    st.write(df.head())
    user_question = st.text_input("Ask your question about the data..")

    agent = create_csv_agent(
        GoogleGenerativeAI(model='gemini-1.5-flash'),
        "./data/HR-Employee-Attrition.csv",
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        allow_dangerous_code=True,
    )

    if user_question is not None:
        response = agent.invoke(user_question)
    # print(response)
    st.write(response['output'])

if __name__ == "__main__":
    main()