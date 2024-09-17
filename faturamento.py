import json

# Função para carregar os dados do faturamento diário a partir de um arquivo JSON
def carregar_dados(filename):
    with open(filename, 'r') as file:
        dados = json.load(file)
    return dados["faturamento_diario"]

# Função para calcular menor, maior e dias acima da média
def calcular_faturamento(dados_faturamento):
    # Filtra os dias com faturamento maior que 0
    faturamentos_validos = [dia["valor"] for dia in dados_faturamento if dia["valor"] > 0]

    # Calcula o menor e o maior faturamento
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)

    # Calcula a média mensal dos dias com faturamento
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

    # Conta o número de dias com faturamento superior à média mensal
    dias_acima_da_media = sum(1 for valor in faturamentos_validos if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Carregar os dados do arquivo JSON
dados_faturamento = carregar_dados('faturamento.json')

# Calcula os resultados
menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(dados_faturamento)

# Exibe os resultados
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
