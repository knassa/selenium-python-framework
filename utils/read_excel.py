import pandas as pd

file_path = 'test_data/sample.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')
print(df.head())
