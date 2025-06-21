from flask import Flask, render_template, request
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topsis', methods=['POST'])
def topsis():
    
    matrix = request.form.get('matrix')
    weights = request.form.get('weights') # Ponderi ale criteriilor (suma = 1)
    types = request.form.get('types')

    # ----- TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) -----
    
    rows = matrix.strip().split('\n')
    matrix = np.array([[float(x) for x in row.split(',')] for row in rows])

    weights = np.array([float(w) for w in weights.split(',')])
    types = [int(t) for t in types.split(',')]
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

    return render_template('index.html', scores=R.tolist())

if __name__ == '__main__':
    app.run(debug=True)
