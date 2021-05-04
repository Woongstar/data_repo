import pandas as pd
import json, openpyxl
def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, "sheet1")
    writer.save()

df = pd.read_json("./cleanhousjeju.json")

print(df.count())

save(df, "cleanhousejejusi.xlsx")