from tkinter import Tk, Label, Button, Entry, PhotoImage, Toplevel, END, Listbox

#funcion para salir del programa
def salir():
    ventana_ingresar.destroy()
    return True

#funcion de la ventana principal, es donde el usuario ingresa su 
#identificación y su contraseña
def login():
    nombre = usuario.get()
    contraseña = contrasena.get()
    
      # condicion que comprueba que los datos ingresados por el 
      # usuario son correctos, para poder ingresar al software
    if nombre == "Francisco Riquelme" and contraseña == "21594":
        contrasena_correcta = Label(ventana_ingresar, bg="white")
        contrasena_correcta.place(x=400, y=290, width=160, height=25)
      
      #limpiar las entradas de texto
        usuario.delete(0,END)
        contrasena.delete(0,END)
      
      #invocar la función "correcta" que abre la ventana principal
        correcta()
      
      # si no se cumple lo anterior, aparecerá una notificación que indicará 
      # que la contraseña o el usuario es incorrecto
    else:
        contrasena_incorrecta = Label(ventana_ingresar, 
                   text="Contraseña o usuario incorrecto", 
                   bg="gray", 
                   fg="white")
        contrasena_incorrecta.place(x=400, y=290, width=190, height=25)
    return True

# función que si se activa, abre la ventana principal
def correcta():
    
    #Boton "Buscar pieza de PVC"
    def buscar():
        
        #Boton "volver a la ventana principal"
        def regreso():
            ventana_buscar_pieza.withdraw()
            ventana_principal.deiconify() 
            return True
            
        #Boton "buscar" atraves de caracteristicas 
        def buscar_por_caracteristicas():
            def regreso2():
                #se cierra la ventana 
                vbuscar.withdraw()
                ventana_buscar_pieza.deiconify()
                return True
            
            ventana_buscar_pieza.withdraw()
            vbuscar = Toplevel()
            vbuscar.title("Buscar Piezas")
            vbuscar.geometry("700x400")
            vbuscar.resizable(width=False, height=False)
            img2 = PhotoImage(file="buscar1.png")
            lb1_img = Label(vbuscar, 
                            image= img2).place(x=0, y=0, 
                                               relwidth=1, 
                                               relheight=1 )
            volver = Button(vbuscar, 
                            text = "Volver", 
                            command = regreso2, 
                            bg = "white")
            volver.place(x=45, y= 18, width=60, height=25)
            ventana_buscar_pieza.mainloop()
         
        # funcion que se activa por el boton "buscar" atraves de variables
        # el cual abre una ventana que muestra por pantalla las piezas
        # encontradas
        def buscar_por_variables():
            def regreso2():
                vbuscar.withdraw()
                ventana_buscar_pieza.deiconify()
                return True
            
            ventana_buscar_pieza.withdraw()
            vbuscar = Toplevel()
            vbuscar.title("Buscar Piezas")
            vbuscar.geometry("700x400")
            vbuscar.resizable(width=False, height=False)
            img2 = PhotoImage(file="buscar1.png")
            lb1_img = Label(vbuscar, image= img2).place(x=0, 
                                                        y=0, 
                                                        relwidth=1, 
                                                        relheight=1 )
            volver = Button(vbuscar, 
                            text= "Volver", 
                            command=regreso2, 
                            bg="white")
            volver.place(x=45, y= 18, width=60, height=25)
            
            #para agregar la barrita que sube y baja, hay que agregar el comando
            #Scrollbar y el .grid
            #video 46, min 11:30
            ventana_buscar_pieza.mainloop()
            return True
        ventana_principal.withdraw()
        ventana_buscar_pieza = Toplevel()
        ventana_buscar_pieza.title("Buscar pieza de PVC")
        ventana_buscar_pieza.geometry("700x400")
        ventana_buscar_pieza.resizable(width=False, height=False)
        img = PhotoImage(file="buscarpiezapvc.png")
        lb1_img = Label(ventana_buscar_pieza, 
                        image= img).place(x=0, y=0, 
                                          relwidth=1, 
                                          relheight=1 )
        
        #botones
        buscar = Button(ventana_buscar_pieza, 
                        text = "Buscar", 
                        command = buscar_por_caracteristicas, 
                        bg = "black", 
                        fg = "white")
        buscar.place(x=222, y= 276, width=110, height=40) 

        buscar2 = Button(ventana_buscar_pieza, 
                         text = "Buscar", 
                         command = buscar_por_variables, 
                         bg = "black", 
                         fg = "white")
        buscar2.place(x=489, y= 276, width=110, height=40) 

        volver = Button(ventana_buscar_pieza, 
                        text= "Volver", 
                        command=regreso, 
                        bg="white")
        volver.place(x=44, y= 18, width=61, height=26)
        
        
        #entradas
        largo = Entry(ventana_buscar_pieza, bg="white")
        largo.place(x=245, y= 150, width=70, height=20)

        ancho = Entry(ventana_buscar_pieza, bg="white")
        ancho.place(x=245, y= 178, width=70, height=20)

        color = Entry(ventana_buscar_pieza, bg="white")
        color.place(x=245, y= 204, width=70, height=20)
        
        
        ventana_buscar_pieza.mainloop()
        return True
    #Boton "almacenamiento de medidas"
    def almacenamiento_de_medidas():
        
        def regreso3():
            ventana_almacen.withdraw()
            ventana_principal.deiconify()
            return True

        def nuevas_medidas():
            
            def regreso4():
                ventana_medidas.withdraw()
                ventana_almacen.deiconify()
                return True
            #ventana
            ventana_almacen.withdraw()
            ventana_medidas = Toplevel()
            ventana_medidas.title("ingresar nuevas medidas")
            ventana_medidas.geometry("700x400")
            ventana_medidas.resizable(width=False, height=False)
            
            #imagen
            img2 = PhotoImage(file="ingresar_nuevas_medidas.png")
            lb1_img = Label(ventana_medidas, 
                            image= img2).place(x=0, y=0, 
                                               relwidth=1, 
                                               relheight=1 )
            
            #entradas
            largo = Entry(ventana_medidas, bg="white")
            largo.place(x=275, y= 130, width=70, height=20)

            ancho = Entry(ventana_medidas, bg="white")
            ancho.place(x=275, y= 158, width=70, height=20)

            color = Entry(ventana_medidas, bg="white")
            color.place(x=275, y= 184, width=70, height=20)

            ubicacion = Entry(ventana_medidas,bg="white")
            ubicacion.place(x=275, y= 212, width=70, height=20)
            
            #botones
            boton_almacenar = Button(ventana_medidas, 
                                     text= "Almacenar", 
                                     bg="black", fg="white")
            boton_almacenar.place(x=269, y= 280, width=110, height=40) 
            
            volver = Button(ventana_medidas, 
                            command=regreso4, 
                            text= "Volver", 
                            bg="white")
            volver.place(x=31, y= 8, width=61, height=25)
            
            ventana_medidas.mainloop()
            return True
        
        def variables():
            
            def regreso5():
                ventana_variables.withdraw()
                ventana_almacen.deiconify()
                return True
            
            ventana_almacen.withdraw()
            ventana_variables = Toplevel()
            ventana_variables.title("Variables")
            ventana_variables.geometry("700x400")
            ventana_variables.resizable(width=False, height=False)
            
            #imagen
            img2 = PhotoImage(file="ingresar_variables.png")
            lb1_img = Label(ventana_variables, 
                            image= img2).place(x=0, y=0, 
                                               relwidth=1, 
                                               relheight=1 )
            
            #entradas
            nombre_variable = Entry(ventana_variables, bg="white")
            nombre_variable.place(x=275, y= 132, width=70, height=20)
            
            largo_variable = Entry(ventana_variables, bg="white")
            largo_variable.place(x=275, y= 161, width=70, height=20)

            ancho_variable = Entry(ventana_variables, bg="white")
            ancho_variable.place(x=275, y= 189, width=70, height=20)

            color_variable = Entry(ventana_variables, bg="white")
            color_variable.place(x=275, y= 218, width=70, height=20)

            ubicacion_variable = Entry(ventana_variables,bg="white")
            ubicacion_variable.place(x=275, y= 245, width=70, height=20)
            
            #botones
            almacenarb = Button(ventana_variables, 
                                text= "Almacenar", 
                                bg="black", 
                                fg="white")
            almacenarb.place(x=252, y= 287, width=110, height=40) 
            
            volver = Button(ventana_variables, 
                            command=regreso5, 
                            text= "Volver", 
                            bg="white")
            volver.place(x=43, y= 28, width=61, height=26)
            
            ventana_variables.mainloop()
            return True
        
        #ventana
        ventana_principal.withdraw()
        ventana_almacen = Toplevel()
        ventana_almacen.title("Almacenamiento de medidas")
        ventana_almacen.geometry("700x400")
        ventana_almacen.resizable(width=False, height=False)

        img2 = PhotoImage(file="almacen.png")
        lb1_img = Label(ventana_almacen, 
                        image= img2).place(x=0, y=0, 
                                           relwidth=1, 
                                           relheight=1 )

        #botones
        almacenamiento = Button(ventana_almacen, 
                                text= "Ingresar nuevas medidas", 
                                command=nuevas_medidas, 
                                bg="blue", 
                                fg="black")
        almacenamiento.place(x=138, y= 185, width=170, height=60) 

        variables = Button(ventana_almacen, 
                           text= "Variables", 
                           command=variables, 
                           bg="Blue", 
                           fg="black")
        variables.place(x=387, y= 185, width=170, height=60)

        volver = Button(ventana_almacen,
                        text= "Volver", 
                        command=regreso3, 
                        bg="white")
        volver.place(x=45, y= 20, width=60, height=26)
        
        ventana_almacen.mainloop()
        return True
    
    #Boton "estadisticas"
    def estadisticas():
        
        def regreso5():
            ventana_estadistica.withdraw()
            ventana_principal.deiconify()
            return True
        
        ventana_principal.withdraw()
        ventana_estadistica = Toplevel()
        ventana_estadistica.title("Estadisticas")
        ventana_estadistica.geometry("700x400")
        ventana_estadistica.resizable(width=False, height=False)
        
        #imagen
        img2 = PhotoImage(file="estadistica.png")
        lb1_img = Label(ventana_estadistica, 
                        image= img2).place(x=0, y=0, 
                                           relwidth=1, 
                                           relheight=1 )
        
        #botones
        volver = Button(ventana_estadistica, 
                        command=regreso5, 
                        text= "Volver", 
                        bg="white")
        volver.place(x=38, y= 7, width=61, height=26)
        
        ventana_estadistica.mainloop()
        return True
    #Boton "gestor"
    def gestor():
        
        def login_admin():
           contraseña = contrasena.get()
           if contraseña == "21594":
              contrasena_correcta = Label(ventana_gestor, bg="white")
              contrasena_correcta.place(x=400, y=290, width=160, height=25)
              
              sesión_admin()
           else:
               contrasena_incorrecta = Label(ventana_gestor, 
                                             text="Contraseña incorrecta", 
                                             bg="gray", 
                                             fg="white")
               contrasena_incorrecta.place(x=400, y=290, width=140, height=25)
               
        def sesión_admin():
            
            def entradas():
                b = nuevo_nombre.get() + "," + nueva_contrasena.get()
                lista.insert(END, b )
                
                nuevo_nombre.delete(0, END)
                nueva_contrasena.delete(0,END)   

            def regreso5():
                ventana_admin.withdraw()
                ventana_principal.deiconify()
              
            ventana_gestor.withdraw()
            ventana_admin = Toplevel()
            ventana_admin.title("Administrar usuarios y contraseñas")
            ventana_admin.geometry("700x400")
            ventana_admin.resizable(width=False, height=False)
            
            #imagen
            img2 = PhotoImage(file="gestor de contraseñas.png")
            lb1_img = Label(ventana_admin, 
                            image= img2).place(x = 0, y = 0, 
                                               relwidth = 1, 
                                               relheight = 1 )
            
            #botones
            volver = Button(ventana_admin, 
                            command = regreso5, 
                            text = "Volver", 
                            bg ="white")
            volver.place(x = 40, y = 17, width = 61, height = 26)
            
            boton_agregar = Button(ventana_admin, 
                                   text ="Agregar", 
                                   command = entradas, 
                                   cursor = "hand2", 
                                   bg = "black", 
                                   fg = "white")
            boton_agregar.place(x = 202, y = 197, width = 115, height = 40)
            
            boton_guardar = Button(ventana_admin, 
                                   text = "Guardar", 
                                   cursor = "hand2", 
                                   bg = "black", 
                                   fg = "white")
            boton_guardar.place(x = 530, y = 330, width = 80, height = 27)
            
            #Entradas
            nuevo_nombre = Entry(ventana_admin, bg="white")
            nuevo_nombre.place(x = 220, y = 112, 
                               width = 112, 
                               height = 22)
            
            nueva_contrasena = Entry(ventana_admin,bg="white")
            nueva_contrasena.place(x = 220, y = 140, 
                                   width = 112, 
                                   height = 22)
            
            cambio_contrasena = Entry(ventana_admin, bg="white")
            cambio_contrasena.place(x = 310, y = 330, width = 200, height = 25)
            
            # texto
            texto = Label(ventana_admin, 
                          bg = "black", 
                          fg = "white", 
                          text = "Nombre y Contraseña:")
            texto.place(x = 390, y = 105, 
                        width = 200, 
                        height = 20)
            
            #listas
            lista = Listbox(ventana_admin)
            lista.place(x = 390, y = 125, width = 200, height = 150)
            
            ventana_gestor.mainloop()
            
            
        
        def regreso5():
            ventana_gestor.withdraw()
            ventana_principal.deiconify()
          
        ventana_principal.withdraw()
        ventana_gestor = Toplevel()
        ventana_gestor.title("Login administrador")
        ventana_gestor.geometry("700x400")
        ventana_gestor.resizable(width=False, height=False)

        #imagen
        img2 = PhotoImage(file = "gestor de usuarios.png")
        lb1_img = Label(ventana_gestor, 
                        image = img2).place(x = 0, y = 0, 
                                           relwidth = 1, 
                                           relheight = 1 )

        #entrada 
        contrasena = Entry(ventana_gestor, bg="white", show="*")
        contrasena.place(x=220, y= 200, width=250, height=30)

        #botones
        volver = Button(ventana_gestor, 
                        command=regreso5, 
                        text= "Volver", 
                        bg="white")
        volver.place(x=43, y= 28, width=61, height=26)
        
        boton = Button(ventana_gestor, 
                       text = "Iniciar sesión", 
                       command = login_admin, 
                       cursor = "hand2", 
                       bg = "black", 
                       fg = "white")
        boton.place(x=272, y= 315, width=120, height=50)

        ventana_gestor.mainloop()
    
    
   # ventana que contiene 4 botones que abren sus respectivas ventanas 
   # y un boton para cerrar el software 
    ventana_ingresar.withdraw()
    ventana_principal = Toplevel()
    ventana_principal.title("Login")
    ventana_principal.geometry("700x400")
    ventana_principal.resizable(width=False, height=False)
    img3 = PhotoImage(file="inicio.png")
    lb1_img = Label(ventana_principal, 
                    image= img3).place(x=0, y=0, 
                                       relwidth=1, 
                                       relheight=1 )
    
    
    #botones
    buscar = Button(ventana_principal, 
                    bg = "blue", 
                    command = buscar, 
                    text = "Buscar pieza de PVC")
    buscar.place(x = 165, y = 128, width = 170, height = 60)
    
    estadisticas = Button(ventana_principal,
                          bg = "blue", 
                          command = estadisticas, 
                          text = "Estadisticas")
    estadisticas.place(x = 165, y = 225, width = 170, height = 60)
    
    almacenamiento = Button(ventana_principal,
                            bg = "blue", 
                            command = almacenamiento_de_medidas, 
                            text = "Almacenamiento de medidas")
    almacenamiento.place(x = 400, y= 128, width=170, height=60)
    
    gestor = Button(ventana_principal,
                    bg = "blue", 
                    command = gestor,
                    text = "Gestor de usuarios")
    gestor.place(x = 400, y = 220, width = 170, height = 60)
    
    salida= Button(ventana_principal, 
                   text = "Salir", 
                   command = salir, 
                   bg = "white")
    salida.place(x = 600, y = 15, width = 60, height = 25) 
    
    #texto que se muestra en la ventana principal indicando el nombre
    #del usuario que ha ingresado
    indicador = Label(ventana_principal, 
                bg = "white", 
                fg = "black", 
                font = "consolas 15 bold")
    indicador.place(x=380, y=20, width=210, height=25)
    indicador.config(text=usuario.get())
    ventana_principal.mainloop()
    

#ventana principal de ingreso de usuario
ventana_ingresar = Tk()
ventana_ingresar.title("Login")
ventana_ingresar.geometry("700x400")
ventana_ingresar.resizable(width=False, height=False)
fondo = PhotoImage(file= "portada.png")
fondo1 = Label(ventana_ingresar, 
               image=fondo).place(x=0, y=0, 
                                  relwidth = 1, 
                                  relheight = 1)

#botones
boton = Button(ventana_ingresar, 
               text = "Iniciar sesión", 
               command = login, 
               cursor = "hand2", 
               bg = "black", 
               fg = "white")
boton.place(x=269, y= 315, width=125, height=50)

boton2 = Button(ventana_ingresar, 
                text = "Salir", 
                command = salir, 
                bg = "white")
boton2.place(x=600, y= 15, width=50, height=20) 

#entradas
usuario = Entry(ventana_ingresar,bg="white")
usuario.place(x=330, y= 165, width=250, height=30)

contrasena = Entry(ventana_ingresar,bg="white", show="*")
contrasena.place(x=330, y= 247, width=250, height=30)

ventana_ingresar.mainloop()