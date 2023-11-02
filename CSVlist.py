import pandas as pd

dataframe = pd.read_csv('SENARAI.PERUNDANGAN.csv', usecols=['AGENSI_xn', 'name'])
dataframe.columns = ['AGENCY', 'Ordinance']

print(dataframe.head())

print(dataframe['AGENCY'].iloc[0])
print(dataframe['Ordinance'].iloc[0])

print(dataframe['AGENCY'].iloc[1])
print(dataframe['Ordinance'].iloc[1])


print(dataframe.shape[0])

#print('Do you want to make changes (yes/no) ? : ')
user_input = ''

while user_input not in ('yes', 'no'):
    
    user_input = input('Do you want to make changes (yes/no) ? : ')
    
    if user_input.lower() == 'yes':
        print('yes')
        # ask for ic; then get the xpath of the profile email text field
        break
    if user_input.lower() == 'no':
        print('no')
        # end session / back to home portal
        break
    else:
        print('please type yes or no')
        #user_input = input('Do you want to make changes (yes/no) ? : ')
