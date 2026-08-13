# import time

# for i in range(5,-1,-1):
#     print(i)
#     time.sleep(1)

# print("Feliz Ano Novo!")

# for i in range(2,101,2):
#     print(i)

# soma = 0

# for i in range(1,500,2):
#     if i % 3 == 0:
#         soma += i

# print(f'A soma dos números ímpares de 1 a 500 que são múltiplos de 3 é: {soma}')

# numero = int(input("Digite um número para tabuada: "))

# for i in range(1,11):
#     print(f"{numero} x {i} = {numero * i}")

# numero = int(input("Digite um número: "))
# divisor = 0

# for i in range(1, numero + 1):
#     if numero % i == 0:
#         divisor += 1

# if divisor == 2:
#     print(f"{numero} é um número primo.")
# else:
#     print(f"{numero} não é um número primo.")


import datetime

# qtd_maior = 0
# qtd_menor = 0

# for i in range(1, 6):
#     ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
#     idade = datetime.datetime.now().year - ano_nascimento

#     if idade >= 18:
#         qtd_maior = qtd_maior + 1
#     else:
#         qtd_menor += 1

# print(f"Quantidade de pessoas maiores de idade: {qtd_maior}")
# print(f"Quantidade de pessoas menores de idade: {qtd_menor}")

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa (em kg): "))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso é: {maior} kg")
print(f"O menor peso é: {menor} kg")