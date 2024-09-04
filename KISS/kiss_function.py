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

# 단순화 ; 각 도형에 대해 별도의 함수를 만들어 코드가 단순해졌습니다. 불필요한 조건문이 사라졌고, 이해하기 쉬워졌습니다.
def calculate_rectangle_area(base, height):
    return base * height

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return 3.14159 * radius * radius
