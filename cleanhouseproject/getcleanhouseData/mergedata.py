import pandas as pd

jejusi = pd.read_json("./cleanhousejejuchange.json")
# print(jejusi)
sequipo = pd.read_json("./cleanhouseseyqyupochange.json")
# print(sequipo)
jejuall = pd.concat([jejusi, sequipo], ignore_index=True)
jejujson = jejuall.to_json(orient='records')
jejuall.to_json("./jejucleanhousedata.json",orient='records')

print(jejujson)
# print(jejuall)