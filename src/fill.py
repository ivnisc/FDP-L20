from random import choice, randint
import pandas as pd

df = pd.DataFrame(columns=["perfil", "color", "largo", "ubicación"])

def insertar(profile, kolor, largue, location):
    df.loc[len(df)] = [profile, kolor, largue, location]

for linea in range(1000): # n elementos
    insertar(choice(["marco - corredera", "marco - ventana fija",
                 "hoja - ventana fija", "hoja - corredera", 
                 "ventana - oscilante", "ventana batiente"]), 
     choice(["blanco", "caoba", "grafito", "nogal", "roble claro", "roble oscuro",]),
     float(randint(1000, 4000)/10), 
     choice((["A", "B", "C", "D", "E"])) + str(randint(1, 10)))

df.to_csv("inventario.csv", index=False)