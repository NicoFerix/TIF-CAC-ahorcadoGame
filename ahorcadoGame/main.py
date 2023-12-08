#Importación de funciones.
from random import choice
from resource.modules.ahorcadoListas import palabrasOcultasPython, mostrarFigura
from resource.modules.ahorcadoFunciones import espaciosVacios, intento, mostrarLetrasArriesgadas, mostrarVictoria, impresionMensaje


def main():
     #Flujo de programa principal.

    print("""
                        Bienvenid@  al Juego del:
                    A H O R C A D O - Edición Python
                                
                               +---+
                                   |   
                                   |
                                   |
                                   |
                                   |
                           =========""")         

    
    while True:  
        puntajeFinal = 0
        #Nombre predeterminado
        jugador = "Jugador"
        menuGame = input("""\n--MENÚ DE OPCIONES--
        [1] - JUGAR
        [2] - INSTRUCCIONES
        [3] - SALIR
>: """)
        print("#"*100,"\n")
        
             
        if menuGame == "1":
            #Ejecución del juego
            jugador = input(f"""
Nombre del Jugador:
>: """)
            print("#"*100, "\n")
            print(f"""
        ¡Bien {jugador}, comencemos! 
    ¡Esta es tu horca!, ¡Mucha suerte!""")
            continuar = True

            while continuar:
                #Inicialización
                adivinarLaPalabra = choice(palabrasOcultasPython)
                letraActual = ""
                intentosFallidos = 0
                letrasCorrectas = []
                letrasArriesgadas = []
                ganadorOPerdedor = False
                puntajeObtenido = 0
                print(adivinarLaPalabra)

                while intentosFallidos != 7:
                    #Mapeo del ahorcado
                    print(f"""
                {mostrarFigura(intentosFallidos)}

                {espaciosVacios(adivinarLaPalabra, letrasCorrectas)}

                Las letras que arriesgaste ---> {mostrarLetrasArriesgadas(letrasArriesgadas)}""")
                    print("#"*100)


                    #Estructura para ingresar la letra y comprobarla.
                    while True:
                        letraIngresada = input("""
Adivine una letra:
>: """)
                        if len(letraIngresada) != 1:
                            print('Por favor, introduce UNA letra.')
                        
                        elif letraIngresada in letrasArriesgadas:
                            print('Ya has probado esa letra. Elige otra.')
                        
                        elif not letraIngresada.isalpha():
                            print('Por favor ingresa una LETRA.')
                        
                        else:
                            letrasArriesgadas.append(letraIngresada.lower())
                            letraActual = letraIngresada.lower()
                            break
                    

                    #Invocación para separar letras correctas de incorrectas.
                    aciertoFalloPuntaje = intento(letrasCorrectas, intentosFallidos, letraActual, adivinarLaPalabra, puntajeObtenido)
                    print(aciertoFalloPuntaje[1])
                    intentosFallidos = aciertoFalloPuntaje[0]
                    puntajeObtenido = aciertoFalloPuntaje[2]

                    #Invocación para determinar la victoria del jugador.
                    ganadorOPerdedor = mostrarVictoria(adivinarLaPalabra, letrasCorrectas, jugador)

                    #Condicional para evaluar si ganó y salir del juego
                    if ganadorOPerdedor[0]:
                        break
                

                #Acumulador de puntaje
                puntajeFinal += puntajeObtenido
                
                #Condicional para evaluar si ganó o perdió e imprimir un mensaje
                if ganadorOPerdedor[0]:
                    print(ganadorOPerdedor[1])
                else:
                    print(f"{mostrarFigura(intentosFallidos)} {ganadorOPerdedor[1]} ")
                

                #Volver a jugar?
                while True:
                    reintentar = int(input("""
¿Reintentar?
[1]- SI
[2]- NO
>: """))
                    
                    if reintentar == 1:
                        continuar = True
                        mensaje = f"""
                                {jugador.upper()} PUNTAJE TOTAL: {puntajeObtenido} 
                                VAMOS POR ESA NUEVA PARTIDA!!\n"""
                        break
                        
                    elif reintentar == 2:
                        continuar = False
                        mensaje = f"""
                                {jugador.upper()} PUNTAJE TOTAL: {puntajeObtenido}
                                PUNTAJE FINAL: {puntajeFinal}
                                HASTA LUEGO!!\n"""
                        break

                    else: 
                        print("ERROR - Ingrese un valor válido.")

                impresionMensaje(mensaje)  

        
        elif menuGame == "2":
            #Menú de instrucciones
            print(f"""
        Hola, {jugador}
    
    OBJETIVO:
- Adivinar la palabra oculta en menos de 7 intentos.
- Si acaban los intentos, perderás y quedarás AHORCADO.
            ¡¡Si aciertas, GANAS!!
    
    INSTRUCCIONES:
- La palabra estará relacionada con Python.
- En consola verás: 
        ♦ Tantas rayas como letras tenga la palabra.
        ♦ Todas las letras que ingreses.
        ♦ El estado del ahorcado.

    PUNTAJES:
        ♠ Acierto: +1 
        ♠ Error: -0.5 
            
    Luego de cada partida podrás reintentar y ver tu puntaje.
            ¿Preparad@ {jugador}? ¡COMENCEMOS!\n""")
        
       
        elif menuGame ==  "3":
            #Salir del juego
            print("#" * 100, "\n")
            print("MUCHAS GRACIAS POR JUGAR. ¡HASTA LUEGO!\n")
            print("#" * 100, )
            break

        else:
            print("ERROR - Opción inválida. Vuelva a intentarlo.")



    
                 


if __name__ == "__main__":
    main()
