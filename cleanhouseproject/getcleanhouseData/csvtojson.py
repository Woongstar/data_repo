import pandas as pd
df = pd.read_csv ('./seuguipoCleanhouse_utf8.csv')
df["latitude"] = df["위도"]
df["longtitude"] = df["경도"]
df["address"] = df["지번주소"]
df["location"] = df["단지명"]
print(df.columns)
df.drop(columns=['읍면동', '단지명', '설치위치', '클린하우스 형태', '도로명주소', '지번주소', '위도', '경도',
       '데이터기준일자'], inplace=True)
df=df[['address','location','latitude','longtitude']]
df.to_json("./cleanhouseseyqyupochange.json",orient="columns")

print(df)