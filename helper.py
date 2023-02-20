import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

def connect_database(db_host, db_name, db_user, db_password):

	db_connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

	db_engine = create_engine(db_connection_string)
	db_connection = db_engine.connect()

	return db_connection


def read_table(table, db_connection):

	query = text(f"SELECT * FROM {table}")
	df = pd.read_sql(query, con=db_connection)

	return df
