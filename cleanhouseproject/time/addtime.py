import pandas as pd
df = pd.read_json("./cleandata.json")
df.to_excel("./cleandata.xlsx")