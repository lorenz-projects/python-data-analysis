import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_host = "gupeveno.mysql.db.hostpoint.ch"
db_name = "gupeveno_backendAzolla"
db_username = "gupeveno_azbeu"
db_password = "backend_GoNet0"

db_connection_string = f"mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}"

db_engine = create_engine(db_connection_string)
db_connection = db_engine.connect()

query = text("SELECT * FROM transactions")

df = pd.read_sql(query, con=db_connection)

print(df.info())