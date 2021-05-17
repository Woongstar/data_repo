from geopy.geocoders import Nominatim
import pandas as pd
# import osmnx as ox
from geopy.geocoders import Nominatim
from pprint import pprint

app = Nominatim(user_agent='tutorial')
# location = app.geocode('남산타워')
# print(location[1][0])
# pprint(location)
# geolocoder = Nom
# dinatim(user_agent = 'South Korea`')

# def geocodinglat(address):
#     geo = geolocoder.geocode(address)
#     lat = geo.latitude
#     return lat
#
# def geocodinglong(address):
#     geo = geolocoder.geocode(address)
#     long = geo.longtitude
#     return long

# print(geocodinglat("신성마을길 8-9"))

#
df = pd.read_json("./recycledata.json")

# print(df.columns)
df["location"] = df["('location', '')"]
df["address"] = df["('address', '')"]
df.drop(columns=["('location', '')","('address', '')"], inplace=True)
df.to_json("./recycledata.json", orient="records")
# df["latitude"] = app.geocode(df["address"][1][0])
# df["longtitude"] = geocodinglong(df["address"])
# lat = app.geocode(df["address"])
# print(df)
# print(df.dtypes)

#
# for items in df["address"]:
#     try:
#         lat = app.geocode(items)
#         print("latitude : {}".format(lat[1][0]))
#         print("longtitude : {}".format(lat[1][1]))
#     except:
#         print("에러")
