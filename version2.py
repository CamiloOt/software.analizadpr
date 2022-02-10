from gettext import find

# Validacion de buenas y malas practicas de caracteres por linea


def caracteres(archivo_texto):
    num_correct = 0
    num_incorrect = 0
    with open(archivo_texto, "r") as fname:
        archivo = fname.readlines()
        for i in archivo:
            if len(i) >= 79:
                num_incorrect += 1
            else:
                num_correct += 1
    print("* Buenas practicas de caracteres por lineas : ", num_correct)
    print("* Malas practicas de caracteres por lineas", num_incorrect, "\n")
    print("¡ERROR! Malas practicas de caracteres en", num_incorrect, "lineas")
    print("----------------------------------------------------------------")


# Validacion de buenas y malas practicas de comentarios


def comentarios(archivo_texto):
    contador_buenas = 0
    contador_malas = 0
    with open(archivo_texto, "r") as fname:
        archivo = fname.readlines()
        for i in archivo:
            if i.find('#') >= 0:
                if len(i) <= 72:
                    contador_buenas += 1
                else:
                    contador_malas += 1
    print("* Buenas practicas de comentarios: ", contador_buenas)
    print("* Malas practicas de comentarios: ", contador_malas, "\n")
    print("¡ERROR! Malas practicas de comentarios en", contador_malas, "lineas")
    print("----------------------------------------------------------------")

# Validacion de malas  practicas de indentacion


def indentacion(archivo_texto):
    espacio = 0
    lista_espacios = {'4espacios': 0}
    with open(archivo_texto, "r") as fname:
        archivo = fname.readlines()
        for i in archivo:
            espacio = 0
            for j in i:
                if j == ' ':
                    espacio += 1
                else:
                    break
            if espacio % 4 != 0:
                lista_espacios['4espacios'] += 1
    print("* Malas practicas de indentacion: ", lista_espacios["4espacios"], "\n")
    print("----------------------------------------------------------------")


# Validacion de malas practicas al imprimir


def espacios_imprimir(archivo_texto):
    malas = 0
    buenas = 0
    with open(archivo_texto, "r") as fname:
        archivo = fname.readlines()
        for i in archivo:
            if i.find('print ') >= 0:
                if len(i) <= 1:
                    malas += 1
                else:
                    buenas += 1
    print("* Malas practicas de imprimir con un total de: ", buenas, "\n")
    print("¡ERROR!  Tiene malas practicas de imprimir en", buenas, "lineas")
    print("----------------------------------------------------------------")


# Validacion de buenas  variables


def prac_variables(archivo_texto):
    correctas = 0
    with open(archivo_texto, 'r') as fname:
        archivo = fname.readlines()
        for i in archivo:
            if '=' in i and i.count('=') == 1:
                posicion = i.find('=')
                if i[posicion - 1] == " " and i[posicion + 1] == " ":
                    if len(i):
                        correctas += 1
    print("* Buenas practicas de variable con el signo ( = ): ", correctas)
    print("----------------------------------------------------------------")


archivo_texto = input("Escriba el nombre del archivo: ")
print("----------------------------------------------------------------")
caracteres(archivo_texto)
comentarios(archivo_texto)
indentacion(archivo_texto)
espacios_imprimir(archivo_texto)
prac_variables(archivo_texto)
