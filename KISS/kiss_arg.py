# 복잡한 예제 
def greet_user(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Guest!")

# 단순화 : 기본 인수를 활용해 조건문 없이 간단하게 바꿨습니다. 코드의 가독성이 향상되었습니다.  
def greet_user(name="Guest"):
    print(f"Hello, {name}!")
