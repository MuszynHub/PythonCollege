# Autor - Waląg Piotr
# Data utworzenia - 11.11.2022
# Cel programu - Obliczanie objętości, masy lub pola powierzchni brył na podstawie wprowadzonych danych
# Python 3.10

import numpy as np  # import biblioteki numpy która pomoże obliczać pierwiastki oraz funkcje trygonometryczne

print('Wybierz bryłę podając jej numer')
print('1. Kula')
print('2. Czworościan foremny')
print('3. Elipsoida')
print('4. Ostrosłup prosty o podstawie prostokątnej')
print('5. Stożek')
print('6. Walec')

figura = int(input('Podaj numer bryły: '))  # zmienna przechowująca wybór figury przez użytkownika
while figura <= 0 or figura > 6:
    try:
        if figura <= 0 or figura > 6:
            figura = int(input('Wartość musi być z przedziału <1-6>! Spróbuj ponownie: '))
    except:
        print('Podana wartość nie może być ciągiem znaków!')


def wybrana_figura(figura):  # funkcja zwracająca wybór figury do funkcji wyboru operacji
    match figura:
        case 1:
            return wybierz_operacje(1)
        case 2:
            return wybierz_operacje(2)
        case 3:
            return wybierz_operacje(3)
        case 4:
            return wybierz_operacje(4)
        case 5:
            return wybierz_operacje(5)
        case 6:
            return wybierz_operacje(6)


def wybierz_operacje(figura):  # funkcja zwracająca wybór operacji  do wyliczenia do następnej funkcji
    print("Wybierz którą wartość chcesz wyliczyć")
    print("1. Objętność")
    print("2. Masę")
    print("3. Polę powierzchni")
    operacja = int(input('Podaj numer bryły: '))
    while operacja <= 0 or operacja > 3:
        try:
            if operacja <= 0 or operacja > 3:
                operacja = int(input('Wartość musi być z przedziału <1-3>! Spróbuj ponownie: '))
        except:
            print('Podana wartość nie może być ciągiem znaków!')
    return rezultat(figura, operacja)


def rezultat(figura, operacja):  # finalna funkcja która otrzymuje wynik wyboru figury oraz wartosci do wyliczenia
    match figura:
        case 1:
            return kula(operacja)
        case 2:
            return czworoscian_foremny(operacja)
        case 3:
            return elipsoida(operacja)
        case 4:
            return ostroslup_prosty_o_podstawie_prostokatnej(operacja)
        case 5:
            return stozek(operacja)
        case 6:
            return walec(operacja)


def kula(operacja):  # funkcja obliczania wartości związanych z kulą
    r = float(input('Podaj promień kuli: '))  # zmienna r przechowująca długość promienia kuli
    while r < 0:
        try:
            if r < 0:
                r = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
        except:
            print('Podana wartość nie może być ciągiem znaków!')

    match operacja:
        case 1:
            objetosc = round((4 / 3) * np.pi * r ** 3, 2)
            print(objetosc)
        case 2:
            gestosc = float(input('Podaj gęstość kuli: '))
            objetosc = (4 / 3) * np.pi * r ** 3
            masa = round(gestosc * objetosc, 2)
            print(masa)
        case 3:
            polePowierzchni = round(4 * np.pi * r ** 2, 2)
            print(polePowierzchni)


def czworoscian_foremny(operacja):  # funkcja obliczania wartości związanych z czworościanem foremnym
    a = float(input('Podaj długość boku czworościanu foremnego: '))  # zmienna przechowująca długość boku czworościanu
    while a < 0:
        try:
            if a < 0:
                a = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
        except:
            print('Podana wartość nie może być ciągiem znaków!')

    match operacja:
        case 1:
            objetosc = round((1 / 12) * a ** 3 * np.sqrt(2), 2)
            print(objetosc)
        case 2:
            gestosc = float(input('Podaj gęstość czworoscianu foremnego: '))
            objetosc = (1 / 12) * a ** 3 * np.sqrt(2)
            masa = round(gestosc * objetosc, 2)
            print(masa)
        case 3:
            polePowierzchni = round(np.sqrt(3) * a ** 2, 2)
            print(polePowierzchni)


def elipsoida(operacja):  # funkcja obliczania wartości związanych z elipsoidą
    def wybor_osi():
        a = float(input("Podaj długość dłuższej półosi elipsoidy: "))  # zmienna przechowująca długość dłuższej półosi
        b = float(input("Podaj długość krótszej półosi elipsoidy: "))  # zmienna przechowująca długość krótszej półosi
        while a < 0:
            try:
                if a < 0:
                    a = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
            except:
                print('Podana wartość nie może być ciągiem znaków!')

        while b < 0:
            try:
                if b < 0:
                    b = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
            except:
                print('Podana wartość nie może być ciągiem znaków!')

        if a <= b:
            print("Zły wybór osi")
            return wybor_osi()  # ponowne poproszenie użytkownika o wartości długości półosi jeśli podane są błędne
        else:
            match operacja:
                case 1:
                    objetosc = round((4 / 3) * np.pi * a * b ** 2, 2)
                    print(objetosc)
                case 2:
                    gestosc = float(input('Podaj gęstość elipsoidy: '))
                    objetosc = ((4 / 3) * np.pi * a * b ** 2)
                    masa = round(gestosc * objetosc, 2)
                    print(masa)
                case 3:
                    e = np.sqrt(1 - (b ** 2 / a ** 2))
                    polePowierzchni = round(2 * np.pi * b * (b + (a / e) * np.arcsin(e)), 2)
                    print(polePowierzchni)

    wybor_osi()


def ostroslup_prosty_o_podstawie_prostokatnej(operacja):  # funkcja obliczania wartości związanych z ostrosłupem
    a = float(input("Podaj długość boku ostrosłupa: "))  # zmienna przechowująca długość boku ostrosłupa
    h = float(input("Podaj wysokość ostrosłupa: "))  # zmienna przechowująca długość wysokości ostrosłupa
    while a < 0:
        try:
            if a < 0:
                a = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
        except:
            print('Podana wartość nie może być ciągiem znaków!')

    while h < 0:
        try:
            if h < 0:
                h = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
        except:
            print('Podana wartość nie może być ciągiem znaków!')

    match operacja:
        case 1:
            objetosc = round((1 / 3) * a ** 2 * h, 2)
            print(objetosc)
        case 2:
            gestosc = float(input('Podaj gęstość ostrosłupa: '))
            objetosc = round((1 / 3) * a ** 2 * h, 2)
            masa = gestosc * objetosc
            print(masa)
        case 3:
            polePowierzchni = round(a ** a + (a ** 2 * np.sqrt(3)) / 4, 2)
            print(polePowierzchni)


def stozek(operacja):  # funkcja obliczania wartości związanych ze stożkiem
    r = float(input("Podaj promień stożka: "))  # zmienna przechowująca długość promienia stożka
    h = float(input("Podaj wysokość stożka: "))  # zmienna przechowująca długość wysokości stożka
    while r < 0:
        try:
            if r < 0:
                r = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
        except:
            print('Podana wartość nie może być ciągiem znaków!')

    while h < 0:
        try:
            if h < 0:
                h = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
        except:
            print('Podana wartość nie może być ciągiem znaków!')

    match operacja:
        case 1:
            objetosc = round((np.pi * r ** 2 * h) / 3, 2)
            print(objetosc)
        case 2:
            gestosc = float(input("Podaj gęstość stożka: "))
            objetosc = (np.pi * r ** 2 * h) / 3
            masa = round(gestosc * objetosc, 2)
            print(masa)
        case 3:
            l = float(input("Podaj długość tworzącej stożka: "))
            polePowierzchni = round(np.pi * r * (r + l), 2)
            print(polePowierzchni)


def walec(operacja):  # funkcja obliczania wartości związanych z walcem
    r = float(input("Podaj promień walca: "))  # zmienna przechowująca długość promienia walca
    h = float(input("Podaj wysokość walca: "))  # zmienna przechowująca długość wysokości walca
    while r < 0:
        try:
            if r < 0:
                r = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
        except:
            print('Podana wartość nie może być ciągiem znaków!')

    while h < 0:
        try:
            if h < 0:
                h = float(input('Wartość nie może być ujemna! Spróbuj ponownie: '))
        except:
            print('Podana wartość nie może być ciągiem znaków!')

    match operacja:
        case 1:
            objetosc = round(np.pi * r ** 2 * h, 2)
            print(objetosc)
        case 2:
            gestosc = float(input("POdaj gęstość walca: "))
            objetosc = np.pi * r ** 2 * h
            masa = round(gestosc * objetosc, 2)
            print(masa)
        case 3:
            polePowierzchni = round(2 * np.pi * r * (r + h), 2)
            print(polePowierzchni)


wybrana_figura(figura)  # wywołanie funkcji rozpoczynającej program
