# 복잡한 예제 
def greet_users(names):
    for name in names:
        if name:
            print(f"Hello, {name}!") 
# 단순화 : filter()를 사용해 None 값을 자동으로 걸러내고 불필요한 조건문을 없앴습니다. 코드를 더 간단하게 만듭니다.
def greet_users(names):
    for name in filter(None, names):
        print(f"Hello, {name}!")
