# Proyecto de laboratorio FDP 10145-0 | L-20 # 

## Primer paso ## 
* Asegúrate de tener instalado *git* en tu dispositivo, o [instálalo](https://git-scm.com/downloads).
* Realiza un **fork** del repositorio (el botoncito de arriba a la derecha). Se creará una copia en tu cuenta. 
* Crea una nueva carpeta y dentro abre una terminal (powershell, bash). Luego utiliza el siguiente comando:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `` git clone https://github.com/tu_usuario/FDP-L20 ``

## Para contribuir al proyecto ##
Visita [esta guía](https://gist.github.com/BCasal/026e4c7f5c71418485c1) para trabajar colaborativamente usando ``git``. Los pasos anteriores también están explicados ahí. 
  
<br>
<br>
<br>
Si no entendiste nada y decidiste seguir leyendo esto después de 10 segundos de haber entrado al enlace, te recomiendo buscar videos sobre git en youtube.

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

## Algunos comandos de git útiles ##

1. ``git init`` inicializa un repositorio nuevo en la carpeta actual.
2. ``git add .`` toma todos los archivos y los prepara para "sacar una foto". Puedes reemplazar el "." por el nombre del archivo específico a preparar. Por ejemplo, ``git add README.md``.
3. ``git reset .`` deshace el git add.
4. ``git commit -m "mensaje"`` saca una foto.
5. ``git checkout -- .`` un ctrl-z pro.
6. ``git log`` lista los commits realizados.
7. ``git commit -amend`` permite modificar el último commit.
8. ``git checkout -b nombredelbranch`` crea un branch.
9. ``git branch`` lista todas las branches.
10. ``git checkout master`` se cambia a la rama master.
11. ``git merge nombredelbranch`` mezcla la rama actual con la rama master.
12. ``git branch -d nombredelbranch`` -d de delete, borra la rama.
13. ``git push`` despliegar a github. 
14. ``git commit -am "mensaje"`` add y commit simultáneamente.
15. ``git status`` un buen comando.

Probablemente más adelante quite esta sección de comandos, ya que es muy genérico y a veces se necesitan parámetros adicionales, además de que en youtube explican mil veces mejor.

Por otro lado, hacer es mejor que ver. Practicar los comandos y ver que desastre provocan ayudan a aprender más rápido (pueden borrar el proyecto y clonarlo de nuevo las veces que quieran).
