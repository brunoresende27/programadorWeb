import math

numero = float(input("Digite um número: "))
numero_cima = math.ceil(numero)
numero_baixo = math.floor(numero)

print("O número arredondado para cima é:",numero_cima)
print("O número arredondado para baixo é:",numero_baixo)

print("O número arredondado para cima é:{}".format(numero_cima))
print("O número arredondado para baixo é:{}".format(numero_baixo))

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = str(input("Digite o nome da sua cidade: "))

print("Olá, {}! Você tem {} anos e mora em {}.".format(nome, idade, cidade))
print(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}.")