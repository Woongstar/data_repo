import requests, xmltodict, json
import pandas as pd

key = "Z6Tp4O27CyA2s3Eo23cuSyi8Uu1%2BhZiQa%2Fz%2BV%2F%2Bg57vtLn6P4fpAcMnHjxATQtGy3xMjwZa0KELrsp%2Bi6qgbVw%3D%3D"
url = "http://openapi.jejusi.go.kr/rest/cleanhouseinfoservice/getCleanHouseInfoList?ServiceKey={}&pageSize=2000".format(key)

content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict["rfcOpenApi"]["body"], ensure_ascii=False)
jsonObj = json.loads(jsonString)



for list in jsonObj["data"]["list"]:
    print(list)

file = open("./cleanhousjeju.json", "w+")
file.write(json.dumps(jsonObj["data"]["list"]))