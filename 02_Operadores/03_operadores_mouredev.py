# Operadores, me ayudan a realizar funciones aritmeticas (matemáticas)
print(5+5) # suma
print(5*5) # multiplicación
print(5-5) # resta
print(5/5) # división 
print(5**2) # potencia (elevado a n número)
print(53 % 7) # el famoso sobrante, usando el % divido el número por lo que le estoy indicando y de ahí saco el sobrante de esa división
print(10//3) # Me permite únicamente hacer la división, pero que lo deje en un número entero

# Cadenas de texto
print("Hola amigo" + " cómo estás?")
# No puedo utilizar otros operadores con sting
# Solo puedo usar funciones del mismo tipo al sumarlas, tengo que convertirlas si las quiero usar str(5)
print("Edad = " + str(5))
print("luis"*5)
# para multiplicar un strig, debe ser multiplicado con un número entero


#OPERADORES COMPARATIVOS
print(4==4)
print(4>8)
print(4<8)
print(4 >= 8)
print(4 <= 8)

"""
- Para usar comparativos con strig, lo que compara es el orden alfabetico y detiene la comparación en cuanto encuentre la primera diferencia
- ej. a < c (verdadero, ahí detiene la comparación y da "True")
- las mayúsculas tienen menos valor que las minúsculas
- ej A < a (true)
- No como tal, el número de caracteres de cada palabra.
- Las mayúsculas tienen un papel importante.
"""
print("Hola" == "Hola")
print("Hola" <= "Python")
print("Hola" >= "Python")
print("aaaa" < "bbbb")
print("aaaa" > "bbbb")
print("bbbb" == "bbbb")

## Vamos a utilizar la lógica booleana con operatores lógicos
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" == "Python")
# Ahora si yo quisiera invertir la lógica, lo que debo usar es "not" en lo que me ayuda es en 
print(not(3 < 4)) # Invertí el resultado del operador lógico que iba a dar verdadero. 

print("Hola" > "hola")
