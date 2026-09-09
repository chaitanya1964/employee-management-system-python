import os

import psycopg2

from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

        return connection

    except psycopg2.OperationalError:
        print("Unable to connect to the database.")
        print("Please make sure PostgreSQL is running.")
        return None