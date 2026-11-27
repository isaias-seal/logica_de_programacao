#entrada de dados 
nome = input("informe sueu nome: ").strip().title()
idade = int(input("Informe sua idade:"))

# estrutura de decisão 
if idade >=18:
 print(f"(nome) e maior de idade.")
else:
 print(f"(nome) é menor de idade.")