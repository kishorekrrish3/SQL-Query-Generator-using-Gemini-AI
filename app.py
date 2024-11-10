import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "Your API Key"         # REPLACE WITH YOUR GEMINI API KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


def main():
    st.set_page_config(page_title="SQL Query Generator using Gemini AI", page_icon=":robot:")
    st.markdown(
        """
        <div style="text-align:center;">
            <h1>SQL Query Generator</h1>
            <h3>I can generate SQL queries for you!</h3>
            <h4>Will Explanation as well!!!</h4>
            <p>This tool is a simple tool that allows you to generate SQL queries based on your prompts.</p>
        </div>
""",
unsafe_allow_html=True
    )

    text_input = st.text_area("Enter your Query here in plain English:")

    

    submit=st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template="""
                Create a SQL query snippet using the below text:
                ```
                    {text_input}
                ```
                NO PREAMBLE and I just want a SQL query.
            """
            formatted_template = template.format(text_input=text_input)

            response = model.generate_content(formatted_template)
            sql_query = response.text
            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
            # st.write(sql_query)

            expected_output = """
                What would be the expected response of this SQL query snippet:
                ```
                    {sql_query}
                ```
                Provide sample tabular Response with no explanation and NO PREAMBLE:
            """

            expected_output_formatted = expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_output_formatted)
            eoutput = eoutput.text
            # st.write(eoutput)

            explanation="""
            Explain this SQL Query:
            ```
                {sql_query}
            ```
            Please provide with simplest of explanation:
            """

            explanation_formatted = explanation.format(sql_query=sql_query)
            explanation = model.generate_content(explanation_formatted)
            explanation = explanation.text
            # st.write(explanation)

        # response = model.generate_content(text_input)

        # print(response.text)
        # st.write(response.text)

        with st.container():
            st.success("SQL Query Generated Successfully! Here is your Query Below:")
            st.code(sql_query, language="sql")
            
            st.success("Expected Output of this SQL Query will be:")
            st.markdown(eoutput)

            st.success("Explanation of this SQL Query:")
            st.markdown(explanation)

main()