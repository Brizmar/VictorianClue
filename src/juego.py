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
    def obtener_opciones_deduccion(self):
        historia = self.historia_actual

        sospechoso_real = historia["culpable"]
        arma_real = historia["arma"]
        lugar_real = historia["lugar"]

        # --- Sospechosos ---
        sospechosos = historia["sospechosos"]
        sospechosos_falsos = [s for s in sospechosos if s != sospechoso_real]
        opciones_sospechoso = random.sample(sospechosos_falsos, 2) + [sospechoso_real]
        random.shuffle(opciones_sospechoso)

        # --- Armas ---
        armas = historia["armas"]
        armas_falsas = [a for a in armas if a != arma_real]
        opciones_arma = random.sample(armas_falsas, 2) + [arma_real]
        random.shuffle(opciones_arma)

        # --- Lugares ---
        lugares_disponibles = list(historia["lugares"].keys())
        if lugar_real not in lugares_disponibles:
            lugares_disponibles.append(lugar_real)  # Por si está fuera de los lugares investigables
        lugares_falsos = [l for l in lugares_disponibles if l != lugar_real]
        opciones_lugar = random.sample(lugares_falsos, 2) + [lugar_real]
        random.shuffle(opciones_lugar)

        return opciones_sospechoso, opciones_arma, opciones_lugar

