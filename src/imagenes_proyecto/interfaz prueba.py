from tkinter import Tk, Label, Button, Entry, PhotoImage, Toplevel, END,\
Listbox, filedialog, StringVar, ttk

#Tk = ventana
#Label = textos 
#Button = Button 
#Entry = entradas de texto 
#PhotoImage = colocar imágenes 
#Toplevel = colocar una ventana sobre otra 
#END = final de una lista
#Listbox = listas
#filedialog = abrir un archivo de la computadora
#StringVar y ttk = menu de opciones


def salir():
    ventana.destroy()

def login():
   nombre = usuario.get()
   contraseña = contrasena.get()
   if nombre == "<nombredeusuario>" and contraseña == "<contrasena>":
        inc = Label(ventana, bg="white")
        inc.place(x=400, y=290, width=160, height=25)
        usuario.delete(0,END)
        contrasena.delete(0,END)
        correcta()
    
   else:
        inc = Label(ventana, text="Contraseña o usuario incorrecto", 
                    bg="gray", fg="white")
        inc.place(x=400, y=290, width=190, height=25)


def correcta():
    
    #Boton "Buscar pieza de PVC"
    def buscar():
        
        #Boton "volver"
        def regreso():
            window.withdraw()
            ventana2.deiconify() 
        
        def abrir_archivo():
            archivo = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

            nombre_archivo = filedialog.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=archivo)
            
            
            archivo_seleccionado = Label(window, bg="white", fg="black")
            archivo_seleccionado.place(x=40, y=309, width=490, height=23)
            archivo_seleccionado.config(text=nombre_archivo)  
        
        #Boton "buscar" 
        def buscar1():
            def regreso2():
                vbuscar.withdraw()
                window.deiconify()
            
            window.withdraw()
            vbuscar = Toplevel()
            vbuscar.title("Buscar Piezas")
            vbuscar.geometry("700x400")
            vbuscar.resizable(width=False, height=False)
            img2 = PhotoImage(file="buscar1.png")
            img = Label(vbuscar, image= img2)
            img.place(x=0, y=0, relwidth=1, relheight=1 )
            volver = Button(vbuscar, text= "Volver",
                            command=regreso2, bg="white")
            volver.place(x=45, y= 18, width=60, height=25)
            
            window.mainloop()
            
        ventana2.withdraw()
        window = Toplevel()
        window.title("Buscar pieza de PVC")
        window.geometry("700x400")
        window.resizable(width=False, height=False)
        img3 = PhotoImage(file="buscarpiezapvc.png")
        img = Label(window, image= img3)
        img.place(x=0, y=0, relwidth=1, relheight=1 )
        
        #botones
        buscar_pieza = Button(window, text="Buscar", command=buscar1, 
                              bg="black", fg="white")
        buscar_pieza.place(x=543, y=287, width=116, height=45)

        volver = Button(window, text="Volver", command=regreso, 
                        bg="white")
        volver.place(x=31, y=10, width=64, height=28)
        
        buscar_archivo = Button(window, text= "Buscar", command=abrir_archivo,
                                bg="black", fg="white")
        buscar_archivo.place(x=162, y=170, width=116, height=45)
        
        window.mainloop()
    
    #Boton "almacenamiento de medidas"
    def almacenamiento_de_medidas():
    
        def regreso4():
            ventana_medidas.withdraw()
            ventana2.deiconify()
               
           #ventana
        ventana2.withdraw()
        ventana_medidas = Toplevel()
        ventana_medidas.title("ingresar nuevas medidas")
        ventana_medidas.geometry("700x400")
        ventana_medidas.resizable(width=False, height=False)
                
        #imagen
        img2 = PhotoImage(file="ingresar_nuevas_medidas.png")
        img = Label(ventana_medidas, image= img2)
        img.place(x=0, y=0, relwidth=1, relheight=1 )
        #entradas
        largo = Entry(ventana_medidas, bg="white")
        largo.place(x=275, y=130, width=70, height=20)
    
        ancho = Entry(ventana_medidas, bg="white")
        ancho.place(x=275, y=158, width=70, height=20)
    
        color = Entry(ventana_medidas, bg="white")
        color.place(x=275, y=186, width=70, height=20)
        
        ubicacion = Entry(ventana_medidas,bg="white")
        ubicacion.place(x=275, y=215, width=70, height=20)
        
        texto = StringVar
        combo = ttk.Combobox(ventana_medidas)
        combo.place(x=275, y=243)
        combo["values"]=("marco - corredera",
                         "marco - ventana",
                         "hoja - ventana fija",
                         "hoja - corredera",
                         "hoja - ventana oscilante",
                         "hoja - ventana batiente")
                
        #botones
        almacenarb = Button(ventana_medidas, text= "Almacenar", 
                            bg="black", fg="white")
        almacenarb.place(x=303, y= 281, width=116, height=42) 
                
        volver = Button(ventana_medidas, command=regreso4, 
                        text= "Volver", bg="white")
        volver.place(x=20, y= 2, width=65, height=27)
                
        ventana_medidas.mainloop()
        
    #Boton "estadisticas"
    def estadisticas():
        
        def regreso5():
            ventana_estadistica.withdraw()
            ventana2.deiconify()
          
        ventana2.withdraw()
        ventana_estadistica = Toplevel()
        ventana_estadistica.title("Estadisticas")
        ventana_estadistica.geometry("700x400")
        ventana_estadistica.resizable(width=False, height=False)
       
        #imagen
        img2 = PhotoImage(file="estadistica.png")
        img = Label(ventana_estadistica, image=img2)
        img.place(x=0, y=0, relwidth=1, relheight=1)
        
        #botones
        volver = Button(ventana_estadistica, command=regreso5, 
                        text="Volver", bg="white")
        volver.place(x=38, y=7, width=61, height=26)
        
        ventana_estadistica.mainloop()
    
    #Boton "gestor"
    def gestor():
        def login_admin():
           contraseña = contrasena.get()
           if contraseña == "21594":
              correct = Label(ventana_gestor, bg="white")
              correct.place(x=400, y=290, width=160, height=25)
              
              sesión_admin()
           else:
               inc = Label(ventana_gestor, text="Contraseña incorrecta", 
                           bg="gray", fg="white")
               inc.place(x=400, y=290, width=140, height=25)
               
        def sesión_admin():
            
            def entradas():
                b = nuevo_nombre.get() + "," + nueva_contrasena.get()
                lista.insert(END, b )
                
                nuevo_nombre.delete(0, END)
                nueva_contrasena.delete(0,END)   

            def regreso5():
                ventana_admin.withdraw()
                ventana2.deiconify()
              
            ventana_gestor.withdraw()
            ventana_admin = Toplevel()
            ventana_admin.title("Administrar usuarios y contraseñas")
            ventana_admin.geometry("700x400")
            ventana_admin.resizable(width=False, height=False)
            
            #imagen
            img2 = PhotoImage(file="gestor de contraseñas.png")
            img = Label(ventana_admin, image= img2)
            img.place(x=0, y=0, relwidth=1, relheight=1 )
            
            #botones
            volver = Button(ventana_admin, command=regreso5, 
                            text= "Volver", bg="white")
            volver.place(x=40, y=17, width=61, height=26)
            
            boton_agregar = Button(ventana_admin, text="Agregar", 
                                   command=entradas, bg = "black", fg="white")
            boton_agregar.place(x=202, y=197, width=115, height=40)
            
            boton_guardar = Button(ventana_admin, text="Guardar", 
                                   bg = "black", fg="white")
            boton_guardar.place(x=530, y=330, width=80, height=27)
            
            #Entradas
            nuevo_nombre = Entry(ventana_admin, bg="white")
            nuevo_nombre.place(x=220, y= 112, width=112, height=22)
            
            nueva_contrasena = Entry(ventana_admin,bg="white")
            nueva_contrasena.place(x=220, y= 140, width=112, height=22)
            
            cambio_contrasena = Entry(ventana_admin,bg="white")
            cambio_contrasena.place(x=310, y= 330, width=200, height=25)
            
            # texto
            texto = Label(ventana_admin, bg="black", fg="white",
                          text= "Nombre:      Contraseña:")
            texto.place(x=390, y=105, width=200, height=20)
            
            #listas
            lista = Listbox(ventana_admin)
            lista.place(x=390, y=125, width=200, height=150)
            
            ventana_admin.mainloop()
            
            
        
        def regreso5():
            ventana_gestor.withdraw()
            ventana2.deiconify()
          
        ventana2.withdraw()
        ventana_gestor=Toplevel()
        ventana_gestor.title("Login administrador")
        ventana_gestor.geometry("700x400")
        ventana_gestor.resizable(width=False, height=False)

        #imagen
        img2 = PhotoImage(file="gestor de usuarios.png")
        img = Label(ventana_gestor, image=img2)
        img.place(x=0, y=0, relwidth=1, relheight=1 )

        #entrada 
        contrasena = Entry(ventana_gestor, bg="white", show="*")
        contrasena.place(x=220, y= 200, width=250, height=30)

        #botones
        volver = Button(ventana_gestor, command=regreso5, 
                        text= "Volver", bg="white")
        volver.place(x=43, y= 28, width=61, height=26)
        boton = Button(ventana_gestor, text="Iniciar sesión", 
                       command=login_admin, cursor="hand2",
                       bg = "black", fg="white")
        boton.place(x=272, y= 315, width=120, height=50)

        ventana_gestor.mainloop()
    
    ventana.withdraw()
    ventana2 = Toplevel()
    ventana2.title("Login")
    ventana2.geometry("700x400")
    ventana2.resizable(width=False, height=False)
    img3 = PhotoImage(file="inicio.png")
    img = Label(ventana2, image= img3)
    img.place(x=0, y=0, relwidth=1, relheight=1 )
    
  
    #botones
    buscar=Button(ventana2,bg="blue", 
                    command=buscar, text = "Buscar pieza de PVC")
    buscar.place(x=165, y= 130, width=170, height=60)
    
    estadisticas=Button(ventana2,bg="blue", 
                          command=estadisticas, text = "Estadísticas")
    estadisticas.place(x=165, y=221, width=170, height=60)
    
    almacenamiento=Button(ventana2,bg="blue", 
    command=almacenamiento_de_medidas, text = "Almacenamiento de medidas")
    almacenamiento.place(x=400, y= 128, width=170, height=60)
    
    gestor=Button(ventana2,bg="blue", 
                    command=gestor,text = "Gestor de usuarios")
    gestor.place(x=400, y=220, width=170, height=60)
    
    salida=Button(ventana2, text= "Salir", 
                   command=salir, bg="white")
    salida.place(x=600, y=15, width=60, height=25) 
    
    #texto
    nombre = Label(ventana2, bg="white", fg="black", font="consolas 15 bold")
    nombre.place(x=380, y=20, width=210, height=25)
    nombre.config(text=usuario.get())
    ventana2.mainloop()
    

#ventana
ventana = Tk()
ventana.title("Login")
ventana.geometry("700x400")
ventana.resizable(width=False, height=False)
fondo = PhotoImage(file="portada.png")
fondo1 = Label(ventana, image=fondo)
fondo1.place(x=0, y=0, relwidth=1, relheight=1)

#botones
iniciar_sesion = Button(ventana, text="Iniciar sesión", command=login, 
               cursor="hand2", bg="black", fg="white")
iniciar_sesion.place(x=269, y=315, width=125, height=50)

boton_salir = Button(ventana, text="Salir", command=salir, bg="white")
boton_salir.place(x=600, y=15, width=50, height=20) 

#entradas
usuario = Entry(ventana,bg="white")
usuario.place(x=330, y=165, width=250, height=30)

contrasena = Entry(ventana,bg="white", show="*")
contrasena.place(x=330, y=247, width=250, height=30)

ventana.mainloop()
