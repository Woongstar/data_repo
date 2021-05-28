import pandas as pd

df = pd.read_excel("./cleandata.xlsx",index_col=0)

df.to_json("./cleandata.json",orient='records')