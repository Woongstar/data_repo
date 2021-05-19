import pandas as pd

# df = pd.read_csv("./ejejejej.csv")
df = pd.read_json("./cleandata.json")
# df.drop(columns=["Unnamed: 0"],inplace=True)
df.rename(columns={"longtitude":"longitude"},inplace=True)
df.to_json("./cleandata.json",orient="records")
print(df)