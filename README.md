# Proyecto de laboratorio FDP 10145-0 | L-20 # 

## Primer paso ## 
* Asegúrate de tener instalado *git* en tu dispositivo, o [instálalo](https://git-scm.com/downloads).
* Instala GitHub Desktop para utilizar git de manera más sencilla.
* Realiza un **fork** del repositorio (el botoncito de arriba a la derecha). Se creará una copia en tu cuenta. 
* Crea una nueva carpeta y dentro abre una terminal (cmd, bash). Luego utiliza el siguiente comando:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `` git clone https://github.com/tu_usuario/FDP-L20 ``

## Depedencias ## 

> *qué raro, en mi pc si funciona...*

Para evitar problemas de compatibilidad, conflictos de versiones o paquetes corruptos, es recomendable utilizar un [entorno virtual](https://docs.python.org/es/3.8/library/venv.html). Una vez activa, puedes hacer una instalación limpia de las librerías necesarias para el correcto funcionamiento del proyecto (esto después de haberlo clonado en tu pc).

Como se mencionó antes, se sugiere utilizar una nueva carpeta para dentro de esta crear la carpeta del entorno virtual y para clonar el proyecto, quedando más o menos de la siguiente manera: 

```
carpeta
└── proyecto (repositorio clonado)
    ├── src
    ├── README.md
    ├── requirements.txt
    ├── ...
└── entornovirtual
    ├── scripts
    ├── pip3
    ├── python3
    ├── ...
  
```
[Este](https://learnpython.com/blog/python-requirements-file/) y [este otro](https://note.nkmk.me/en/python-pip-install-requirements/) artículo explican como utilizar el archivo **requirements.txt** para instalar automáticamente las dependencias necesarias. 
En todo caso, las dependencias del proyecto serán descritas acá de manera oportuna, ya que a medida que se va avanzando, se requiere la intalación de más packages.

## Algunos comandos de git útiles ##

1. ``git add .`` toma todos los archivos y los prepara para "sacar una foto". Puedes reemplazar el "." por el nombre del archivo específico a preparar. Por ejemplo, ``git add README.md``. Esto es útil para que git no trackee todos los archivos innecesarios de un directorio y se haga commit solo del archivo que se está trabajando.
2. ``git reset .`` deshace el git add.
3. ``git commit -m "mensaje"`` saca una foto.
4. ``git log`` lista los commits realizados.
5. ``git commit -amend`` permite modificar el último commit.
6. ``git checkout -b <nombredelbranch>`` crea un branch.
7. ``git branch`` lista todas las branches.
8. ``git checkout master`` se cambia a la rama master.
9. ``git merge <nombredelbranch>`` mezcla la rama actual con la rama master.
10. ``git branch -d <nombredelbranch>`` -d de delete, borra la rama.
11. ``git push`` despliegar a github. 
12. ``git commit -am "mensaje"`` add y commit simultáneamente.
13. ``git status`` un buen comando.

Probablemente más adelante quite esta sección de comandos, ya que es muy genérico y a veces se necesitan parámetros adicionales, además de que en youtube explican mil veces mejor.

Aquí estuvo Giuseppe :O

## Funcionalidades ##
