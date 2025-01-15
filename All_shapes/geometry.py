from math import degrees, acos, isclose

class Point:
    """Clase Punto que se utiliza para crear puntos.

    Inicializa el objeto Punto con los parámetros x e y.

        - param x: representa la coordenada del punto en el eje x.
        - param y: representa la coordenada del punto en el eje y.
    """
    
    definition: str = """Entidad geométrica abstracta 
    que representa una ubicación en un espacio."""

    def __init__(self, x: float = 0, y: float = 0):     
        self._x = x
        self._y = y

    def point_setter(self, new_x: float, new_y: float):
        """Coloca el punto en una nueva coordenada x y y.
        
        - param x: nueva posición en el eje x del punto.
        - param y: nueva posición en el eje y del punto.
        """
        self._x = new_x
        self._y = new_y

    def point_getter(self):
        """Devuelve las coordenadas x e y del punto."""
        return self._x, self._y

    def reset(self):
        """Coloca el punto en las coordenadas (0,0)."""
        self._x = 0
        self._y = 0

    def compute_distance(self, point: "Point") -> float:
        """Calcula la distancia entre dos puntos y la devuelve como un valor numérico.

        - param point: el segundo punto que se compara con el primer punto.
        """

        distance = ((self._x - point._x)**2 + (self._y - point._y)**2)**(0.5)
        return distance

    def __str__(self):
        """Método que devuelve una representación en cadena del punto."""
        return f"({self._x},{self._y})"
class Line:
    """Clase Línea utilizada para crear líneas.

    Inicializa un objeto Línea con los puntos inicial y final.

        - param start_point: representa el punto inicial de la línea.
        - param end_point: representa el punto final de la línea.

        La clase tiene un atributo llamado 'length' que indica la longitud de la línea,
        pero no es necesario inicializarlo directamente.
    """

    def __init__(self, start_point: "Point", end_point: "Point"):
        self.start = start_point
        self.end = end_point
        self.length = self.compute_length()

    def compute_length(self):
        """Calcula la distancia entre el punto inicial y el final, y la devuelve."""
        return self.start.compute_distance(self.end)

    def compute_slope(self):
        """Calcula la pendiente de la línea y la devuelve."""
        return (self.start._y - self.end._y) / (self.start._x - self.end._x)

    def compute_horizontal_cross(self):
        """Determina si la línea cruza el eje x y devuelve el punto de intersección."""
        if self.start._y * self.end._y > 0:
            return False
        if self.start._y == self.end._y:
            return False
        x_cross = self.start._x - (self.start._y * (
                  self.end._x - self.start._x)) / (self.end._y - self.start._y)
        return Point(x_cross, 0), True

    def compute_vertical_cross(self):
        """Determina si la línea cruza el eje y y devuelve el punto de intersección."""
        if self.start._x * self.end._x > 0:
            return False
        if self.start._x == self.end._x:
            return False
        y_cross = self.start._y - (self.start._x * (
                  self.end._y - self.start._y)) / (self.end._x - self.start._x)
        
        return Point(0, y_cross), True
    
    def __str__(self):
        """Método que devuelve una representación en cadena de la línea."""
        return f"Linea definida entre los puntos {self.start} y {self.end}."

class Shape:
    """Clase Figura utilizada para crear polígonos regulares e irregulares.
    
    Inicializa un objeto Figura con un valor que indica si es regular o no y una lista
    de vértices.
        
        - param is_regular: valor booleano que indica si la figura es regular o no.
        - param vertices: lista de instancias de puntos utilizados para crear las aristas
        (instancias de línea).
        
        Tiene los atributos adicionales:
        - edges: calculados usando el método calculate_edges.
        - inner_angles: calculados usando el método calculate_inner_angles.
    """

    def __init__(self, is_regular: "bool", vertices: "list[Point]"):
        self.is_regular = is_regular
        self.vertices = vertices
        self.edges = self.calculate_edges()
        self.inner_angles = self.compute_inner_angles()

    def calculate_edges(self) -> "list[Line]":
        """Calcula las aristas de la figura y verifica si son regulares como se indicó,
        devuelve una lista de instancias de la clase Line."""

        shape_edges = [] 
        
        for index in range(len(self.vertices)):
            start_point = self.vertices[index]
            end_point = self.vertices[(index + 1) % len(self.vertices)]
            shape_edges.append(Line(start_point, end_point))
        
        if self.is_regular:
            comparison_length = shape_edges[0].length
            for edge_length in shape_edges:
                if not (isclose(comparison_length, edge_length.length)):
                    raise ValueError("La figura debe ser regular como se indicó.")
        
        return shape_edges
    
    def compute_area(self) -> "float":
        """Calcula el área de la figura y devuelve su valor numérico."""
        pass

    def compute_perimeter(self) -> "float":
        """Calcula el perímetro de la figura y devuelve su valor numérico."""
        shape_perimeter = 0

        for edges in self.edges:
            shape_perimeter += edges.length
        return shape_perimeter
    
    def compute_inner_angles(self) -> "list":
        pass

    def __str__(self):
        vertices = [point.__str__() for point in self.vertices]
        return f"Figura definida con los siguientes vértices {vertices}."


class Rectangle(Shape):
    """Clase Rectángulo utilizada para crear rectángulos, hereda métodos
    y atributos de la clase Shape.
    
    Inicializa un objeto Rectángulo con los parámetros is_regular y vertices.
        
        - param is_regular: valor booleano que indica si la instancia es regular o no.
        - param vertices: lista de instancias de puntos utilizadas para crear las aristas
        (instancias de líneas).
    """
    def __init__(self, is_regular, vertices):
        if len(vertices) != 4: 
            raise ValueError("El rectángulo debe tener exactamente 4 vértices.")
        super().__init__(is_regular, vertices)

    def compute_area(self):
        """Calcula el área del rectángulo y la devuelve."""
        width = self.edges[0].length
        length = self.edges[1].length
        return width * length

    def compute_inner_angles(self):
        """Calcula los ángulos internos de la instancia, devuelve una lista con los ángulos internos."""
        return [90, 90, 90, 90]


class Square(Rectangle):
    """Clase Cuadrado utilizada para crear cuadrados, hereda métodos
    y atributos de la clase Rectángulo.
    
    Inicializa un objeto Cuadrado con los parámetros is_regular y vertices.
        
        - param is_regular: valor booleano que indica si la instancia es regular o no.
        - param vertices: lista de instancias de puntos utilizadas para crear las aristas
        (instancias de líneas).
    """
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        
        a, b, c, d = (edge.length for edge in self.edges)

        if self.is_regular == True:
            if not (a == b and b == c and c == d and d == a):
                raise ValueError (
                    "El cuadrado debe tener la misma longitud en todos los lados.")
        else:
            raise ValueError("La instancia de cuadrado debe ser regular.")

class Triangle(Shape):
    """Clase Triángulo utilizada para crear triángulos, hereda métodos
    y atributos de la clase Shape.
    
    Inicializa un objeto Triángulo con los parámetros is_regular y vertices.
        
        - param is_regular: valor booleano que indica si la instancia es regular o no.
        - param vertices: lista de instancias de puntos utilizadas para crear las aristas
        (instancias de líneas).
    """
    def __init__(self, is_regular, vertices):
        if len(vertices) != 3:
            raise ValueError("La instancia de triángulo debe tener 3 vértices.")
        super().__init__(is_regular, vertices)
    
    def compute_area(self):
        """Calcula el área del triángulo usando la fórmula de Herón."""
        a, b, c = (edge.length for edge in self.edges)
        semiperimeter = (a + b + c) / 2
        return (semiperimeter * (semiperimeter - a) * (semiperimeter - b) *
                (semiperimeter - c))**0.5
    
    def compute_inner_angles(self):
        """Calcula los ángulos internos, devuelve una lista con los ángulos internos de la instancia."""
        angles = []
        a, b, c = (edge.length for edge in self.edges)
        
        a_angle = degrees(acos(((b**2 + c**2) - a**2) / (2 * b * c)))
        b_angle = degrees(acos(((a**2 + c**2) - b**2) / (2 * a * c)))
        c_angle = degrees(acos(((a**2 + b**2) - c**2) / (2 * b * a)))
        
        angles.append(a_angle) 
        angles.append(b_angle) 
        angles.append(c_angle)
        return angles

class Equilateral(Triangle):
    """Clase Triángulo Equilátero utilizada para crear triángulos equiláteros, hereda métodos
    y atributos de la clase Triángulo.
    
    Inicializa un objeto Triángulo Equilátero con los parámetros is_regular y vertices.
        
        - param is_regular: valor booleano que indica si la instancia es regular o no.
        - param vertices: lista de instancias de puntos utilizadas para crear las aristas
        (instancias de líneas).
    """
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == False:
            raise ValueError("El triángulo equilátero debe ser regular.")
        
        # Los triángulos equiláteros deben tener la misma longitud en todos los lados
        a, b, c = (edge.length for edge in self.edges)
        
        if not (a == b and b == c):
            raise ValueError (
                "El triángulo equilátero debe tener la misma longitud en todos los lados.")

class Isosceles(Triangle):
    """Clase Triángulo Isósceles utilizada para crear triángulos isósceles, hereda métodos
    y atributos de la clase Triángulo.
    
    Inicializa un objeto Triángulo Isósceles con los parámetros is_regular y vertices.
        
        - param is_regular: valor booleano que indica si la instancia es regular o no.
        - param vertices: lista de instancias de puntos utilizadas para crear las aristas
        (instancias de líneas).
    """
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == True:
            raise ValueError("El triángulo isósceles no puede ser regular.")
        
        # Verificar si los vértices forman un triángulo isósceles
        a, b, c = (edge.length for edge in self.edges)
        
        isosceles_condition = (
            isclose(a, b) and not isclose(b, c) or
            isclose(b, c) and not isclose(c, a) or
            isclose(a, c) and not isclose(a, b)
        )

        if not isosceles_condition:
            raise ValueError(
        "El triángulo isósceles no puede ser formado con los vértices dados.")


class Scalene(Triangle):
    """Clase Triángulo Escaleno utilizada para crear triángulos escalenos, hereda métodos
    y atributos de la clase Triángulo.
    
    Inicializa un objeto Triángulo Escaleno con los parámetros is_regular y vertices.
        
        - param is_regular: valor booleano que indica si la instancia es regular o no.
        - param vertices: lista de instancias de puntos utilizadas para crear las aristas
        (instancias de líneas).
    """
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        if self.is_regular == True:
            raise ValueError("El triángulo escaleno no puede ser regular.")
        
        # Los triángulos escalenos tienen diferentes longitudes de lados
        a, b, c = (edge.length for edge in self.edges)

        scalene_condition = (
            not isclose(a, b) and 
            not isclose(b, c) and 
            not isclose(a, c)
        )

        if not scalene_condition:
            raise ValueError(
        "El triángulo escaleno no puede ser formado con los vértices dados.")


class Trirectangle(Triangle):
    """Clase Triángulo Rectángulo utilizada para crear triángulos rectángulos, hereda métodos
    y atributos de la clase Triángulo.
    
    Inicializa un objeto Triángulo Rectángulo con los parámetros is_regular y vertices.
        
        - param is_regular: valor booleano que indica si la instancia es regular o no.
        - param vertices: lista de instancias de puntos utilizadas para crear las aristas
        (instancias de líneas).
    """
    def __init__(self, is_regular, vertices):
        super().__init__(is_regular, vertices)
        # Verificar si la forma es regular
        if self.is_regular == True:
            raise ValueError("El triángulo rectángulo no puede ser regular.")

        a, b, c = sorted(edge.length for edge in self.edges)

        if not (c**2 - (10**-9)) < (a**2 + b**2) <= c**2:
            raise ValueError(
            "El triángulo rectángulo no puede ser formado con los vértices dados.")
