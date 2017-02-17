
def fizzBuzzTazz(n):
    if n == 0:
        return ""
    return fizzBuzzTazzQuentin(n)

def fizzBuzzTazzQuentin(n):
    result = ""
    matches = [
        [3, "Fizz"],
        [5, "Buzz"],
        [7, "Tazz"],
        [11, "Mozz"],
        [13, "Vezz"]
    ]
    
    for m in matches:
        if n % m[0] == 0:
            result = result + m[1]
    return result


l = [""]*1000
l[3] = "Fizz"
l[5] = "Buzz"
l[7] = "Tazz"
l[11] = "Mozz"
l[13] = "Vezz"
def fizzBuzzTazzTom(n):
    s = ""
    y = 14
    for x in range (1,y):
        if n % x == 0:
            s += l[x]
    return s

def fizzBuzzTazzNaive(n):
    s = ""

    if n == 0:
        return s
    if n % 3 == 0:
        s += "Fizz"
    if n % 5 == 0:
        s += "Buzz"
    if n % 7 == 0:
        s += "Tazz"
    if n % 11 == 0:
        s += "Mozz"
    if n % 13 == 0:
        s += "Vezz"
    return s

