input("Faça a conversão de temperatura aqui!")
x = int(input("Insira o valor da temperatura: "))
y = str(input("Escreva 'C' para Celsius, 'F' para Fahrenheit ou 'K' para Kelvin: "))
z = str(input("Escreva 'C' para Celsius, 'F' para Fahrenheit ou 'K' para Kelvin para fazer a conversão: "))

if y == "C":
    if z == "K":
        x = x + 273.15
    elif z == "F":
        x = x * 9/5 + 32
    else:
        x = x

if y == "F":
    if z == "C": 
        x = (x-32) * 5/9
    elif z == "K":
        x = (x - 32) * 5 / 9 + 273.15
    else:
        x = x

if y == "K":
    if z == "C":
        x = x - 273.15
    elif z == "F":
        x = (x - 273.15) * 9/5 + 32
    else:
        x = x

print("Resultado: ", x)