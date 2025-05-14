import pygame
import sys
from diseño import *
from utils import renderizar_texto, cargar_imagen, dividir_texto
from juego import *
import diseño

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

        titulo = renderizar_texto("Haz tu deducción", diseño.FUENTE_TITULO, diseño.DORADO)
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

    # Convertir el diccionario de lugares a lista de tuplas (nombre, pista)
    lugares = list(juego.historia_actual["lugares"].items())
    pistas_mostradas = set()

    fondo = cargar_imagen("fondo_exploracion.png", tamaño=(ANCHO_VENTANA, ALTO_VENTANA))

    botones = []
    for i, (nombre, pista) in enumerate(lugares):
        boton = crear_boton(nombre, FUENTE_NORMAL, BLANCO, AZUL_NOCHE, 250, 60)
        x = ANCHO_VENTANA // 2 - 130
        y = 180 + i * 90
        botones.append((boton, pygame.Rect(x, y, 250, 60), nombre, pista))

    while len(pistas_mostradas) < len(lugares):
        ventana.blit(fondo, (0, 0))

        titulo = renderizar_texto("¿Dónde quieres investigar?", FUENTE_TITULO, DORADO)
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO_VENTANA // 2, 60)))

        for boton, rect, _, _ in botones:
            ventana.blit(boton, rect.topleft)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                for i, (boton, rect, nombre, pista) in enumerate(botones):
                    if rect.collidepoint(x, y) and i not in pistas_mostradas:
                        mostrar_pista(ventana, nombre, pista)
                        pistas_mostradas.add(i)

        pygame.display.flip()
        reloj.tick(60)

def mostrar_pista(ventana, lugar, pista):
    reloj = pygame.time.Clock()
    continuar = False

    # Crea un fondo semitransparente
    overlay = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA))
    overlay.set_alpha(200)  # Transparencia
    overlay.fill((0, 0, 0))  # Fondo negro semitransparente

    # Crear botón de continuar
    boton = crear_boton("CONTINUAR", FUENTE_NORMAL, BLANCO, VERDE_PISTA, 200, 60)
    rect_boton = pygame.Rect(ANCHO_VENTANA // 2 - 100, ALTO_VENTANA - 100, 200, 60)

    # Procesar texto en líneas ajustadas
    palabras = pista.split()
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        test_linea = linea_actual + " " + palabra if linea_actual else palabra
        test_render = FUENTE_NORMAL.render(test_linea, True, BLANCO)
        if test_render.get_width() > ANCHO_VENTANA - 160:
            lineas.append(linea_actual)
            linea_actual = palabra
        else:
            linea_actual = test_linea
    if linea_actual:
        lineas.append(linea_actual)

    while not continuar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = pygame.mouse.get_pos()
                if rect_boton.collidepoint(x, y):
                    continuar = True

        ventana.blit(overlay, (0, 0))

        # Título del lugar
        titulo = renderizar_texto(lugar.upper(), FUENTE_TITULO, DORADO)
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO_VENTANA // 2, 100)))

        # Texto de la pista
        y = 180
        for linea in lineas:
            texto = renderizar_texto(linea, FUENTE_NORMAL, BLANCO)
            ventana.blit(texto, texto.get_rect(center=(ANCHO_VENTANA // 2, y)))
            y += 40

        # Botón de continuar
        ventana.blit(boton, rect_boton.topleft)

        pygame.display.flip()
        reloj.tick(60)

import pygame
import sys
import utils  # Cambiar diseño por utils

def escena_deduccion(ventana, juego):
    reloj = pygame.time.Clock()
    opciones_sospechoso, opciones_arma, opciones_lugar = juego.obtener_opciones_deduccion()

    seleccion = {"sospechoso": None, "arma": None, "lugar": None}
    etapa = "sospechoso"
    mensaje = ""

    def generar_botones(opciones):
        botones = []
        for i, opcion in enumerate(opciones):
            x = 100 + (i % 3) * 280
            y = 300
            boton = diseño.crear_boton(opcion, diseño.FUENTE_NORMAL, diseño.NEGRO, diseño.GRIS_CLARO, 200, 60)
            rect = boton.get_rect(topleft=(x, y))
            botones.append((opcion, boton, rect))
        return botones

    botones = generar_botones(opciones_sospechoso)

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                for opcion, boton, rect in botones:
                    if rect.collidepoint(evento.pos):
                        seleccion[etapa] = opcion
                        if etapa == "sospechoso":
                            etapa = "arma"
                            botones = generar_botones(opciones_arma)
                        elif etapa == "arma":
                            etapa = "lugar"
                            botones = generar_botones(opciones_lugar)
                        elif etapa == "lugar":
                            corriendo = False
                        break

        # Dibujar fondo
        ventana.fill(diseño.AZUL_NOCHE)

        # Títulos
        titulo = utils.renderizar_texto("Haz tu deducción", diseño.FUENTE_TITULO, diseño.DORADO)
        ventana.blit(titulo, utils.centrar_superficie(titulo, diseño.ANCHO_VENTANA, diseño.ALTO_VENTANA, 100))

        subtitulo_texto = {
            "sospechoso": "¿Quién fue el culpable?",
            "arma": "¿Con qué arma?",
            "lugar": "¿Dónde ocurrió?"
        }[etapa]
        subtitulo = utils.renderizar_texto(subtitulo_texto, diseño.FUENTE_SUBTITULO, diseño.BLANCO)
        ventana.blit(subtitulo, utils.centrar_superficie(subtitulo, diseño.ANCHO_VENTANA, diseño.ALTO_VENTANA, 180))

        # Botones
        for _, boton, rect in botones:
            ventana.blit(boton, rect)

        pygame.display.flip()
        reloj.tick(60)

    return seleccion["sospechoso"], seleccion["arma"], seleccion["lugar"]

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

