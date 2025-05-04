import random
from utils import cargar_json

class Juego:
    def __init__(self, ruta_json):
        self.historias = cargar_json(ruta_json)
        self.historia_actual = None
        self.lugares_visitados = set()

    def inicializar(self):
        """Selecciona una historia al azar y reinicia el progreso."""
        self.historia_actual = random.choice(self.historias)
        self.lugares_visitados = set()

    def obtener_lugares_disponibles(self):
        """Devuelve los lugares que aún no han sido visitados."""
        todos_lugares = list(self.historia_actual["pistas"].keys())
        return [l for l in todos_lugares if l not in self.lugares_visitados]

    def visitar_lugar(self, lugar):
        """Marca un lugar como visitado y devuelve la pista correspondiente."""
        self.lugares_visitados.add(lugar)
        return self.historia_actual["pistas"][lugar]

    def pistas_restantes(self):
        """Devuelve la cantidad de pistas que aún faltan por ver."""
        return 3 - len(self.lugares_visitados)

    def verificar_respuesta(self, sospechoso, arma, lugar):
        """Verifica si la elección del jugador coincide con la historia real."""
        historia = self.historia_actual
        return (
            sospechoso == historia["culpable"] and
            arma == historia["arma"] and
            lugar == historia["lugar"]
        )
