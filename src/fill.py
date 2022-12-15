# Esta función es para generar un archivo inventario.csv con datos aleatorios, 
# para poder probar el programa sin tener que llenar el inventario manualmente.

from random import choice, randint
import pandas as pd
from path import ruta_de_

df = pd.DataFrame(columns=["Perfil", "Color", "Largo", "Ubicación", "Usuario"])

def insertar(profile, kolor, largue, location): 
    # El insertar no recibe el no-usuario como argumento, se inserta por default     ;
    df.loc[len(df)] = [profile, kolor, largue, location, "uwu"]

for linea in range(1000): # n elementos
    insertar(choice(["CORREDERA", "FIJA", "OSCILANTE", "BATIENTE"]), 
     choice(["BLANCO", "CAOBA", "GRAFITO", "NOGAL", "ROBLE CLARO", "ROBLE OSCURO",]),
     float(randint(1000, 4000)/10), 
     choice((["A", "B", "C", "D", "E"])) + str(randint(1, 10)))

df.to_csv(ruta_de_("inventario.csv"), index=False)