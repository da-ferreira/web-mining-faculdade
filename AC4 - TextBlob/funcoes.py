# importando uma das principais bibliotecas de tratamento de texto
import nltk

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
nltk.download("brown")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")

# importando o modelo que vamos usar para classificar a frase
from textblob import TextBlob

import pandas as pd


def traduz(frase):
    exemplo = TextBlob(frase)
    return exemplo.translate(from_lang="pt", to="en")


def trata(frase):
    text_tokens = word_tokenize(str(frase))
    tokens_without_sw = [
        word for word in text_tokens if not word in stopwords.words("portuguese")
    ]
    return (" ").join(tokens_without_sw)


def previsao(frase):
    exemplo = TextBlob(frase)
    polaridade = exemplo.sentiment[0]
    subjetividade = exemplo.sentiment[1]

    df = pd.DataFrame(
        [[frase, polaridade, subjetividade]],
        columns=["frase", "polaridade", "subjetividade"],
    )

    df["sentimento"] = "neutro"
    df.loc[df.polaridade < -0.25, "sentimento"] = "negativo"
    df.loc[df.polaridade > 0.25, "sentimento"] = "positivo"

    return df.to_json("dados.json", orient="columns"), polaridade, subjetividade
