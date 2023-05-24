import pandas as pd
from scipy.stats import chi2_contingency

# Create a DataFrame with your data
data = {
    'Line': ['Darmor', 'DW001', 'DW002', 'DW004', 'DW005', 'DW019', 'DW022', 'DW023', 'DW024', 'DW026', 'DW028',
             'DW030', 'DW031', 'DW032', 'DW033', 'DW034', 'DW037', 'DW044', 'DW045', 'DW050', 'DW053', 'DW054',
             'DW056', 'DW061', 'DW067', 'DW069', 'DW075', 'DW078', 'DW080', 'DW084', 'DW089', 'DW092', 'DW097',
             'DW098', 'DW099', 'DW105', 'DW108', 'DW115', 'DW116', 'DW120', 'DW122', 'DW124', 'DW125', 'DW126',
             'DW134', 'DW139', 'DW146', 'DW147', 'DW149', 'DW155', 'DW157', 'DW163', 'DW164', 'DW166', 'DW167',
             'DW168', 'DW172', 'DW174', 'DW176', 'DW178', 'DW179', 'DW181', 'Westar'],
    'CSII': [22, 29, 100, 16, 100, 74, 97, 12, 36, 95, 67, 98, 32, 97, 84, 100, 8, 23, 25, 34, 31, 100, 57, 100, 31,
             27, 49, 95, 61, 100, 10, 21, 100, 21, 61, 94, 28, 100, 27, 100, 100, 88, 62, 100, 100, 36, 27, 20, 64, 96,
             29, 20, 100, 20, 18, 31,10,33,21,100,37,100,100],

    'Rlm9': ['+', '+', '-', '+','-', '+', '-', '+', '+', '-', '+', '-', '+', '-', '-', '-',
             '+', '+', '+', '+','+', '+', '+', '-', '+', '+', '+', '-','-', '-', '+', '+',
             '-', '+', '+', '-', '+', '-','+', '-', '-','-', '+','-', '+', '+', '+', '+',
             '+', '-', '+', '+', '+', '+', '+', '-', '+', '+', '+', '-', '+', '-','-']
}

df = pd.DataFrame(data)

# Create a contingency table
contingency_table = pd.crosstab(df['CSII'], df['Rlm9'])

# Perform the chi-square test
chi2, p_value, _, _ = chi2_contingency(contingency_table)

# Print the results
print("Chi-square test results:")
print("Chi-square value:", chi2)
print("p-value:", p_value)




#Convert numerical values to categorical values before performing a chi-square test. 


import pandas as pd
from scipy.stats import chi2_contingency

# Create a DataFrame with numerical and categorical variables
data = {
    'Numerical': [100, 95, 20, 15, 98, 10, 100, 65, 10, 15],
    'Category': ['R', 'R', 'S', 'S', 'R', 'S','R', 'R','S','S']
}

df = pd.DataFrame(data)

# Convert numerical values to categorical by creating bins
bins = [0, 50, 100]  # Define the bin boundaries
labels = ['Susceptible', 'Resistant']  # Define the labels for each bin

df['Numerical_Category'] = pd.cut(df['Numerical'], bins=bins, labels=labels)

# Create a contingency table
contingency_table = pd.crosstab(df['Numerical_Category'], df['Category'])

# Perform the chi-square test
chi2, p_value, _, _ = chi2_contingency(contingency_table)

# Print the results
print("Chi-square test results:")
print("Chi-square value:", chi2)
print("p-value:", p_value)
