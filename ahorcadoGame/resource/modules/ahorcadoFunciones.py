#Función que muestra la palabra oculta entre guiones y letras adivinadas 
def espaciosVacios(palabraPrincipal, letrasAcertadas):
    guionesOLetras = ""
    
    for letras in palabraPrincipal:

        if letras in letrasAcertadas:
            guionesOLetras += f"{letras} "
        else:
            guionesOLetras += "_ "
     
    return guionesOLetras



#Función que imprime la lista de letras obtenidas una al lado de la otra
def mostrarLetrasArriesgadas(letrasObtenidas):
    letrasEnRenglon = ""

    for letras in letrasObtenidas:
        letrasEnRenglon += f"{letras} "

    return letrasEnRenglon



#Función que determina si la letra es correcta o incorrecta y suma los puntajes
def intento (letrasAcertadas, intentosFallidos, letraIngresada, palabraPrincipal, puntajeTotal):

    if letraIngresada in palabraPrincipal:
        puntajeTotal += 1
        letrasAcertadas.append(letraIngresada)
        mensaje = "\n\t¡Letra Correcta!  (◠﹏◠)  "
    else:
        intentosFallidos +=1
        puntajeTotal += -0.5
        mensaje = "\n\t¡Letra Incorrecta!  ಠ_ಠ  "
    
    return (intentosFallidos, mensaje, puntajeTotal)



#Función que evalúa si el jugador ganó o perdió y además guarda un mensaje de victoria o derrota según corresponda.
def mostrarVictoria(palabraPrincipal, letrasAcertadas, player):
    
    for letras in palabraPrincipal:
        if letras not in letrasAcertadas:
            victoria = False
            mensaje = f"""
                           HAS PERDIDO {player.upper()}.
                        TE QUEDASTE SIN INTENTOS

                    No adivinaste la palabra - {palabraPrincipal} -"""
            break
    
    else:
        victoria = True
        mensaje = f"""
                        ¡¡¡FELICIDADES {player.upper()}
                        HAS GANADO EL JUEGO!!!
                
                    Adivinaste la palabra - {palabraPrincipal} -"""
    
    return (victoria, mensaje)



#Procedimiento que imprime bonito.
def impresionMensaje(mensaje):
    print("#" * 100, "\n")
    print(mensaje)
    print("#" * 100)

