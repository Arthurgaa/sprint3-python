"""
Arthur Galvão Alves - RM554462
Felipe Braunstein e Silva - RM554483
Jefferson Junior Alvarez Urbina - RM558497
Eduardo da Silva Lima - RM554804
"""

import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa matplotlib para visualização de dados

# Exibe uma mensagem de boas-vindas ao usuário
print('*' * 60)  # Imprime uma linha de asteriscos
print('* SEJA BEM-VINDO AO GERENCIADOR DE PILOTOS DA FORMULA E *')  # Mensagem de boas-vindas
print('*' * 60)  # Imprime outra linha de asteriscos

# Função para coletar dados dos pilotos
def coletar_dados_pilotos():
    pilotos = []  # Inicializa uma lista para armazenar os dados dos pilotos
    while True:  # Loop para coletar dados até que o usuário decida sair
        nome = input("Digite o nome do piloto (ou 'sair' para encerrar): ")  # Solicita o nome do piloto
        if nome.lower() == 'sair':  # Verifica se o usuário deseja encerrar a inserção
            break  # Sai do loop se o usuário digitar 'sair'
        equipe = input("Digite o nome da equipe: ")  # Solicita o nome da equipe do piloto
        pontuacao = []  # Inicializa uma lista para armazenar as pontuações do piloto
        while True:  # Loop para coletar as pontuações do piloto
            pontuacao_input = input("Digite a pontuação do piloto (ou 'sair' para encerrar a inserção): ")  # Solicita a pontuação
            if pontuacao_input.lower() == 'sair':  # Verifica se o usuário deseja encerrar a inserção de pontuação
                break  # Sai do loop se o usuário digitar 'sair'
            pontuacao.append(int(pontuacao_input))  # Adiciona a pontuação convertida para inteiro à lista

        corridas = input("Digite as corridas em que o piloto participou (separadas por vírgula): ")  # Solicita as corridas
        corridas_tuple = tuple(corridas.split(','))  # Converte a string de corridas em uma tupla

        # Adiciona um dicionário com os dados do piloto à lista
        pilotos.append({
            'Nome': nome,
            'Equipe': equipe,
            'Pontuação': pontuacao,
            'Corridas': corridas_tuple
        })

    return pd.DataFrame(pilotos)  # Retorna um DataFrame do pandas com os dados coletados

# Função para exibir a tabela de pilotos
def exibir_tabela_pilotos(df):
    print("\nTabela de Pilotos da Fórmula E:")  # Exibe um título para a tabela
    print(df)  # Imprime o DataFrame com os dados dos pilotos

# Função para gerar gráfico de comparação de pontuação
def gerar_grafico_pontuacao(df):
    plt.figure(figsize=(10, 5))  # Cria uma nova figura com tamanho 10x5 polegadas

    # Criando rótulos para o eixo x que incluem o nome e a equipe de cada piloto
    rotulos = [f"{row['Nome']} - {row['Equipe']}" for _, row in df.iterrows()]  # Formata os rótulos

    # Somando as pontuações para exibir no gráfico
    pontuacoes_totais = [sum(row['Pontuação']) for _, row in df.iterrows()]  # Calcula a pontuação total para cada piloto

    plt.bar(rotulos, pontuacoes_totais, color='skyblue')  # Cria um gráfico de barras com os rótulos e pontuações
    plt.xlabel('Pilotos e Equipes')  # Define o rótulo do eixo x
    plt.ylabel('Pontuação Total')  # Define o rótulo do eixo y
    plt.title('Comparação de Pontuação dos Pilotos da Fórmula E')  # Define o título do gráfico
    plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor visualização
    plt.grid(axis='y')  # Adiciona uma grade ao gráfico no eixo y
    plt.tight_layout()  # Ajusta o layout do gráfico
    plt.show()  # Exibe o gráfico

# Função principal
def main():
    df_pilotos = coletar_dados_pilotos()  # Coleta os dados dos pilotos
    if not df_pilotos.empty:  # Verifica se o DataFrame não está vazio
        exibir_tabela_pilotos(df_pilotos)  # Exibe a tabela de pilotos
        gerar_grafico_pontuacao(df_pilotos)  # Gera o gráfico de pontuação
    else:
        print("Nenhum dado de piloto foi inserido.")  # Mensagem caso nenhum dado tenha sido inserido

# Inicializa o programa
if __name__ == "__main__":  # Verifica se o arquivo está sendo executado diretamente
    main()  # Chama a função principal
