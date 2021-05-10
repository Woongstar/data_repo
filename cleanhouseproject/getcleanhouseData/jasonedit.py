import json
import pandas as pd
import numpy as np
file_path = "./cleanhousjeju.json"
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

df=pd.DataFrame(json_data)
df["latitude"] = df["mapx"]
df["longtitude"] = df["mapy"]
# print(df.columns)
# print(df.head)
df.drop(columns=["mapx","mapy","dong"], inplace=True)

print(df)
# print(df.columns)

df.to_json("./cleanhousejejuchange.json",orient="columns")