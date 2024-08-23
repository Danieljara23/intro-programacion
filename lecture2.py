# print("Hola")
# print('Hola')
# print("Hola 'Daniel'")
# print('Hola "Daniel"')
x = 5
name = input("Ingrese su nombre:...")
year = int(input("Ingrese su año de nacimiento"))

if year >= 1930 and year <= 1948:
    print("Eres un niño de la postguerra")
elif year >= 1949 and year <= 1968:
    print("Eres un baby boomer")
elif year > 2011:
    print("Eres un bebé Alfa")