from helper import *

import pandas as pd

db_host = "gupeveno.mysql.db.hostpoint.ch"
db_name = "gupeveno_backendAzolla"
db_user = "gupeveno_azbeu"
db_password = "backend_GoNet0"

db_connection = connect_database(db_host, db_name, db_user, db_password)

df = read_table("transactions", db_connection)

print(df.info())