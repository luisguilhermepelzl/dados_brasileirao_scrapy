import pandas as pd


df = pd.read_excel('links_calendarios.xlsx')

print(df)

json_data = df.to_json(orient="records")

caminho_arquivo_json = "dados.json"

with open(caminho_arquivo_json, "w") as json_file:
    json_file.write(json_data)

print("Arquivo JSON salvo")
