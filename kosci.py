import random

def gra():
    print("Trwa rzut kośćmi")
    
    x = 0
    while x + 2 < 6:
        print(".")
        print("..")
        print("...")
        print("....")
        print(".....")
        print("......")
        print("......")
        print(".....")
        print("....")
        print("...")
        print("..")
        print(".")
        x += 2
    
    print("Dealer wyrzucił: ")
    dl = random.randint(1, 6)
    print(dl)
    
    print("Twoja kolej")
    
    input()
    
    print("Trwa rzut kośćmi")
    
    x = 0
    while x + 2 < 6:
        print(".")
        print("..")
        print("...")
        print("....")
        print(".....")
        print("......")
        print("......")
        print(".....")
        print("....")
        print("...")
        print("..")
        print(".")
        x += 2
    
    print(imie + " Wyrzucił: ")
    pl = random.randint(1, 6)
    print(pl)

    if dl > pl:
        print("Przegrałeś! Dealer zgarnia kase")
    elif dl == pl:
        print("Remis! Jeszcze raz")
        return gra()
    elif dl < pl:
        print("Wygrałeś! Zgarniasz kase")

imie = input("Podaj imie: ")

print("Cześć " + imie)

print("Czy chcesz rzucić kośćmi?" )

print("Tak / Nie")

odp = input()

if odp == 'Nie':
    print("Pizda")
    print("Nie dziękuję za gre.")
elif odp == 'Tak':
    print("Ja pierwszy, następnie ty " + imie)
    print("Ok")
    
    wybor = input()
    
    
    if wybor == 'Ok':
        print("W takim razie Zaczynamy")
    elif wybor == 'Nie':
        print("Wypierdalaj nie ma takiej opcji")
    gra()
    print("Dzięki za grę")