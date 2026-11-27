#entrada de dados
nome = input("informe seu nome:").strip().title()
nota1 = int(input("Informe a 1 nota:"))
nota2 = int(input("Informe a 2 nota:"))

#lançamento de dados
media = (nota1+nota2)/2

#saída de dado
print(f"Média: (media)")

#estrutura de decisão
if media >= 7:
 print(f"{nome} está aprovado. ")
elif media >= 5:
 print(f"{nome}está de recuperação. ")
else:
 print(f"{nome} está reprovado. ")
