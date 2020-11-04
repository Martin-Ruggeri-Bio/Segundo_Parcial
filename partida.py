class Partida():
    def __init__(self, nombre_palabra, intentos, tipo_palabra, nombre_jugador):
        self.palabra = nombre_palabra
        self.tipo_palabra = tipo_palabra
        self.intentos = intentos
        self.nombre_jugador = nombre_jugador
        self.palabra_aciertos = nombre_palabra

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, value):
        if value == "":
            raise ValueError("no puede ser vacio")
        self._palabra = [i.upper() for i in value]

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, value):
        if value == "":
            raise ValueError("no puede ser vacio")
        self._tipo_palabra = value.upper()

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, value):
        if value < 1:
            raise ValueError("no puede ser menor a 1")
        self._intentos = value

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, value):
        if value == "":
            raise ValueError("no puede ser vacio")
        self._nombre_jugador = value.upper()

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, value):
        if value == "":
            raise ValueError("no puede ser vacio")
        self._palabra_aciertos = [None for i in value]
