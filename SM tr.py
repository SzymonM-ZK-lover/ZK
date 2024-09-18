a = int(input())
b = int(input())
c = int(input())
if a == b or b == c or c == a:
    print("to jest tr rownoramienny")
else:
    print("to nie jest tr rownoramienny")
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("to jest tr prost")
else:
    print("to nie jest tr prost")
if a + b > c or b + c > a or c + a > b:
    print("to jest tr")
else:
    print("to nie jest tr")

