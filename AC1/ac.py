from flask import Flask, jsonify, request
import pandas as pd

# Integrantes do grupo:
# David Ferreira de Almeida, RA: 1904024
# Matheus de Jesus Oliveira RA: 1903603

app = Flask(__name__)


@app.route('/')
def hello_word():
    return "Bem vindo a nossa aplicação. Vá para a rota /jogo/ para ver os jogos."

# Exercício 1: 
#   rota /jogo/: 
#   vai retornar para o usuário um dicionário com o nome do time da casa, 
#   nome do time visitante, placar e data da partida de todos os jogos!

@app.route('/jogo/')
def game():
    data = pd.read_csv('./futebol.csv', sep=";")
    result = []

    for index, row in data.iterrows():
        result.append({
            'Time da casa': str(row['home_team_name']),
            'Time visitante': str(row['away_team_name']),
            'Placar': '',
            'Data da partida de todos os jogos': str(row['date_GMT'])
        })
    
    return jsonify(result)

# Exercício 2: 
#   rota /casa/: 
#   vai retornar para o usuário um dicionário de dicionários (ou 3 dicionários diferentes,
#   pode ser em 3 rotas diferentes se você achar melhor) de 3 times da sua escolha que mostre nome do time, 
#   quantidade de gols totais e contagem de jogos.

@app.route('/casa/')
def home_team():
    data = pd.read_csv('./futebol.csv', sep=";")
    teams = ['São Paulo', 'Goiás', 'Cuiabá']
    result = {}

    for team in teams:
        result[team] = {
            'Quantidade de gols': str(data.loc[data['home_team_name'] == team, 'home_team_goal_count'].sum() + 
                                      data.loc[data['away_team_name'] == team, 'away_team_goal_count'].sum()),
            'Contagem de jogos': str(data['home_team_name'].value_counts()[team] + data['away_team_name'].value_counts()[team])
        }

    return jsonify(result)

# Exercício 3:
#   rota /juizes/: 
#   vai retornar um dicionário com a quantidade de jogos por juiz

@app.route('/juizes/')
def referees():
    data = pd.read_csv('./futebol.csv', sep=";")
    result = []

    referees = data['referee'].value_counts()

    for index, referee in referees.iteritems():
        result.append({
            'Nome do juiz': index,
            'Quantidade de jogos': referee
        })

    return jsonify(result)

app.run(debug=True)
