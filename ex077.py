'''GUANABARA'''
'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:      #Analisa cada elemento em 'palavras'
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:     #Analisa cada letra em 'p'
        if letra.lower() in 'aeiou': #Verifica cada letra em palavra, se tiver a, e, i, o, u imprima a letra
            print(letra, end=' ')



