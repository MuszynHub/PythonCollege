import matplotlib.pyplot as plt
import numpy as np

# Pobranie od użytkownika współczynników wielomianu 4 stopnia
a = input("Podaj wartość współczynnika a wielomianu 4 stopnia: ")
b = input("Podaj wartość współczynnika b wielomianu 4 stopnia: ")
c = input("Podaj wartość współczynnika c wielomianu 4 stopnia: ")
d = input("Podaj wartość współczynnika d wielomianu 4 stopnia: ")

# Pobranie od użytkownika zakres w jakim ma zostać wyświetlona funkcja
ymin = float(input('Zakres minimalny osi Y'))
ymax = float(input('Zakres maksymalny osi Y'))
if ymin >= ymax:
    print('Błędny zakres osi Y')
    quit()
xmin = float(input('Zakres minimalny osi X'))
xmax = float(input('Zakres maksymalny osi X'))
if xmin >= xmax:
    print('Błędny zakres osi X')
    quit()

# Ustawienie zakresu podanego przez użytkownika
plt.axis([xmin, xmax, ymin, ymax])

# Wypisanie równania wielomianu
print(a, end="x^4")
if int(b)<0:
    print(b, end="x^3")
else:
    print('+' + b, end="x^3")
if int(c)<0:
    print(c, end="x^2")
else:
    print('+' + c, end="x^2")
if int(d)<0:
    print(d, end="x")
else:
    print('+' + d, end="x")

# Ustawienie wartości X na zakres podany przez użytkownika oraz obliczenie wartości Y
def funkcja(x,a,b,c,d):
    return a*(x**4)+b*(x**3)+c*(x**2)+d*x

xlist = np.arange(xmin, xmax, (xmax - xmin)/100)
ylist = funkcja(xlist, float(a), float(b), float(c), float(d))

# Wyświetlenie wykresu funkcji oraz opisanie osi X oraz osi Y
plt.plot(xlist, ylist)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()