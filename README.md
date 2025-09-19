# SQL Query Generator using Gemini AI \:robot:

This is a simple tool built with Streamlit and Google's Gemini AI to help you generate SQL queries from plain English text prompts. The tool interprets your input, generates an SQL query, provides a sample output, and explains the query.

## Features

* **SQL Query Generation**: Translates plain English prompts into SQL query snippets.
* **Sample Output**: Provides an expected result in a tabular format.
* **Explanation**: Delivers an easy-to-understand explanation of the generated SQL query.

---

## Getting Started

### Prerequisites

Make sure you have Python installed. You’ll also need to install Streamlit, Python-dotenv, and Google’s Gemini AI library.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/kishorekrrish3/SQL-Query-Generator-using-Gemini-AI.git
   cd SQL-Query-Generator-using-Gemini-AI
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   *(Or, if you prefer individually)*

   ```bash
   pip install streamlit
   pip install google-generativeai
   pip install python-dotenv
   ```

3. **Set Up API Key using .env**:

   * Create a `.env` file in the project root.
   * Add your Google API key as follows:

     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```
   * The app will automatically load this key using `python-dotenv`.

---

### Usage

1. **Run the Application**:

   ```bash
   streamlit run app.py
   ```

2. **Enter Your Query**:

   * In the Streamlit app, type a query in plain English into the text area, describing the SQL query you want.

3. **Generate**:

   * Click on "Generate SQL Query."
   * The application will display:

     * The generated SQL query.
     * A sample output in tabular form.
     * A simple explanation of the SQL query.

---

## Example Usage

* **Input Prompt**: "Retrieve all employee names and departments from the 'employees' table where the department is 'Sales'."

* **Generated SQL Query**:

  ```sql
  SELECT name, department FROM employees WHERE department = 'Sales';
  ```

* **Expected Output**:

  ```
  | name     | department |
  |----------|------------|
  | John Doe | Sales      |
  | Jane Roe | Sales      |
  ```

* **Explanation**:
  Retrieves employee names and departments for all records in the 'employees' table where the department matches 'Sales'.

---

## Contributing

Feel free to open issues or submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

### Acknowledgments

* **Streamlit** for providing an interactive web framework.
* **Google's Gemini AI** for enabling natural language SQL query generation.

---

Happy querying! \:robot:

