# 복잡한 예제 
def find_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1
# 단순화 : 내장 함수 index()와 in을 활용해 반복문을 제거하고 더 직관적으로 바꿨습니다.  
def find_index(lst, value):
    return lst.index(value) if value in lst else -1
