#entrada
nome = input("informe o nome.")
idade = input("informe sua idade;")
altura = input("informe sua altura").replace(",", ".")

# nova linha
idade = int(idade)
altura = float(altura)

#saida de dados
print(f"Nome: {nome}. Tipo: {type(nome)}")
print(f"Idade: {idade}. Tipo: {type(idade)}")
print(f"Altura: {altura}. metros. Tipo: {type(altura)}")



