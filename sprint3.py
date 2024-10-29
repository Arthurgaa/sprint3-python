"""
Arthur Galvão Alves - RM554462
Felipe Braunstein e Silva - RM554483
Jefferson Junior Alvarez Urbina - RM558497
Eduardo da Silva Lima - RM554804
"""

import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa matplotlib para visualização de dados

def exibir_boas_vindas() -> None:
    """Exibe uma mensagem de boas-vindas ao usuário."""
    print('*' * 60)
    print('* SEJA BEM-VINDO AO GERENCIADOR DE PILOTOS DA FORMULA E *')
    print('*' * 60)

def coletar_dados_pilotos() -> pd.DataFrame:
    """
    Coleta dados de pilotos da Fórmula E, incluindo nome, equipe, pontuação e corridas.

    Returns:
        pd.DataFrame: DataFrame contendo os dados dos pilotos.
    """
    pilotos = []
    while True:
        nome = input("Digite o nome do piloto (ou 'sair' para encerrar): ")
        if nome.strip().lower() == 'sair':
            break
        equipe = input("Digite o nome da equipe: ")

        pontuacao = []
        while True:
            try:
                pontuacao_input = input("Digite a pontuação do piloto (ou 'sair' para encerrar a inserção): ")
                if pontuacao_input.lower() == 'sair':
                    break
                pontuacao_val = int(pontuacao_input)
                if pontuacao_val < 0:
                    raise ValueError("A pontuação não pode ser negativa.")
                pontuacao.append(pontuacao_val)
            except ValueError as e:
                print(f"Entrada inválida: {e}. Por favor, insira um número inteiro válido.")

        corridas = input("Digite as corridas em que o piloto participou (separadas por vírgula): ")
        corridas_tuple = tuple(corrida.strip() for corrida in corridas.split(','))

        pilotos.append({
            'Nome': nome,
            'Equipe': equipe,
            'Pontuação': pontuacao,
            'Corridas': corridas_tuple
        })

    return pd.DataFrame(pilotos)

def exibir_tabela_pilotos(df: pd.DataFrame) -> None:
    """
    Exibe uma tabela com os dados dos pilotos.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados dos pilotos.
    """
    print("\nTabela de Pilotos da Fórmula E:")
    print(df)

def gerar_grafico_pontuacao(df: pd.DataFrame) -> None:
    """
    Gera um gráfico de barras para comparar as pontuações totais dos pilotos.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados dos pilotos.
    """
    plt.figure(figsize=(10, 5))
    rotulos = [f"{row['Nome']} - {row['Equipe']}" for _, row in df.iterrows()]
    pontuacoes_totais = [sum(row['Pontuação']) for _, row in df.iterrows()]

    plt.bar(rotulos, pontuacoes_totais, color='skyblue')
    plt.xlabel('Pilotos e Equipes')
    plt.ylabel('Pontuação Total')
    plt.title('Comparação de Pontuação dos Pilotos da Fórmula E')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def main() -> None:
    """Função principal para executar o programa."""
    exibir_boas_vindas()
    df_pilotos = coletar_dados_pilotos()
    if not df_pilotos.empty:
        exibir_tabela_pilotos(df_pilotos)
        gerar_grafico_pontuacao(df_pilotos)
    else:
        print("Nenhum dado de piloto foi inserido.")

if __name__ == "__main__":
    main()

