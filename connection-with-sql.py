# First, make sure you have the library installed. You can install it using :- "pip install mysql-connector-python"
# Here's a simple Python program that connects to a MySQL server, fetches data, and displays it to the user
# Make sure to replace the placeholders (your_host, your_username, your_password, your_database, and your_table) with your actual MySQL server details and the SQL query you want to execute.
# This code connects to the MySQL server, executes a SELECT query, fetches the results, 
# and prints them. You can customize the code to display the data in a more user-friendly way,
# such as formatting it into a table or presenting it in a graphical user interface (GUI) if needed.

# Here is the code

import mysql.connector

# Define your MySQL database connection details
db_config = {
    "host": "your_host",
    "user": "your_username",
    "password": "your_password",
    "database": "your_database",
}

try:
    # Create a connection to the MySQL server
    conn = mysql.connector.connect(**db_config)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Execute a SQL query to fetch data from your database
    query = "SELECT * FROM your_table"
    cursor.execute(query)

    # Fetch all rows of the result
    result = cursor.fetchall()

    # Display the fetched data
    for row in result:
        print(row)  # You can format and display the data as needed

except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()

