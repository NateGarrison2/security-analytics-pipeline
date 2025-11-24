import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import time

# Load environment variables from .env file
load_dotenv()

# Load database connection details from environment variables
DBUser = os.getenv("DBUser")
DBPassword = os.getenv("DBPassword")
DBHost = os.getenv("DBHost", "postgres")
DBPort = os.getenv("DBPort", "5432")
DBName = os.getenv("DBName", "siemdb")

# Create a database engine
engine = create_engine(f'postgresql+psycopg2://{DBUser}:{DBPassword}@{DBHost}:{DBPort}/{DBName}')

# Wait for the Postgres database to be ready
while True:
    try:
        with engine.connect() as connection:
            print("Postgres is ready to accept connections.")
            break
    except Exception as e:
        print("Postgres is not ready yet, retrying...")
        time.sleep(5)

# Load the cleaned SIEM events data
df = pd.read_csv('../data/cleaned_siem_events.csv')

# Ensure the schema exists and grant necessary permissions
with engine.begin() as connection:

    # Load the DataFrame into a PostgreSQL database table
    try:
        df.to_sql('siem_events', connection, schema='public', if_exists='replace', index=False)
        print(f'Data loaded into PostgreSQL schema "public" table "siem_events"')
    except Exception as e:
        print(f"Error loading data into database: {e}")

# Verify the data has loaded by querying for existing table(s)
with engine.connect() as connection:
    result = connection.execute(text("SELECT table_name, table_schema FROM information_schema.tables WHERE table_schema='public';"))
    print("Tables in schema:", result.fetchall())
