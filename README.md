# Sprint 3 - Python

## Descrição do Projeto:
Este projeto é um gerenciador simples para coletar e visualizar dados sobre pilotos da Fórmula E. 
Os usuários podem inserir informações como nome, equipe, pontuações em corridas e visualizar uma tabela e um gráfico comparativo das pontuações.

## Funcionalidades:
- Coleta de Dados: O programa permite que os usuários insiram informações sobre pilotos, incluindo nome, equipe e pontuações.
- Exibição de Tabela: Após a coleta, os dados dos pilotos são exibidos em uma tabela.
- Gráfico de Comparação: Um gráfico de barras é gerado para comparar as pontuações totais dos pilotos.

## Tecnologias Utilizadas:
- Python: A linguagem de programação utilizada.
- Pandas: Biblioteca para manipulação e análise de dados.
- Matplotlib: Biblioteca para visualização de dados.

## Estrutura do Código
- coletar_dados_pilotos(): Função responsável pela coleta de dados dos pilotos.
- exibir_tabela_pilotos(df): Função que exibe a tabela de pilotos.
- gerar_grafico_pontuacao(df): Função que gera um gráfico de barras com a comparação das pontuações dos pilotos.
- main(): Função principal que controla o fluxo do programa.

## Como usar:
1. Instalação das Bibliotecas: Certifique-se de ter o Python instalado. Instale as bibliotecas necessárias com o seguinte comando:
   - pip install pandas matplotlib
2. Execução do Programa: Execute o arquivo Python. Você pode fazer isso no terminal:
   - python seu_arquivo.py
4. Interação:
   - Siga as instruções na tela para inserir o nome do piloto, nome da equipe e suas pontuações.
   - Para encerrar a entrada de dados, digite "sair".
   - Após a inserção, a tabela de pilotos será exibida e um gráfico comparativo será gerado.

## Integrantes:
- Arthur Galvão Alves - RM554462 
- Eduardo da Silva Lima - RM554804 
- Felipe Braunstein e Silva - RM554483
- Felipe do Nascimento Fernandes - RM554598
- Jefferson Junior Alvarez Urbina - RM558497
