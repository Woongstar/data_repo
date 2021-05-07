import pandas as pd
df = pd.read_csv ('./seuguipoCleanhouse.csv')
df.to_json (r'./seuguipoCleanhouse.json')