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
    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color
class Cuadrado(FiguraGeometrica, Color):
    def _init_(self, lado, color):
        FiguraGeometrica._init_(self, lado, lado)
        Color._init_(self, color)

    def area(self):
        return self._alto * self._ancho

    def _str_(self):
        return f"Cuadrado de color {self._color}, lado {self._alto}, área {self.area()}"


class Rectangulo(FiguraGeometrica, Color):
    def _init_(self, alto, ancho, color):
        FiguraGeometrica._init_(self, alto, ancho)
        Color._init_(self, color)

    def area(self):
        return self._alto * self._ancho

    def _str_(self):
        return f"Rectángulo de color {self._color}, alto {self._alto}, ancho {self._ancho}, área {self.area()}"