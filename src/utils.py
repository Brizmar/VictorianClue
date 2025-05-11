import os
import pygame
import json

def cargar_sonido(nombre_archivo):
    ruta = os.path.join("assets", "sounds", nombre_archivo)
    try:
        return pygame.mixer.Sound(ruta)
    except pygame.error as e:
        print(f"Error al cargar el sonido: {e}")
        return None

def cargar_imagen(nombre_archivo, tamaño=None):
    ruta = os.path.join("assets", "img", nombre_archivo)
    try:
        imagen = pygame.image.load(ruta).convert_alpha()
        if tamaño:
            imagen = pygame.transform.scale(imagen, tamaño)
        return imagen
    except pygame.error as e:
        print(f"Error al cargar la imagen: {e}")
        return None

def cargar_json(nombre_archivo):
    ruta = os.path.join("data", nombre_archivo)
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo} no encontrado.")
        return []

def renderizar_texto(texto, fuente, color):
    """Renderiza un texto con una fuente y color específicos."""
    return fuente.render(texto, True, color)

def centrar_superficie(superficie, ancho_ventana, alto_ventana, y=0):
    """Centra horizontalmente una superficie. Se puede indicar la posición Y."""
    rect = superficie.get_rect(center=(ancho_ventana // 2, y))
    return rect

def dividir_texto(texto, fuente, max_ancho):
    palabras = texto.split()
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        linea_prueba = linea_actual + palabra + " "
        if fuente.size(linea_prueba)[0] <= max_ancho:
            linea_actual = linea_prueba
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "
    if linea_actual:
        lineas.append(linea_actual.strip())

    return lineas
