# 복잡한 예제 
def get_max_value(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

# 단순화 : 내장 함수 max()를 사용하여 복잡한 반복문을 제거하고 코드를 간결하게 만들었습니다.  
def get_max_value(numbers):
    return max(numbers)
