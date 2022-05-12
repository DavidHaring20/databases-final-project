from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()


try: 
    # create configuration
    database_config = {
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME")
    }

    # create connection 
    database_connection = mysql.connector.connect(**database_config)

    # create cursor
    cursor = database_connection.cursor(dictionary=True)

    cursor.execute("""
    
    """)

    database_connection.commit()

except Exception as exception:
    print(exception)
    exit()
print("Completed")