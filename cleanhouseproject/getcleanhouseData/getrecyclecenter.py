import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.jeju.go.kr/nature/environment/recycle.htm"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"html.parser")

tables = soup.select('table')
table = tables[0]
table1 = tables[1]

# data_rows = soup.find("table",attrs={"class":"table dataTable"}).find("tbody").find_all("tr")
# for row in data_rows:
#     columns = row.find_all("td")
#     if len(columns) >=2:
#         continue
#     data = [column.get_text for column in columns]
#     print(data)
# print(data_rows)

#제주시 재활용센터 데이터
table_html = str(table)
recycle_list = pd.read_html(table_html)
recycledata = recycle_list[0]
# df = pd.DataFrame(recycle_list)

#서귀포시 재활용센터 데이터
table1_html = str(table1)
recycle_list1 = pd.read_html(table1_html)
recycledata1 = recycle_list1[0]
print(recycledata1["운영시간"])
# recycledata1.reset_index(drop=False, inplace=True)
# recycledata1.drop(columns=["읍면동","특수시책","위치","운영시간","운영개시일"], inplace=True)
# # print(recycledata1.columns)
# recycledata1["location"] = recycledata1["명칭"]
# recycledata1["address"] = recycledata1["도로명주소"]
# recycledata1.drop(columns=["명칭","도로명주소","index"], inplace=True)
# # print(recycledata1.columns)
# print(recycledata1)
#
# recycledata1.to_json("./recycledata1.json",orient='records')
#
#
# recycledata.drop(columns=["읍면동","특수시책","위치","운영시간","운영개시일"], inplace=True)
# recycledata["location"] = recycledata["명칭"]
# recycledata["address"] = recycledata["도로명주소"]
# recycledata.drop(columns=["명칭","도로명주소"], inplace=True)
# print(recycledata)
# recycledata.to_json("./recycledata.json",orient='records')
# print(type(recycledata))
# col_name = ['colname1', 'colname2',"colname3","colname4"]
# df = pd.DataFrame(recycle_list[0], columns=col_name)