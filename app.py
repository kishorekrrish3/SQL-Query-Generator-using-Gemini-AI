import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get API key from environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-002')

def main():
    st.set_page_config(page_title="SQL Query Generator using Gemini AI", page_icon=":robot:")

    st.markdown(
        """
        <div style="text-align:center;">
            <h1>SQL Query Generator</h1>
            <h3>I can generate SQL queries for you!</h3>
            <h4>With Explanation as well!!!</h4>
            <p>This tool is a simple tool that allows you to generate SQL queries based on your prompts.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    text_input = st.text_area("Enter your Query here in plain English:")

    submit = st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template = f"""
                Create a SQL query snippet using the below text:
                ```
                    {text_input}
                ```
                NO PREAMBLE and I just want a SQL query.
            """

            response = model.generate_content(template)
            sql_query = response.text.strip().lstrip("```sql").rstrip("```")

            expected_output = f"""
                What would be the expected response of this SQL query snippet:
                ```
                    {sql_query}
                ```
                Provide sample tabular Response with no explanation and NO PREAMBLE:
            """

            eoutput = model.generate_content(expected_output).text

            explanation = f"""
            Explain this SQL Query:
            ```
                {sql_query}
            ```
            Please provide with simplest of explanation:
            """

            explanation = model.generate_content(explanation).text

        with st.container():
            st.success("SQL Query Generated Successfully! Here is your Query Below:")
            st.code(sql_query, language="sql")

            st.success("Expected Output of this SQL Query will be:")
            st.markdown(eoutput)

            st.success("Explanation of this SQL Query:")
            st.markdown(explanation)

if __name__ == "__main__":
    main()
