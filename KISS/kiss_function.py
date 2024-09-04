# 복잡한 예제  
def calculate_area(shape, base=0, height=0, radius=0):
    if shape == 'rectangle':
        return base * height
    elif shape == 'triangle':
        return 0.5 * base * height
    elif shape == 'circle':
        return 3.14159 * radius * radius
    else:
        return None

# 단순화   
def calculate_rectangle_area(base, height):
    return base * height

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return 3.14159 * radius * radius
