#Función que devuelve los intentos fallados del ahorcado
def mostrarFigura(intentos):
    figuras = [
        """
           +---+
               |
               |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
               |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========="""
    ]
    return figuras[intentos]



#Lista de palabras para el juego
palabrasOcultasPython = "print input output diagrama modulo excepcion archivo entrada salida argumento expresion algoritmo programacion interprete sintaxis biblioteca condicional clase objeto python metodo estructura funcion bucle codigo operador while for if else elif match case break continue diccionario lista tupla variable string bool int true false clave valor cadena multiparadigma dinamico interpretado multiplataforma len range append count extend insert index remove pop reverse sort copy fromkeys get items keys values update popitem clear del dir type return parametros argumentos from def resource pass libreria".split()

