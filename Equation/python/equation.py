
def calculate_x(str_eq):
    list_eq = str_eq.split(" = ")

    left_member  = list_eq[0] # "2x", "x", "3x"
    right_member = list_eq[1] # "10", "1"

    eq = float(right_member)

    n = 1
    if left_member != "x":
        num = left_member[:-1]
        n = float(num)
    
    return eq / n
