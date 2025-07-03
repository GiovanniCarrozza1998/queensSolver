import cv2
import numpy as np
from PIL import Image

def estrai_griglia(input_path, output_path, debug=False):
    # 1. Carica l'immagine
    img = cv2.imread(input_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Soglia per evidenziare le linee della griglia
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    edges = cv2.Canny(blur, threshold1=50, threshold2=150)

    # 3. Trova i contorni
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 4. Trova il più grande quadrato (quasi quadrato) tra i contorni
    max_area = 0
    best_rect = None
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        aspect = w / h
        # Cerca una forma abbastanza quadrata (rapporto dimensioni ~1)
        if 0.95 < aspect < 1.05 and area > max_area and w > 100 and h > 100:
            max_area = area
            best_rect = (x, y, w, h)

    if not best_rect:
        print("Impossibile rilevare automaticamente la griglia, riprovo fra 10 secondi...")
        return False


    x, y, w, h = best_rect
    grid_img = img[y:y+h, x:x+w]

    # 5. Salva la griglia estratta
    cv2.imwrite(output_path, grid_img)
    #print(f"Griglia salvata come {output_path}")

    # DEBUG opzionale
    if debug:
        debug_img = img.copy()
        cv2.rectangle(debug_img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.imwrite("debug_estrazione_griglia.png", debug_img)
        #print("Immagine debug salvata come debug_estrazione_griglia.png")

# --- ESEMPIO USO ---"""
"""estrai_griglia('C:\\Users\\503415936\\Pictures\\queens_grid_1.PNG', 'C:\\Users\\503415936\\Pictures\\griglia_estratta.png', debug=True)"""