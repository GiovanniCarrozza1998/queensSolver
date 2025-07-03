import pyautogui
from screeninfo import get_monitors
import time


def get_total_screens_bounds():
    monitors = get_monitors()
    min_left = min([m.x for m in monitors])
    min_top = min([m.y for m in monitors])
    max_right = max([m.x + m.width for m in monitors])
    max_bottom = max([m.y + m.height for m in monitors])
    total_width = max_right - min_left
    total_height = max_bottom - min_top
    return min_left, min_top, total_width, total_height


def locate_grid_and_compute_cells(grid_img, grid_n, region=None, confidence=0.95):
    """
    Trova la posizione della griglia intera, calcola tutti i centri delle celle.
    Restituisce:
        (grid_x, grid_y, cell_size, centro_griglia, centri_celle)
    """
    box = pyautogui.locateOnScreen(grid_img, region=region, confidence=confidence)
    if box is None:
        raise Exception(f"Impossibile trovare la griglia ({grid_img}) nello schermo!")
    grid_x, grid_y, grid_w, grid_h = box
    print(f"Trovata la griglia a: {box}")

    # Assumiamo griglia quadrata
    assert abs(grid_w - grid_h) < 3, "La griglia non sembra quadrata!"
    cell_size = grid_w // grid_n

    # Calcola centri celle
    centri_celle = []
    for i in range(grid_n):
        row = []
        for j in range(grid_n):
            cx = grid_x + j * cell_size + cell_size // 2
            cy = grid_y + i * cell_size + cell_size // 2
            row.append((cx, cy))
        centri_celle.append(row)

    centro_griglia = (grid_x + grid_w // 2, grid_y + grid_h // 2)
    return (grid_x, grid_y, cell_size, centro_griglia, centri_celle)


def click_celle_su_griglia(centri_celle, matrice):
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            if matrice[i][j] == 1:
                cx, cy = centri_celle[i][j]
                pyautogui.moveTo(cx, cy, duration=0.05)
                pyautogui.click()


def make_moves(matrice, img_grid, n, confidence=0.95):
    min_left, min_top, total_width, total_height = get_total_screens_bounds()
    region = (min_left, min_top, total_width, total_height)

    print("Rilevamento posizione griglia...")
    grid_x, grid_y, cell_size, centro_griglia, centri_celle = \
        locate_grid_and_compute_cells(img_grid, n, region=region, confidence=confidence)
    print(f"Centro griglia rilevato: {centro_griglia}")

    click_celle_su_griglia(centri_celle, matrice)


