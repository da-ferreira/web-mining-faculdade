from flask import Flask, jsonify
import pandas as pd 

app = Flask(__name__)

# contruindo as funcionalidades
@app.route('/')
def hello_word():
    return "A aplicação está no ar"

@app.route('/pegarvendas/')
def pegarvendas():
    dados = pd.read_csv('./advertising.csv')
    ttvendas = dados['Sales'].sum()
    resposta = {'total_vendas':ttvendas}
    return jsonify(resposta)

# dados = pd.read_csv('./advertising.csv')
# ttvendas = dados.Vendas.sum()
# print(ttvendas)


app.run()