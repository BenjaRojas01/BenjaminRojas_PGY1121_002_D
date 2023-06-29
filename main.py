from Libros import *
import random as rn
import numpy as np


acum_pais = np.array([])
acum_cat = np.array([])
ListaLibro = np.array([])
def agregarLibro(ListaLibro):
    l = Libros()
    c = False
    while c == False:

        c = l.setCodlib(input("Ingrese un codigo: "))

    l.titulo_lib = input("Ingrese el Titulo del Libro: ")
    l.autor_lib = input("Ingrese el Autor de Libro: ")

    c = False
    while c == False:
        try:
            c = l.setPrecio(int(input("ingrese el Precio del Libro: ")))
        except BaseException as error:
            print(f"Error: {error}")
    l.pais_lib = input("Ingrese el Pais del Libro: ")

    l.cat_lib = input("Ingrese Categoria del Libro: ")


    c = False
    while c == False:
        try:
            c = l.setA_Publicacion(int(input("ingrese el Año de Publicacion del Libro: ")))
        except BaseException as error:
            print(f"Error: {error}")
    print("Libro Agregado")
    return np.append(ListaLibro,l)


def buscarLibro(ListaLibro):
    codigo = input("Ingrese el codigo del libro: ")
    f = False
    for Libros in ListaLibro:
        if codigo == Libros.cod_lib:
            f = True
            print("-----------------------------------")
            print("Datos de Libro")
            print("-----------------------------------")
            print(f"El Codigo del Libro es: {Libros.cod_lib}")
            print(f"El Titulo del Libro es: {Libros.titulo_lib}")
            print(f"El Auto del Libro es: {Libros.autor_lib}")
            if Libros.apub_lib >= 1780 and Libros.apub_lib<=2018:
                Libros.precio_lib = Libros.precio_lib - (Libros.precio_lib * 0.05)
                print(f"El Precio del libro con descuento es: {Libros.precio_lib}")
            else:
                print(f"El Precio del Libro es: {Libros.precio_lib}")
            print(f"El Pais del Libro es: {Libros.pais_lib}")
            print(f"La Categoria del Libro es: {Libros.cat_lib}")
            if Libros.apub_lib <= 1993:
                print(f"El año de Publicacion es {Libros.apub_lib}")
                print("---------------------------------------------")
                print("El libro es una Edicion Especial, Felicidades")
                print("---------------------------------------------")
            else:
                print(f"El año de Publicacion es {Libros.apub_lib}")
                print("-------------------------------------------")
            break
    if f == False:
        print("Codigo no se encuentra en el sistema")


def imprimirPais(ListaLibro):
    pais = input("Ingrese Pais: ")
    f = False
    print("Certificado del Libro")
    print("---------------------")
    for Libros in ListaLibro:
        if pais == Libros.pais_lib:
            f = True
            print(f"Pais del Certificado: {Libros.pais_lib}")
            print(f"Titulo del libro: {Libros.titulo_lib}")
            print(f"Precio del libro: {Libros.precio_lib}")
            print(f"Catgoria del Libro: {Libros.cat_lib}")
            print(f"Autor del Libro: {Libros.autor_lib}")
    numbers = rn.randrange(1500, 5000)
    print("----------------------------------")
    print(f"El precio del Certificado es: {numbers}")
    print("----------------------------------")
    if f == False:
        print("Pais no se encuentra en el sistema")


def imprimirCat(ListaLibro):
    categoria = input("Ingrese Categoria: ")
    f = False
    for Libros in ListaLibro:
        if categoria == Libros.cat_lib:
            f = True
            print("Certificado del Libro")
            print("---------------------")
            print(f"Categoria del Certificado: {Libros.cat_lib}")
            print(f"Titulo del libro: {Libros.titulo_lib}")
            print(f"Precio del libro: {Libros.precio_lib}")
            print(f"Catgoria del Libro: {Libros.cat_lib}")
            print(f"Autor del Libro: {Libros.autor_lib}")
    numbers = rn.randrange(1500, 5000)
    print("----------------------------------")
    print(f"El precio del Certificado es: {numbers}")
    print("----------------------------------")

    if f==False:
            print("La categoria no esta en el sistema")



def imprimirLibro(ListaLibro):
    print("Imprimir Informes")
    print("1) Informe por Pais")
    print("2) Informe por Categoria")
    try:
        op_imp = int(input("Ingrese Opcion (1-2): "))
        match op_imp:
            case 1:
                imprimirPais(ListaLibro)
            case 2:
                imprimirCat(ListaLibro)
    except BaseException as error:
        print(f"Error{error}")

def salir():
    print("Cerrando sesion")
    print("Autor: Benjamin Rojas")
    print("Version: 1.0")
    return False

ciclo = True
while ciclo:
    print("Bienvenido a Libreria Mayor")
    print("1) Añadir Libro")
    print("2) Buscar Libro")
    print("3) Imprimir Informe")
    print("4) Salir del sistema")
    try:
        op = int(input("Ingrese opcion: (1-4): "))
        match op:
            case 1:
                ListaLibro = agregarLibro(ListaLibro)
            case 2:
                buscarLibro(ListaLibro)
            case 3:
                imprimirLibro(ListaLibro)
            case 4:
                ciclo = salir()
    except BaseException as error:
        print(f"Error{error}")
