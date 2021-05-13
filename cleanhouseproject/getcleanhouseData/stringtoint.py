import pandas as pd

data = pd.read_csv("./jejucleanhouseutf.csv")


# def save(df, filename):
#     writer = pd.ExcelWriter(filename)
#     df.to_excel(writer, "sheet1")
#     writer.save()
#
# save(data, "jejucleanhouse.xlsx")

# data["latitude"][806] == "33.3032512"
data["latitude"] = pd.to_numeric(data["latitude"])
# print(data["latitude"][807])
# print(data["latitude"][806])
# print(data.columns)
data.drop(columns=["Unnamed: 0"], inplace=True)
print(data)
# print(data.dtypes)
data.to_json("./jejucleanhousedata.json",orient="records")