import pandas as pd
df = pd.read_csv("./ejejejej.csv")
# df.to_excel("./eeeeeeeeeeeeeeeee.xlsx")
df.drop(columns=["Unnamed: 0"], inplace=True)
print(df)
df.to_json("./cleandata.json",orient="records")
# print(df.isnull().sum(axis=0))