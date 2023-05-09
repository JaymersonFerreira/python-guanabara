altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura**2)
print('IMC = {:.0f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso!!!')
elif 18.5 <= imc < 25:
    print('Peso ideal!!')
elif 25 <= imc < 30:
    print('Sobrepeso!!')
elif 30 <= imc < 40:
    print('Obesidade!!')
elif imc >= 40:
    print('Obesidade morbida!!')
