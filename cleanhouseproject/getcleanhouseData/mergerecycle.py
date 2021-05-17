import pandas as pd

jeju = pd.read_json("./recycledata.json")
seogui = pd.read_json("./recycledata1.json")
#
# seogui["location"] = seogui["('location', '')"]
# seogui["address"] = seogui["('address', '')"]
# seogui.drop(columns=["('location', '')","('address', '')"], inplace=True)
# seogui.to_json("./recycledata1.json", orient="records")

jeju["location"] = jeju["('location', '')"]
jeju["address"] = jeju["('address', '')"]
jeju.drop(columns=["('location', '')","('address', '')"], inplace=True)
jeju.to_json("./recycledata1.json", orient="records")

print(jeju)
print(seogui)

recycle = pd.concat([jeju, seogui], ignore_index=True)
recycle.to_json("./jejurecycledata.json",orient='records')
print(recycle)
