import pandas as pd

df = pd.read_csv("./ejejejej.csv")
df.drop(columns=["Unnamed: 0"],inplace=True)
df.to_json("./cleandata.json",orient="records")
print(df)