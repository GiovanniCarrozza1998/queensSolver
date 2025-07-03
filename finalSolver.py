import numpy as np
from copy import deepcopy

def trova_prima_soluzione_no_vertici(A):
    n = A.shape[0]
    soluzione_finale = None
    found = [False]  # usiamo una lista per mutabilità nel backtracking

    def no_vertices_adjacency(sol, r, c):
        adiacenti_diagonali = [
            (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)
        ]
        for rr, cc in adiacenti_diagonali:
            if 0 <= rr < n and 0 <= cc < n and sol[rr, cc] == 1:
                return False
        return True

    def backtrack(riga, soluzione, colonne_usate, colori_usati):
        if found[0]:
            return
        if riga == n:
            nonlocal soluzione_finale
            soluzione_finale = deepcopy(soluzione)
            found[0] = True
            return

        for col in range(n):
            colore = A[riga, col]
            if (col not in colonne_usate
                and colore not in colori_usati
                and no_vertices_adjacency(soluzione, riga, col)):
                soluzione[riga, col] = 1
                colonne_usate.add(col)
                colori_usati.add(colore)
                backtrack(riga + 1, soluzione, colonne_usate, colori_usati)
                soluzione[riga, col] = 0
                colonne_usate.remove(col)
                colori_usati.remove(colore)

    soluzione_iniziale = np.zeros((n, n), dtype=int)
    backtrack(0, soluzione_iniziale, set(), set())

    if soluzione_finale is not None:
        print(f"Soluzione trovata:\n{soluzione_finale}")
        return soluzione_finale
    else:
        print("Nessuna soluzione trovata.")
        return None
"""
# --- ESEMPIO USO: (modifica A come necessario!) ---
A = np.array([[3, 3, 3, 3, 3, 4, 4, 4],
 [3, 2, 2, 2, 4, 4, 4, 1],
 [2, 2, 2, 2, 2, 2, 1, 1],
 [2, 2, 2, 5, 2, 2, 2, 1],
 [2, 2, 2, 5, 2, 2, 2, 6],
 [2, 5, 5, 5, 2, 6, 6, 6],
 [2, 7, 7, 7, 2, 2, 2, 8],
 [7, 7, 7, 8, 8, 8, 8, 8]])
_ = trova_prima_soluzione_no_vertici(A)"""