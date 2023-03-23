#Realizar un script en Python que lea un archivo y pase a otro archivo las palabras que solo tengan la letra u
#archivo1 hugo le dio un bulto a lulu
#archivo2  hugo un bulto lulu
palabras_u = []

try:
    file = open("archivo1.txt", "r")
    pasar_lista = file.read().split()

    for palabras in pasar_lista:
        if 'u' in palabras:
            palabras_u.append(palabras)

    nueva_cadena = " ".join(palabras_u)

    file.close()
    print("Archivo creado con exito")

except FileNotFoundError:
    print("No encuentra el archivo a leer")
    nueva_cadena = "No se paso ninguna palabra"


finally:
    file2 = open("archivo2.txt", "w")
    file2.write(nueva_cadena)
    file2.close()
