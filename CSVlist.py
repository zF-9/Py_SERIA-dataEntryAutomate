import pandas as pd

dataframe = pd.read_csv('SENARAI.PERUNDANGAN.csv', usecols=['AGENSI_xn', 'name'])
dataframe.columns = ['AGENCY', 'Ordinance']

print(dataframe.head())

print(dataframe['AGENCY'].iloc[0])
print(dataframe['Ordinance'].iloc[0])

print(dataframe['AGENCY'].iloc[1])
print(dataframe['Ordinance'].iloc[1])


print(dataframe.shape[0])
