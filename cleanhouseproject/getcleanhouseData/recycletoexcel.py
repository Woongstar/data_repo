import pandas as pd
# df = pd.read_json("./jejurecycledata.json")
# df.to_excel("./jejurecycleexcel.xlsx")
df = pd.read_csv("./jejurecycleexcelcsv.csv")

df.drop(columns=["Unnamed: 0"], inplace=True)
# print(df)
# df["type"]
df["type"]  = "recycle"
print(df.columns)
df.to_json("./jejurecyclejson.json", orient="records")
