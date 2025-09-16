import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Load database connection details from environment variables
DBUser = os.getenv("DBUser")
DBPassword = os.getenv("DBPassword")
DBHost = os.getenv("DBHost", "localhost")
DBPort = os.getenv("DBPort", "5432")
DBName = os.getenv("DBName", "siemdb")

# Create a database engine
engine = create_engine(f'postgresql+psycopg2://{DBUser}:{DBPassword}@{DBHost}:{DBPort}/{DBName}')

# Load the cleaned SIEM events data
df = pd.read_csv('../data/cleaned_siem_events.csv')

# Load the DataFrame into a PostgreSQL database table (or print error if it fails)
try:
    df.to_sql('siem_events', engine, if_exists='replace', index=False)
    print('Data loaded into PostgreSQL database table "siem_events"')
except Exception as e:
    print(f"Error loading data into database: {e}")