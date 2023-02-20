import pandas as pd
import pandas_profiling as pp

try:
	df = pd.read_csv('gupeveno_backendAzolla_transactions.csv')
except:
	print("File was not found");
	quit();

pp.ProfileReport(df)
