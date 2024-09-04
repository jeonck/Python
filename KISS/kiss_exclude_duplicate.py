# 복잡한 예제 
def get_user_status(is_active, is_admin):
    if is_active:
        if is_admin:
            return "Active Admin"
        else:
            return "Active User"
    else:
        return "Inactive User"
# 단순화 : 첫 번째 조건문을 빠르게 처리해 불필요한 중첩을 없앴습니다. 중첩된 조건문이 단순화되어 가독성이 높아졌습니다.
def get_user_status(is_active, is_admin):
    if not is_active:
        return "Inactive User"
    return "Active Admin" if is_admin else "Active User"
