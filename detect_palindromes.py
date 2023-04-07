import math

'''
Palíndromo é uma palavra, frase ou sequência de caracteres que pode ser lida da mesma maneira tanto da esquerda para a direita quanto da direita para a esquerda.
'''

# Identificar se a palvra é palindroma
def is_palindrome(word):
    j = len(word)-1
    resultado = 0
    for i in range(len(word)):
        if word[i] == word[j]:
            resultado = resultado + 1
        if i >= j:
            break
        j = j -1
        
    if resultado == math.ceil(len(word)/2):
        return True
    else:
        return False
    
# a função chamar ela mesma
def is_palindrome_recursive(word):
     if len(word) <= 1:
         return True
     else:
         return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])
    
words = ["arara", "racecar", "carro", "cama", "level"]

for word in words:
    print(word)
    print(is_palindrome_recursive(word))
    print("\n")