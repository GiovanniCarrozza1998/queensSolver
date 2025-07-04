import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def colormap_griglia(img_path, n):
    # 1. Carica immagine e converte in RGB
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img.shape

    cell_h, cell_w = h // n, w // n

    # 2. Trova colore medio di ogni cella
    colori_celle = []
    for i in range(n):
        for j in range(n):
            # Margine per evitare bordo nero griglia
            margin = cell_h // 10
            x_start = j * cell_w + margin
            y_start = i * cell_h + margin
            x_end = (j + 1) * cell_w - margin
            y_end = (i + 1) * cell_h - margin
            cell = img[y_start:y_end, x_start:x_end]
            mean_color = np.mean(cell.reshape(-1, 3), axis=0)
            colori_celle.append(mean_color)

    colori_celle = np.array(colori_celle)

    # 3. Clusterizza i colori in n gruppi
    kmeans = KMeans(n_clusters=n, random_state=42).fit(colori_celle)
    labels = kmeans.labels_

    # 4. Ricostruisci la matrice nxn, mappando i label da 1 a n
    matrice = labels.reshape((n, n)) + 1   # +1 per valori da 1 a n

    """print("Matrice colore rilevata:")
    print(matrice)"""

    # Visualizza risultato (opzionale)
    """ plt.imshow(matrice, cmap='rainbow', interpolation='none')
    plt.title("Mappa dei colori trovati")
    plt.colorbar()
    plt.show()"""

    return matrice
