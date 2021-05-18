import pandas as pd

# jejusi = pd.read_json("./cleanhousejejuchange.json")
# # print(jejusi)
# sequipo = pd.read_json("./cleanhouseseyqyupochange.json")
# # print(sequipo)
# jejuall = pd.concat([jejusi, sequipo], ignore_index=True)

jejuall = pd.read_json("./jejucleanhousedata.json")

jejuall["type"] = "clean"
# jejuall.to_json("./jejucleanhousedata.json",orient='records')

# print(jejuall.columns)
# print(jejuall)
# jejujson = jejuall.to_json(orient='records')
recycle = pd.read_json("./jejurecyclejson.json")
recycle = recycle[["address","location","latitude","longtitude","type"]]
merge = pd.concat([jejuall, recycle], ignore_index=True)

merge.to_json("./cleandata.json", orient="records")
# print(merge)

# print(jejuall)
# print(recycle)



# print(jejujson)
# print(jejuall)