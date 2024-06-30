import pandas as pd

df = pd.read_excel("./test_data/sample.xlsx", usecols=[0, 0])
print(df.iloc[0])