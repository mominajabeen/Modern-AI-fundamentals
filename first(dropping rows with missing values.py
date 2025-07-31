import pandas as pd
data = pd.read_csv('industry.csv')
data = data.dropna() # dropping rows with missing values