import pygame
import sys
from diseño import *
from utils import renderizar_texto, cargar_imagen, dividir_texto



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

def escena_historia(ventana, historia):
    reloj = pygame.time.Clock()
    continuar = False

    fondo = cargar_imagen("fondo_historia.png", tamaño=(ANCHO_VENTANA, ALTO_VENTANA))
    boton_continuar = crear_boton("CONTINUAR", FUENTE_NORMAL, BLANCO, VERDE_PISTA, 200, 60)

    while not continuar:
        ventana.blit(fondo, (0, 0))

        titulo = renderizar_texto(historia["titulo"], FUENTE_TITULO, DORADO)
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO_VENTANA // 2, 60)))

        # Muestra la historia
        y = 150
        lineas = dividir_texto(historia["narrativa"], FUENTE_NORMAL, ANCHO_VENTANA - 160)
        for linea in lineas:
            texto = renderizar_texto(linea, FUENTE_NORMAL, BLANCO)
            ventana.blit(texto, (80, y))
            y += 35

        ventana.blit(boton_continuar, (ANCHO_VENTANA // 2 - 100, ALTO_VENTANA - 100))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                if pygame.Rect(ANCHO_VENTANA // 2 - 100, ALTO_VENTANA - 100, 200, 60).collidepoint(x, y):
                    continuar = True

        pygame.display.flip()
        reloj.tick(60)

def escena_exploracion(ventana, juego):
    reloj = pygame.time.Clock()

    lugares = juego.historia_actual["lugares"]
    pistas_mostradas = set()

    fondo = cargar_imagen("fondo_exploracion.png", tamaño=(ANCHO_VENTANA, ALTO_VENTANA))

    botones = []
    for i, nombre_lugar in enumerate(lugares.keys()):
        boton = crear_boton(nombre_lugar, FUENTE_NORMAL, BLANCO, AZUL_NOCHE, 250, 60)
        x = ANCHO_VENTANA // 2 - 130
        y = 180 + i * 90
        botones.append((boton, pygame.Rect(x, y, 250, 60), nombre_lugar))

    while len(pistas_mostradas) < len(lugares):
        ventana.blit(fondo, (0, 0))

        titulo = renderizar_texto("¿Dónde quieres investigar?", FUENTE_TITULO, DORADO)
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO_VENTANA // 2, 60)))

        for i, (boton, rect, nombre_lugar) in enumerate(botones):
            if rect.collidepoint(x, y) and i not in pistas_mostradas:
                pista = lugares[nombre_lugar]
                mostrar_pista(ventana, nombre_lugar, pista)
                pistas_mostradas.add(i)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                for i, (boton, rect) in enumerate(botones):
                    if rect.collidepoint(x, y) and i not in pistas_mostradas:
                        mostrar_pista(ventana, lugares[i])
                        pistas_mostradas.add(i)

        pygame.display.flip()
        reloj.tick(60)

def mostrar_pista(ventana, lugar):
    reloj = pygame.time.Clock()
    fondo = cargar_imagen("fondo_pista.png", tamaño=(ANCHO_VENTANA, ALTO_VENTANA))
    boton_volver = crear_boton("VOLVER", FUENTE_NORMAL, BLANCO, VERDE_PISTA, 200, 60)

    mostrar = True
    while mostrar:
        ventana.blit(fondo, (0, 0))

        titulo = renderizar_texto(lugar["nombre"], FUENTE_SUBTITULO, DORADO)
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO_VENTANA // 2, 80)))

        y = 160
        for linea in lugar["pista"].split("\n"):
            texto = renderizar_texto(linea, FUENTE_NORMAL, BLANCO)
            ventana.blit(texto, (60, y))
            y += 40

        ventana.blit(boton_volver, (ANCHO_VENTANA // 2 - 100, ALTO_VENTANA - 100))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                if pygame.Rect(ANCHO_VENTANA // 2 - 100, ALTO_VENTANA - 100, 200, 60).collidepoint(x, y):
                    mostrar = False

        pygame.display.flip()
        reloj.tick(60)

def escena_deduccion(ventana, juego):
    reloj = pygame.time.Clock()
    fondo = cargar_imagen("fondo_deduccion.png", tamaño=(ANCHO_VENTANA, ALTO_VENTANA))

    historia = juego.historia_actual

    sospechosos = historia["sospechosos"]
    armas = historia["armas"]
    lugares = [l["nombre"] for l in historia["lugares"]]

    seleccion = {"sospechoso": 0, "arma": 0, "lugar": 0}

    boton_confirmar = crear_boton("CONFIRMAR", FUENTE_NORMAL, BLANCO, VERDE_CLARO, 220, 60)

    while True:
        ventana.blit(fondo, (0, 0))

        # Título
        titulo = renderizar_texto("¿Cuál es tu deducción?", FUENTE_TITULO, DORADO)
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO_VENTANA // 2, 40)))

        # Categorías
        categorias = [("Sospechoso", sospechosos), ("Arma", armas), ("Lugar", lugares)]
        for i, (nombre, opciones) in enumerate(categorias):
            x = 80 + i * 240
            y = 100

            subtitulo = renderizar_texto(nombre, FUENTE_SUBTITULO, BLANCO)
            ventana.blit(subtitulo, (x, y))

            for j, opcion in enumerate(opciones):
                color = VERDE_CLARO if seleccion[nombre.lower()] == j else BLANCO
                texto = renderizar_texto(opcion, FUENTE_NORMAL, color)
                ventana.blit(texto, (x, y + 40 + j * 30))

        # Botón de confirmar
        ventana.blit(boton_confirmar, (ANCHO_VENTANA // 2 - 110, ALTO_VENTANA - 100))

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()

                # Selección de opciones
                for i, (nombre, opciones) in enumerate(categorias):
                    base_x = 80 + i * 240
                    base_y = 140
                    for j in range(len(opciones)):
                        rect_opcion = pygame.Rect(base_x, base_y + j * 30, 200, 25)
                        if rect_opcion.collidepoint(x, y):
                            seleccion[nombre.lower()] = j

                # Confirmar deducción
                rect_confirmar = pygame.Rect(ANCHO_VENTANA // 2 - 110, ALTO_VENTANA - 100, 220, 60)
                if rect_confirmar.collidepoint(x, y):
                    sospechoso = sospechosos[seleccion["sospechoso"]]
                    arma = armas[seleccion["arma"]]
                    lugar = lugares[seleccion["lugar"]]
                    return (sospechoso, arma, lugar)

        pygame.display.flip()
        reloj.tick(60)

def escena_resultado(ventana, historia, resultado_usuario):
    reloj = pygame.time.Clock()
    continuar = False

    # Fondo elegante (puedes usar otra imagen si quieres personalizar más)
    ventana.fill(GRIS_OSCURO)

    # Mensaje de resultado
    if resultado_usuario:
        mensaje = "¡Has resuelto el misterio!"
        color = VERDE_CLARO
    else:
        mensaje = "Has fallado. El misterio continúa..."
        color = ROJO

    texto_resultado = renderizar_texto(mensaje, FUENTE_TITULO, color)
    ventana.blit(texto_resultado, texto_resultado.get_rect(center=(ANCHO_VENTANA // 2, 150)))

    # Mostrar solución real
    solucion = f"Era {historia['culpable']} con {historia['arma']} en {historia['lugar']}."
    texto_solucion = renderizar_texto(solucion, FUENTE_NORMAL, BLANCO)
    ventana.blit(texto_solucion, texto_solucion.get_rect(center=(ANCHO_VENTANA // 2, 250)))

    # Botón para volver al menú
    boton_volver = crear_boton("VOLVER AL MENÚ", FUENTE_NORMAL, BLANCO, AZUL_NOCHE, 250, 60)
    ventana.blit(boton_volver, (ANCHO_VENTANA // 2 - 125, 400))

    pygame.display.flip()

    while not continuar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                if pygame.Rect(ANCHO_VENTANA // 2 - 125, 400, 250, 60).collidepoint(x, y):
                    continuar = True

        reloj.tick(60)

