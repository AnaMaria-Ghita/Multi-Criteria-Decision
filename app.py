from flask import Flask, render_template, request # pyright: ignore[reportMissingImports]
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topsis', methods=['POST'])
def topsis():

    nume_criterii = request.form.getlist('criteriu_nume[]')
    ponderi = list(map(float, request.form.getlist('criteriu_pondere[]')))
    tipuri = list(map(int, request.form.getlist('criteriu_tip[]')))  # 0 = cost, 1 = beneficiu
    nume_alternative = request.form.getlist('alternativa_nume[]')
    valori_criterii = list(map(float, request.form.getlist('valoare_criterii[]')))

    nr_criterii = len(nume_criterii)
    nr_alternative = len(nume_alternative)

    # ----- TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) -----

    matrix = np.array(valori_criterii).reshape((nr_alternative, nr_criterii))
    weights = np.array(ponderi)
    types = tipuri
    # Tip criteriu: 0 = cost, 1 = beneficiu
    
    # ----- Algoritm -----

    # Normalizare vectoriala (Euclidiana)
    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    
    # Matricea consecintelor ponderate
    weighted_matrix = norm_matrix * weights

    # Solutia idala pozitiva si negativa
    poz_ideal = np.zeros(weighted_matrix.shape[1])
    neg_ideal = np.zeros(weighted_matrix.shape[1])

    for i in range(weighted_matrix.shape[1]):
        if types[i] == 1:  # beneficiu
            poz_ideal[i] = weighted_matrix[:, i].max()
            neg_ideal[i] = weighted_matrix[:, i].min()
        else:  # cost
            poz_ideal[i] = weighted_matrix[:, i].min()
            neg_ideal[i] = weighted_matrix[:, i].max()

    # Distanta euclidiana fata de solutiile ideale
    d_poz_ideal = np.sqrt(((weighted_matrix - poz_ideal) ** 2).sum(axis=1))
    d_neg_ideal = np.sqrt(((weighted_matrix - neg_ideal) ** 2).sum(axis=1))

    # Apropierea relativa fata de solutia ideala
    R = d_neg_ideal / (d_poz_ideal + d_neg_ideal)

    rezultate = list(zip(nume_alternative, R.tolist()))
    rezultate.sort(key=lambda x: x[1], reverse=True)

    return render_template('index.html', rezultate=rezultate)

if __name__ == '__main__':
    app.run(debug=True)
