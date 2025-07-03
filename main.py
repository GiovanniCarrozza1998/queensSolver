import finalSolver
import gridExtractor
import colorClustering
import screenshotTaker
import time
import moveMaker
import json
import google.generativeai as genai
from PIL import Image

with open('config.json') as config_file:
    config = json.load(config_file)

working_dir = config["working_directory"]
genai.configure(api_key=config["api_key"])
model = genai.GenerativeModel("gemini-2.5-flash")

print("Premi invio per effettuare lo screenshot...")
input()
time.sleep(3)
screenshotTaker.scatta_monitor_specifico(working_dir + "\\screenshot.PNG", 1)

gridExtractor.estrai_griglia(working_dir+'\\screenshot.PNG', working_dir+'\\griglia_estratta.png', debug=False)
#n = int(math.sqrt(gridDimensionFinder.conta_celle(gridDimensionFinder.solo_bordi_nella_griglia('C:\\Users\\503415936\\Pictures\\griglia_estratta.png'),debug=False)-1))
n = int(model.generate_content(["Quante righe ha la griglia presente nell'immagine allegata? Rispondi solo con il numero!", Image.open(working_dir+'\\griglia_estratta.png')]).text)
matrice = colorClustering.colormap_griglia(working_dir + '\\griglia_estratta.png', n)
matrice_risolta = finalSolver.trova_prima_soluzione_no_vertici(matrice)
moveMaker.make_moves(matrice_risolta, working_dir + '\\griglia_estratta.png', n, confidence=0.95)



