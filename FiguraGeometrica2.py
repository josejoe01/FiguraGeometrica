class FiguraGeometrica:
    def _init_(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    def _str_(self):
        return f"Alto: {self._alto}, Ancho: {self._ancho}"

    def get_alto(self):
        return self._alto

    def set_alto(self, alto):
        self._alto = alto

    def get_ancho(self):
        return self._ancho

    def set_ancho(self, ancho):
        self._ancho = ancho


class Color:
    def _init_(self, color):
        self._color = color
