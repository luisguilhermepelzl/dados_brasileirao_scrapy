import json

with open('brasileirao_dados.json', 'r') as f:
    json_data = json.load(f)

for jogo in json_data:
    jogo['rodada'] = (jogo['jogo_index'] // 10) + 1

for jogo in json_data:
    resultado = jogo['resultado'].split(' x ')
    if len(resultado) == 2:
        jogo['resultado_mandante'] = resultado[0]
        jogo['resultado_visitante'] = resultado[1]
    else:
        print(f"Erro: Resultado inválido para o jogo {jogo['jogo_index']}.")

grupos_por_rodada = {}
for jogo in json_data:
    rodada = jogo['rodada']
    if rodada not in grupos_por_rodada:
        grupos_por_rodada[rodada] = []
    grupos_por_rodada[rodada].append(jogo)

with open('brasileirao_dados_modificado.json', 'w') as f:
    json.dump(json_data, f, indent=4)