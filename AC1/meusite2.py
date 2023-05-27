from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'Oi, bem vindo ao nosso site! <br> Aqui, você não perde seu tempo. Basta navegar até a rota hora ;) </br>' 

data = datetime.today()
data2 = str(data)[0:10]
horae = str(data)[11:19]

@app.route('/hora/') 
def hora(): 
    
    return '<p>Hoje é dia {}</p> <p>e são exatamente: {}</p>'.format(data2, horae)
    
@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return "Bem vindo {}".format(nome_usuario) 

if __name__ == "__main__": 
    app.run(debug=True) 

