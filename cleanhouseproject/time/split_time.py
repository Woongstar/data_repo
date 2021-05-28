import pandas as pd

df=pd.read_json("./cleandata.json")

# print(df)
# df['grp'] = df.id.str.split('_').str[0]

# a = df["time"].split("~")[0]
df["timeStart"] = df.time.str.split("~").str[0]
df["timeEnd"] = df.time.str.split("~").str[1]

df.to_json("./cleandatasplit.json",orient='records')
print(df)