from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return render_template('homepage.html') 

@app.route('/hora/') 
def hora(): 
    data = datetime.today()
    data2 = str(data)[0:10]
    horae = str(data)[11:19]
    return render_template('hora.html').format(data2, horae)
    
@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario) 

if __name__ == "__main__":
    app.run(debug=True)
