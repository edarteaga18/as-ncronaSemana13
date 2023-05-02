print("***************************************************************************")
print("******Bienvenido a nuestro programa de información de los integrantes******")
print("***************************************************************************")   
#Preguntar al usuario si desea ejecutar el programa
while True:
    
        respuesta = input("¿Desea ejecutar el programa? (si/no): ")
        if respuesta.lower() == "si":
            print("INICIO DEL PROGRAMA")
    
            #Mostrar el menú de integrantes
            print("Eliga a un integrante de este grupo: ")
            lisT = [1,2,3,4,5,6]
            integrantes = ["Rodrigo", "Eduardo", "Wendy", "Luis", "Xiomara", "Bryan"]
            for l1, l2 in zip(lisT,integrantes):
                print(l1,l2)   
                    #Pedir al usuario que ingrese el nombre del integrante
            intentos = 4
            while intentos > 0:
                seleccion = input("Ingrese el nombre del integrante: ").upper()
                if seleccion == "Rodrigo".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"*****Información de {seleccion} ******")
                    print("Nombres: Jesus Rodrigo")
                    print("Apellidos: Landaverde Alvarado")
                    print("Sexo: Masculino")
                    print("Departamento: Chalatenango")
                    print("Municipio: Cabecera de chalatenango")
                    print("Dirección: Barrio Las Flores ")
                elif seleccion == "Eduardo".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"****Información de {seleccion} ****")
                    print("Nombres: Eduardo Nathaniel ")
                    print("Apellidos: Sales Arteaga")
                    print("Sexo: Masculino")
                    print("Departamento: Chalatenango")
                    print("Municipio: Dulce Nombre de Maria")
                    print("Dirección: Calle central contiguo a Alcaldia Municipal")
                elif seleccion == "Wendy".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"****Información de {seleccion} *****")
                    print("Nombres: Wendy Daniela ")
                    print("Apellidos: Ayala Ayala")
                    print("Sexo: Femenino")
                    print("Departamento: Chalatengo")
                    print("Municipio: Nueva Concepcion")
                    print("Dirección: Calle Hacia nueva concepcion")
                elif seleccion == "Luis".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"**** Información de {seleccion} ***")
                    print("Nombres: Luis Miguel ")
                    print("Apellidos: Abrego Sanchez")
                    print("Sexo: Masculino")
                    print("Departamento: Chalatenango")
                    print("Municipio:Nueva Trinidad")
                    print("Dirección: Carretera principal hacia Arcatao")
                elif seleccion == "Xiomara".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"**** Información de {seleccion} ****")
                    print("Nombres: Xiomara Abigail ")
                    print("Apellidos: Cisneros Peña")
                    print("Sexo: Femenino")
                    print("Departamento: Chalatenango")
                    print("Municipio: Nueva Concepcion")
                    print("Dirección: Colonia San Francisco,Calle a Metapán")
                elif seleccion == "Bryan".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"**** Información de {seleccion} ****")
                    print("Nombres: Bryan Alexander")
                    print("Apellidos: Pineda Chavez")
                    print("Sexo: Masculino")
                    print("Departamento: Chalatenango")
                    print("Municipio: Nueva Concepcion")
                    print("Dirección: Av. Rio Lempa, Calle El progreso")
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"Nombre no encontrado. Le quedan {intentos} intentos.")
                        continue
                    else:
                        print("Número máximo de intentos finalizados.")
                            
                            #Preguntar si desea consultar otro dato
                
                respuesta = input("¿Desea consultar los datos de otro integrante? (si/no): ")
                if respuesta.lower() == "si":
                    continue
                elif respuesta.lower() == "no":
                    print("Programa finalizado.")
                    break
                else:
                    print("Dato invalido")    
                print("Fin del programa")
                break   
        else:            
            print("Fin del programa")
        break