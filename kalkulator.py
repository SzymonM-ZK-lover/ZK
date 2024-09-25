import math

def szescian():
    a = float(input("długość boku sześcianu w cm: "))
    pole = 6 * a ** 2
    objetosc = a ** 3
    return f"Pole: {pole}, Objetość: {objetosc}"

def prostopadloscian():
    a = float(input("długość boku w cm: "))
    b = float(input("długość boku w cm: "))
    c = float(input("długość boku w cm: "))
    pole = 2 * a * b + 2 * b * c + 2 * a * c
    objetosc = a * b * c
    return f"Pole: {pole}, objętość: {objetosc}"

def graniastoslup():
    a = float(input("długość boku a podstawy w cm: "))
    b = float(input("długość boku b podstawy w cm: "))
    h = float(input("wysokość graniastosłupa w cm: "))
    poleP = a * b
    poleB = 2 * (a * h) + 2 * (b * h)
    pole = 2 * poleP + poleB
    objetosc = poleP * h
    return f"Pole: {pole}, Objętość: {objetosc}"

def walec():
    r = float(input("promień podstawy walca w cm: "))
    h = float(input("wysokość walca w cm: "))
    poleP = math.pi * r ** 2
    pole = 2 * poleP + 2 * math.pi * r * h
    objetosc = poleP * h
    return f"Pole: {pole}, Objętość: {objetosc}"

def stozek():
    r = float(input("promień podstawy stożka w cm: "))
    h = float(input("wysokość stożka w cm: "))
    poleP = math.pi * r ** 2
    l = math.sqrt(r ** 2 + h ** 2)  # Tworząca stożka
    pole = poleP + math.pi * r * l
    objetosc = (1/3) * poleP * h
    return f"Pole: {pole}, Objętość: {objetosc}"

def kula():
    r = float(input("promień kuli w cm: "))
    pole = 4 * math.pi * r ** 2
    objetosc = (4/3) * math.pi * r ** 3
    return f"Pole: {pole}, Objętość: {objetosc}"

def kolo():
    r = float(input("promień koła w cm: "))
    pole = math.pi * r ** 2
    obwod = 2 * math.pi * r
    return f"Pole: {pole}, Obwód: {obwod}"

def romb():
    d1 = float(input("długość pierwszej przekątnej rąbu w cm: "))
    d2 = float(input("długość drugiej przekątnej rąbu w cm: "))
    pole = (d1 * d2) / 2
    a = math.sqrt((d1 / 2) ** 2 + (d2 / 2) ** 2)
    obwod = 4 * a
    return f"Pole: {pole}, Obwód: {obwod}"

def wysokosc_trojkata():
    a = float(input("długość ramienia trójkąta w cm: "))
    b = float(input("długość podstawy trójkąta w cm: "))
    h = math.sqrt(a ** 2 - (b / 2) ** 2)
    return f"Wysokość (w cm): {h}"

def przekatna_kwadratu():
    bok = float(input("długość boku kwadratu w cm: "))
    przekatna = bok * math.sqrt(2)
    return f"Przekątna w cm: {przekatna}"

def tpitagoras():
    a = float(input("długość przyprostokątnej a w cm: "))
    b = float(input("długość przyprostokątnej b w cm: "))
    c = math.sqrt(a ** 2 + b ** 2)
    return f"Długość przeciwprostokątnej w cm: {c}"


def menu():
    while True:
        print("Kalkulator figur geometrycznych")
        print("1. Sześcian")
        print("2. Prostopadłościan")
        print("3. Graniastosłup")
        print("4. Walec")
        print("5. Stożek")
        print("6. Kula")
        print("7. Koło")
        print("8. Romb")
        print("9. Wysokość trójkąta równoramiennego")
        print("10. Przekątna kwadratu")
        print("11. Twierdzenie Pitagorasa")
    
        choice = input("Wybierz opcję (0-11): ")

        if choice == '1':
            print(szescian())
        elif choice == '2':
            print(prostopadloscian())
        elif choice == '3':
            print(graniastoslup())
        elif choice == '4':
            print(walec())
        elif choice == '5':
            print(stozek())
        elif choice == '6':
            print(kula())
        elif choice == '7':
            print(kolo())
        elif choice == '8':
            print(romb())
        elif choice == '9':
            print(wysokosc_trojkata())
        elif choice == '10':
            print(przekatna_kwadratu())
        elif choice == '11':
            print(tpitagoras())
        else:
            print("Nie ma takiej opcji")

menu()

