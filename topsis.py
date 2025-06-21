import numpy as np
import pandas as pd

# ----- TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) -----
alternatives = ['A1', 'A2', 'A3'] # variante decizionale
criteria = ['Preț', 'Consum', 'Putere'] # criterii de evaluare

# Tip criteriu: 0 = cost, 1 = beneficiu
criteria_types = [0, 0, 1]  # cost -> minimizate, beneficiu -> maximizare


# Matricea decizionala
decision_matrix = np.array([
    # pret, consum, putere
    [25000, 6.5, 90],    # A1
    [22000, 5.5, 80],    # A2
    [28000, 7.0, 100]    # A3
])

# Ponderi ale criteriilor (suma = 1)
weights = np.array([0.4, 0.3, 0.3])

# ----- Algoritm -----

# Normalizare vectoriala (Euclidiana)
norm_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))

# Matricea consecintelor ponderate
weighted_matrix = norm_matrix * weights

# Solutia idala pozitiva si negativa
poz_ideal = np.zeros(weighted_matrix.shape[1])
neg_ideal = np.zeros(weighted_matrix.shape[1])

for i in range(weighted_matrix.shape[1]):
    if criteria_types[i] == 1:  # beneficiu
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

# Clasament final
results = pd.DataFrame({
    'Alternativă': alternatives,
    'Scor TOPSIS': R
}).sort_values(by='Scor TOPSIS', ascending=False).reset_index(drop=True)

print(results)