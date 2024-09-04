# 복잡한 예제  
def check_even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

# 단순화 : 리스트 내포를 사용해 한 줄로 간단히 작성했습니다. 코드가 더 직관적이고 간결해졌습니다. 
def check_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]
