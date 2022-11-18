from random import choice, randint
import pandas as pd

df = pd.DataFrame(columns=["Perfil", "Color", "Largo", "Ubicación", "Usuario"])

def insertar(profile, kolor, largue, location): 
    # El insertar no recibe el no-usuario como argumento, se inserta por default     ;
    df.loc[len(df)] = [profile, kolor, largue, location, "uwu"]

for linea in range(1000): # n elementos
    insertar(choice(["CORREDERA", "FIJA", "OSCILANTE", "BATIENTE"]), 
     choice(["BLANCO", "CAOBA", "GRAFITO", "NOGAL", "ROBLE CLARO", "ROBLE OSCURO",]),
     float(randint(1000, 4000)/10), 
     choice((["A", "B", "C", "D", "E"])) + str(randint(1, 10)))

df.to_csv("inventario.csv", index=False)