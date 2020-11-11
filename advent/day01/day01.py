import pandas as pd

df=pd.read_csv('day1.txt', sep='\n', names=["weights"])

df['fuels'] = (df['weights']//3)-2

total = df['fuels'].sum()

print(total)

#3401852
