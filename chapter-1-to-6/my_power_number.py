#Kiem tra liệu b có phải là lũy thừa của a
def is_power(a, b):
    if b == 1:
        return False
    if a % b == 0:
        if a == b:
            return True
        else:
            return is_power(a / b, b)
    else:
        return False


print(is_power(9, 3))
