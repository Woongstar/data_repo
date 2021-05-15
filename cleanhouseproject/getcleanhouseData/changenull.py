import pandas as pd

df = pd.read_json("./jejucleanhousedata.json")
# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_columns',None)
# nulldata = df["location"].isnull
df.fillna({'location':df["address"]},inplace=True)

print(df["location"].isnull().sum(axis=0))
# print(df["location"].isnull)
df.to_json("./jejucleanhousedata.json",orient='records')
df.info()
