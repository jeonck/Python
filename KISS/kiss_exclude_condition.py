# 복잡한 예제
def calculate_discount(price, discount_percentage):
    if discount_percentage > 0:
        discount = price * (discount_percentage / 100)
        discounted_price = price - discount
        return discounted_price
    else:
        return price


# 단순화 : 불필요한 조건문을 제거하고 수식을 간단히 표현했습니다. 더 직관적이고 이해하기 쉬운 코드가 되었습니다.
def calculate_discount(price, discount_percentage):
    return price * (1 - discount_percentage / 100)
