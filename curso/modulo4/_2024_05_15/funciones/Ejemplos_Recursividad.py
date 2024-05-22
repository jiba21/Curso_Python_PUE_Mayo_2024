# Funciones recursivas
def factorial(n): # n=6    6! = 6.5.4.3.2.1
    return 1 if n == 1 else n * factorial(n - 1)

print('Factorial =>', factorial(6))

print('-' * 80)

def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci =>", fibonacci(8)) # 0, 1, 1, 2, 3, 5, 8, 13, 21

print('-' * 80)

def sumas(n): # n=5 = 5 + 4 + 3 + 2 + 1
    return 1 if n == 1 else n + sumas(n - 1) # n=5 + sumas(4) # 15
                                             # n=4 + sumas(3) # 10
                                             # n=3 + sumas(2) # 6
                                             # n=2 + sumas(1) # 3
                                             # n=1

sumatorio = sumas(5)
print("Sumatorio =>", sumatorio)


# Función que devuelve una lista con todas las ocurriencias de una palabra en un texto
# proporcionado.

def ocurriencias(texto, palabra, palabras=[]):
    posicion = texto.lower().find(palabra.lower())
    if posicion == -1:
        return palabras
    else:
        word = texto[posicion:]
        word = word[:word.find(' ')] if word.find(' ') != -1 else word
        palabras.append(word)
        texto = texto[posicion + len(palabra):]
        return ocurriencias(texto, palabra, palabras)

texto = 'NUEva frase frase nuEVa Nueva'

print(ocurriencias(texto, 'nueva'))
