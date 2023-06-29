class Libros:
    cod_lib = ''
    titulo_lib = ''
    autor_lib = ''
    precio_lib = 0
    pais_lib = ''
    cat_lib = ''
    apub_lib = 0

    def __init__(self):
        self.cod_lib = 'AAA-111'
        self.titulo_lib = 'S/N'
        self.autor_lib = 'S/A'
        self.precio_lib = 10000
        self.pais_lib = 'S/P'
        self.cat_lib = 'S/C'
        self.apub_lib = 1780

    def setCodlib(self,codigo):
        if codigo[0:3].isalpha() and codigo[3:4] == '-' and codigo[4:8].isdigit():
            self.cod_lib = codigo
            return True
        else:
            print("El Codigo es incorrecto")
            print("Formato del codigo: AAA-111")
            return False

    def setPrecio(self,precio):
        if precio >=10000 and precio <= 150000:
            self.precio_lib = precio
            return True
        else:
            print("Precio fuera de rango")
            print("Rango de precio: 10000 - 15000")
            return False

    def setA_Publicacion(self,a_publicacion):
        if a_publicacion >= 1780 and a_publicacion <= 2023:
            self.apub_lib = a_publicacion
            return True
        else:
            print("Año fuera de rango")
            print("Rango de año de publicacion: 1780 - 2023")
            return False
