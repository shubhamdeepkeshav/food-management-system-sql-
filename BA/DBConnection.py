import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # your MySQL username
            password="password",  # your MySQL password
            database="rationdb"
        )
        if connection.is_connected():
            print("✅ Connected to MySQL database!")
        return connection
    except mysql.connector.Error as err:
        print("❌ Error:", err)
        return None
