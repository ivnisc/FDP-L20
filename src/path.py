import os
import sys

# Este archivo es para definir una función necesaria para muchos archivos.
# Esta función es para obtener la ruta relativa de un archivo.
# Este archivo se lo pasamos como parámetro.
# Para esta función asumimos construimos siempre la misma ruta,
# es decir, los archivos provenientes de la carpeta "docs".


def ruta_de_(archivo):
    docs_path = os.path.join(os.path.dirname(sys.path[0]), "docs")
    file_path = os.path.join(docs_path, str(archivo))
    return file_path

