# TODO: crie um programa que receba do usuárioo nome, a massa e
# altura, e calcule seu IMC (Indice de Massa cporporal).
# Apos mostrar o IMC, o programa deve informar de acordo com o 
# Valor do seu IMC:
# IMC < 18.5: "Usuário está abaixo do peso"
# IMC < 25: "Usuário está no peso ideal"
# IMC < 30: "Usuário está acima do peso"
# IMC < 35: "Usuário está obeso"
# IMC < 40: "Usuário está com obesidade nível 2"
# Se não estiver nenhuma dos casos acima:
# "Usuário está com obesidade mórbita"
# NOTE: imc = massa/(altura**2)

nome = input("informe seu nome:")
massa = float(input("informe sua massa").replace(",","."))
altura = float(input("informe sua altura(em metros)").replace(",","."))

imc = massa / (altura **2 )
if imc < 18.5:
    print("Usuário bestá abaixo do peso")
elif imc < 25:
    print("Usuário está no peso ideal")
elif imc < 30:
    print("Usuário está acima do peso")
elif imc < 35:
    print("Usuário está obeso")
elif imc < 40:
    print("Usuário está com obesidade nível 2")
else:
    print("Usuário está com obesidade mórbita")
