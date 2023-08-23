#Ejercicio #2
p = input("Ingresa una palabra: ")
palindromo = True  
for i in range(len(p)):
    if p[i] != p[-(i + 1)]:
        palindromo = False
        break
if palindromo:
    print("La palabra que ingresaste es un palíndromo!")
else:
    print("La palabra ingresaste no es un palíndromo.")