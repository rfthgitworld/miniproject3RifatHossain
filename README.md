### INF601 - Advanced Programming in Python
### Rifat Hossain   
### Mini Project 3
 



# Expense Tracker (Flask Application)

## Description

The Expense Tracker is a personal web-based financial management tool built with Python and the Flask framework. It is designed to help users track their personal finances by logging both **income** and **expense** transactions.

**Key Features:**
* **User Authentication:** Secure registration and login for individual users.
* **Transaction Tracking:** Record the amount, type (income/expense), category, and a note for each transaction.
* **Categorization:** Transactions are linked to categories (e.g., Housing, Food & Dining, Transportation) for easy organization.
* **Dashboard View:** A centralized view of all recorded transactions, complete with delete functionality (using a Bootstrap modal for confirmation).
* **SQLite Database:** Uses SQLite to persist data locally.

***

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Dependencies

First, it is highly recommended to set up a **Python Virtual Environment** to isolate project dependencies. 

*Note: If you're using Pycharm then skip step 1 and 2 below, as it can create and manage virtual environments automatically.*

1.  **Create a Virtual Environment** (e.g., named `venv`):

    ```bash
    python3 -m venv venv
    ```

2.  **Activate the Virtual Environment:**

    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows (Command Prompt):**
        ```bash
        .\venv\Scripts\activate
        ```

3.  **Install Required Libraries:** Install the necessary Python packages listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

### Initialize the Database

Before running the application, you must initialize the database. This step creates the required tables (`user`, `category`, and `transactions`) and populates the `category` table with default values.

1.  **Ensure you are in the project root directory** (where `app.py` is located).

2.  **Run the Flask initialization command:**

    ```bash
    flask --app app.py init-db
    ```

    You should see the message: `✅ Initialized the database.`

    *Note: This command connects to the SQLite database path defined in `expense_tracker/__init__.py` and runs the `schema.sql` script, clearing any previous data.*

***

### Program Execution

Once the database is initialized, you can start the development server.

1.  **Run the Flask Development Server:**

    ```bash
    flask --app app.py run
    ```

2.  **Access the Application:** Open your web browser and navigate to the local server address, typically:
    `http://127.0.0.1:5000/`

You can now register a new user and begin tracking your expenses.

***

## Authors

Rifat Hossain

***

## Version History

* 0.1
    * Initial Release

***

## Acknowledgments

* [Flask (Python web framework)](https://flask.palletsprojects.com/)
* [Bootstrap 5 (CSS framework for styling)](https://getbootstrap.com/)
* [SQLite (Database)](https://www.sqlite.org/index.html)
* [ChatGPT](https://chatgpt.com/share/69110877-29c0-8000-85f7-51d671ec8732)
