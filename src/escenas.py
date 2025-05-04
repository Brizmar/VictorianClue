import pygame
from diseño import *
from utils import renderizar_texto, crear_boton, cargar_imagen
from diseño import crear_boton


def escena_menu(ventana):
    reloj = pygame.time.Clock()

    # Cargar fondo del menú
    fondo = cargar_imagen("fondo_menu.png", tamaño=(ANCHO_VENTANA, ALTO_VENTANA))

    # Crear botones
    boton_jugar = crear_boton("JUGAR", FUENTE_NORMAL, BLANCO, AZUL_NOCHE, 200, 60)
    boton_salir = crear_boton("SALIR", FUENTE_NORMAL, BLANCO, ROJO, 200, 60)

    while True:
        ventana.blit(fondo, (0, 0))

        # Título del juego
        titulo = renderizar_texto("The Gala Mystery", FUENTE_TITULO, DORADO)
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO_VENTANA // 2, 80)))

        # Dibujar botones
        ventana.blit(boton_jugar, (ANCHO_VENTANA // 2 - 100, 300))
        ventana.blit(boton_salir, (ANCHO_VENTANA // 2 - 100, 400))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                if pygame.Rect(ANCHO_VENTANA // 2 - 100, 300, 200, 60).collidepoint(x, y):
                    return "juego"
                elif pygame.Rect(ANCHO_VENTANA // 2 - 100, 400, 200, 60).collidepoint(x, y):
                    return "salir"

        pygame.display.flip()
        reloj.tick(60)

# Aquí sólo las preparamos como plantilla para desarrollar después.
def escena_historia(ventana, historia):
    # Más adelante: muestra narrativa inicial y botones para ir a lugares
    pass

def escena_exploracion(ventana, historia):
    # Más adelante: lógica para visitar 3 lugares y mostrar pistas
    pass

def escena_deduccion(ventana, historia):
    # Más adelante: el jugador elige culpable, arma y lugar
    pass

def escena_resultado(ventana, historia, respuesta_usuario):
    # Más adelante: muestra si el jugador acertó o no
    pass
