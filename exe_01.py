gasolina = float(input("Informe o valor da gasolina:").replace(",","."))
etanol = float(input("Informe o valor do etanol:").replace(',','.'))

if etanol <= gasolina*0.75:
    print("Melhor abastecer com Etanol.")
else:
    print("Melhor abastecer com Gasolina.")
    
# TODO: Crie um programa que receba do usuário o valor da gasolina
# e do etanol, e informe para o usuário qual o melhor combustível
# para se abastecer.
# NOTE: compensa mais abastecer com etanol caso o valor do etanol
# corresponda a até 75% do valor da gasolina.
# NOTE: e não se esqueçam do detalhe mais importante de todos:
# DIVIRTAM-SE!!! 😎