import pygame
import sys
from diseño import ANCHO_VENTANA, ALTO_VENTANA, crear_boton
from escenas import escena_menu, escena_historia, escena_exploracion, escena_deduccion, escena_resultado
from juego import Juego

# RUTA AL ARCHIVO DE HISTORIAS
RUTA_JSON = "../data/historias_clue.json"

def main():
    pygame.init()
    pygame.mixer.init()

    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("The Gala Mystery")

    juego = Juego(RUTA_JSON)
    escena_actual = "menu"

    while True:
        if escena_actual == "menu":
            resultado = escena_menu(ventana)
            if resultado == "juego":
                juego.inicializar()
                escena_actual = "historia"
            elif resultado == "salir":
                break

        elif escena_actual == "historia":
            escena_historia(ventana, juego.historia_actual)
            escena_actual = "exploracion"

        elif escena_actual == "exploracion":
            escena_exploracion(ventana, juego)
            escena_actual = "deduccion"

        elif escena_actual == "deduccion":
            respuesta = escena_deduccion(ventana, juego)
            escena_actual = "resultado"
            resultado = juego.verificar_respuesta(*respuesta)

        elif escena_actual == "resultado":
            escena_resultado(ventana, juego.historia_actual, resultado)
            escena_actual = "menu"  # Volver al menú después del resultado

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
