def unique_module():
    import All_shapes.geometry as Shapes

    # Lists to test all classes
    shape_list = [
        Shapes.Point(2, 1),
        Shapes.Point(5, 1),
        Shapes.Point(5.93, 3.85),
        Shapes.Point(3.5, 5.62),
        Shapes.Point(1.07, 3.85)
    ]
    rectangle_list = [
        Shapes.Point(0, 0), 
        Shapes.Point(4, 0), 
        Shapes.Point(4, 2), 
        Shapes.Point(0, 2)
    ]
    square_list = [
        Shapes.Point(0, 0),
        Shapes.Point(0, 3),
        Shapes.Point(3, 3),
        Shapes.Point(3, 0)
    ]
    
    normal_triangle_list = [
        Shapes.Point(6, 2),
        Shapes.Point(3, 1),
        Shapes.Point(5, 0)
    ]

    equilateral_triangle_list = [
        Shapes.Point(0, 0),
        Shapes.Point(2, 0),
        Shapes.Point(1, (3**0.5))
    ]
    
    isosceles_triangle_list = [
        Shapes.Point(0, 0),
        Shapes.Point(3, 0),
        Shapes.Point(1.5, 2)
    ]
    
    scalene_triangle_list = [
        Shapes.Point(0, 0),
        Shapes.Point(4, 0),
        Shapes.Point(3, 3)
    ]
    
    long_name_triangle_list = [
        Shapes.Point(0, 0),
        Shapes.Point(3, 0),
        Shapes.Point(0, 4)
    ]
    
    # Fundamental classes
    point = Shapes.Point(3, 2)
    line = Shapes.Line(Shapes.Point(3, 2), Shapes.Point(1, 2))
    shape = Shapes.Shape(False, shape_list)

    # Quadrilateral classes
    rectangle = Shapes.Rectangle(False, rectangle_list)
    square = Shapes.Square(True, square_list)

    # Triangle classes
    normal_triangle = Shapes.Triangle(False, normal_triangle_list)
    equilateral_triangle = Shapes.Equilateral(True, equilateral_triangle_list)
    isosceles_triangle = Shapes.Isosceles(False, isosceles_triangle_list)
    scalene_triangle = Shapes.Scalene(False, scalene_triangle_list)
    right_angled_triangle = Shapes.Triangle(False, long_name_triangle_list)
    
    # Prints
    print(
    f"""
    - Point, line and shape test:\n
    point definition: {point}
    distance between points: {point.compute_distance(Shapes.Point(5, 6))}
    line definition: {line}
    line slope: {line.compute_slope()}
    shape definition: {shape}
    shape's perimeter: {shape.compute_perimeter()}
    
    - Quadrilaterals test:\n
    rectangle's perimeter: {rectangle.compute_perimeter()}
    rectangle's area: {rectangle.compute_area()}²
    square's perimeter: {square.compute_perimeter()}
    square's area: {square.compute_area()}²

    - Triangles test:\n
    normal_triangle perimeter: {normal_triangle.compute_perimeter()}
    normal_triangle area: {normal_triangle.compute_area()}²
    
    equilateral_triangle perimeter: {equilateral_triangle.compute_perimeter()}
    equilateral_triangle area: {equilateral_triangle.compute_area()}²
    
    isosceles_triangle perimeter: {isosceles_triangle.compute_perimeter()}
    isosceles_triangle area: {isosceles_triangle.compute_area()}²
    
    scalene_triangle perimeter: {scalene_triangle.compute_perimeter()}
    scalene_triangle area: {isosceles_triangle.compute_area()}²
    
    right_angled_triangle perimeter:{right_angled_triangle.compute_perimeter()}
    right_angled_triangle area: {right_angled_triangle.compute_area()}²
    """)

def individual_modules():
    from Shapes import Point_class as Fundamentals
    from Shapes import Line_class as Fundamentals
    from Shapes import Shape_class as Fundamentals
    from Shapes import Rectangle_class as Fundamentals
    from Shapes import Square_class as Fundamentals
    from Shapes import Triangles_class as Fundamentals

    # Lists to test all classes
    shape_list = [
        Fundamentals.Point(2, 1),
        Fundamentals.Point(5, 1),
        Fundamentals.Point(5.93, 3.85),
        Fundamentals.Point(3.5, 5.62),
        Fundamentals.Point(1.07, 3.85)
    ]
    rectangle_list = [
        Fundamentals.Point(0, 0), 
        Fundamentals.Point(4, 0), 
        Fundamentals.Point(4, 2), 
        Fundamentals.Point(0, 2)
    ]
    square_list = [
        Fundamentals.Point(0, 0),
        Fundamentals.Point(0, 3),
        Fundamentals.Point(3, 3),
        Fundamentals.Point(3, 0)
    ]
    
    normal_triangle_list = [
        Fundamentals.Point(6, 2),
        Fundamentals.Point(3, 1),
        Fundamentals.Point(5, 0)
    ]

    equilateral_triangle_list = [
        Fundamentals.Point(0, 0),
        Fundamentals.Point(2, 0),
        Fundamentals.Point(1, (3**0.5))
    ]
    
    isosceles_triangle_list = [
        Fundamentals.Point(0, 0),
        Fundamentals.Point(3, 0),
        Fundamentals.Point(1.5, 2)
    ]
    
    scalene_triangle_list = [
        Fundamentals.Point(0, 0),
        Fundamentals.Point(4, 0),
        Fundamentals.Point(3, 3)
    ]
    
    long_name_triangle_list = [
        Fundamentals.Point(0, 0),
        Fundamentals.Point(3, 0),
        Fundamentals.Point(0, 4)
    ]
    
    # Fundamental classes
    point = Fundamentals.Point(3, 2)
    line = Fundamentals.Line(Fundamentals.Point(3, 2), Fundamentals.Point(1, 2))
    shape = Fundamentals.Shape(False, shape_list)

    # Quadrilateral classes
    rectangle = rectangle.Rectangle(False, rectangle_list)
    square = square.Square(True, square_list)

    # Triangle classes
    normal_triangle = Triangles.Triangle(False, normal_triangle_list)
    equilateral_triangle = Triangles.Equilateral(True, equilateral_triangle_list)
    isosceles_triangle = Triangles.Isosceles(False, isosceles_triangle_list)
    scalene_triangle = Triangles.Scalene(False, scalene_triangle_list)
    
    right_angled_triangle = Triangles.Triangular(False, long_name_triangle_list)

    # Prints
    print(
    f"""
    - Point, line and shape test:\n
    point definition: {point}
    distance between points: {point.compute_distance(Fundamentals.Point(5, 6))}
    line definition: {line}
    line slope: {line.compute_slope()}
    shape definition: {shape}
    shape's perimeter: {shape.compute_perimeter()}
    
    - Quadrilaterals test:\n
    rectangle's perimeter: {rectangle.compute_perimeter()}
    rectangle's area: {rectangle.compute_area()}²
    square's perimeter: {square.compute_perimeter()}
    square's area: {square.compute_area()}²

    - Triangles test:\n
    normal_triangle perimeter: {normal_triangle.compute_perimeter()}
    normal_triangle area: {normal_triangle.compute_area()}²
    
    equilateral_triangle perimeter: {equilateral_triangle.compute_perimeter()}
    equilateral_triangle area: {equilateral_triangle.compute_area()}²
    
    isosceles_triangle perimeter: {isosceles_triangle.compute_perimeter()}
    isosceles_triangle area: {isosceles_triangle.compute_area()}²
    
    scalene_triangle perimeter: {scalene_triangle.compute_perimeter()}
    scalene_triangle area: {isosceles_triangle.compute_area()}²
    
    right_angled_triangle perimeter:{right_angled_triangle.compute_perimeter()}
    right_angled_triangle area: {right_angled_triangle.compute_area()}²
    """)

# Run both tests
unique_module()
individual_modules()
