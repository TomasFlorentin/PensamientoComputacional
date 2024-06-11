# Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
# ● la suma de ambos números
# ● la resta de ambos números
# ● la multiplicación de ambos números
# ● la división entera de ambos números
# ● el resto
# Más adelante podríamos crear nuestra propia calculadora :)

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2
resto = num1 % num2


print("La suma entre", num1, "y", num2, "es: ", suma)
print("La resta entre", num1, "y", num2, "es: ", resta)
print("La multiplicación entre", num1, "y", num2, "es: ", multi)
print("La división entre", num1, "y", num2, "es: ", divi)
print("El resto entre", num1, "y", num2, "es: ", resto)