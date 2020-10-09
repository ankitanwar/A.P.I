import os 

user="ankit"
password="Ankit123"
host="postgres"
database="example"
port=5432


DATABASE_CONNECTION_URI=DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'