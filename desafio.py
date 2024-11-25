import csv

def ler_csv(nome_arquivo):
    with open('vendas.csv', mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        return [linha for linha in reader]
    
def processar_dados(dados):
    categorias = {}
    for item in dados:
        categoria = item["Categoria"]
        produto_info = {
        "Produto": item["Produto"],
        "Quantidade": int(item["Quantidade"]),
        "Venda": float(item["Venda"])
        }
        if categoria not in categorias:
            categorias[categoria] = []
        
        categorias[categoria].append(produto_info)

    return categorias

def calcular_vendas_categoria(categorias):
    totais_vendas = {}
    for categoria,produtos in categorias.items():
        total = 0
        for produto in produtos:
            total += produto["Quantidade"] * produto["Venda"]
        totais_vendas[categoria] = total
    return totais_vendas

def main():
    nome_arquivo = 'vendas.csv'
    dados_brutos = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_vendas_categoria(dados_processados)
    for categoria, total in vendas_categoria.items():
        print(f'{categoria}: ${total}')

if __name__ == '__main__':
    main()