import pandas as pd
df = pd.read_json("./jejurecycledata.json")
df.to_excel("./jejurecycleexcel.xlsx")
