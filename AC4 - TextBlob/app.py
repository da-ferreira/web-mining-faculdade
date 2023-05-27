from flask import Flask, jsonify
import pandas as pd
from flask import render_template
from flask import request
from funcoes import *
import plotly
import plotly.express as px
import json

app = Flask(__name__, static_folder='./templates/assets/')


@app.route("/", methods=["GET", "POST"])
def hello_word():
    if request.method == "POST":
        var_name = request.form.get("fname")
        dict_ = {"0": {"frase": var_name}}
        teste = pd.DataFrame.from_dict(dict_, orient="index")
        teste.to_csv("teste.csv", sep=";", index=True)
        dados = pd.read_csv("./teste.csv", sep=";")
        frase = dados.frase.loc[0]
        string = traduz(frase)
        string = trata(string)
        dfim, pol, sub = previsao(string)
        print('aguif', pol)
            # fig = px.pie(dados, names='sentimento', values='polaridade')
            # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        if pol > 0.25:
            return render_template("positive.html", polaridade=pol)
        elif pol < -0.25:
            return render_template("negative.html", polaridade=pol)
        else:
            return render_template("neutro.html", polaridade=pol)

    return render_template("form.html")


app.run(debug=True)
