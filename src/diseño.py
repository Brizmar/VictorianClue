import pygame

# Inicializamos fuentes de Pygame
pygame.font.init()

# Paleta de colores
BLANCO       = (255, 255, 255)
NEGRO        = (0, 0, 0)
GRIS_OSCURO  = (40, 40, 40)
GRIS_CLARO   = (200, 200, 200)
ROJO         = (180, 50, 50)
DORADO       = (212, 175, 55)
AZUL_NOCHE   = (20, 30, 60)
VERDE_PISTA  = (50, 150, 100)
VERDE_CLARO = (144, 238, 144)

# 🖋️ Fuentes (asegúrate de tener alguna personalizada si lo deseas)
FUENTE_TITULO = pygame.font.SysFont("georgia", 48, bold=True)
FUENTE_SUBTITULO = pygame.font.SysFont("georgia", 32)
FUENTE_NORMAL = pygame.font.SysFont("georgia", 24)
FUENTE_PEQUENA = pygame.font.SysFont("georgia", 18)

# 📏 Dimensiones base
ANCHO_VENTANA = 1024
ALTO_VENTANA = 768

# Función para crear un botón básico
def crear_boton(texto, fuente, color_texto, color_fondo, ancho, alto):
    boton = pygame.Surface((ancho, alto))
    boton.fill(color_fondo)
    texto_render = fuente.render(texto, True, color_texto)
    rect_texto = texto_render.get_rect(center=(ancho // 2, alto // 2))
    boton.blit(texto_render, rect_texto)
    return boton
