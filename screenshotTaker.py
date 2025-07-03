import mss

def scatta_screenshot_tutti_monitor(nome_file):
    with mss.mss() as sct:
        # Screenshot di tutti i monitor (bounding box globale)
        sct.shot(mon=-1, output=nome_file)
    print(f"Screenshot di tutti i monitor salvato come {nome_file}")

def scatta_monitor_specifico(nome_file, numero_monitor):
    with mss.mss() as sct:
        # Screenshot di tutti i monitor (bounding box globale)
        sct.shot(mon=numero_monitor, output=nome_file)
    print(f"Screenshot di tutti i monitor salvato come {nome_file}")