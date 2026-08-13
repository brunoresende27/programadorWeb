# media_idade = 0
# old_man = ""
# qtd_mulheres = 0
# idade_homem = 0
# for i in range(1,7):
#     nome = input(f"Digite o nome do {i}º pessoa: ")
#     idade = int(input(f"Digite a idade do {i}º pessoa: "))
#     sexo = input(f"Digite o sexo do {i}º pessoa (M/F): ").upper().strip()
#     total_idade += idade

#     if sexo == "M" and idade > idade_homem:
#         idade_homem = idade
#         old_man = nome

#     if sexo == "F" and idade < 20:
#         qtd_mulheres += 1

#     if i == 6:
#         media_idade = total_idade / 6

# print(f"A média de idade do grupo é: {media_idade:.2f} anos.")

# if old_man != "":
#     print(f"O homem mais velho é {old_man} com {idade_homem} anos.")
# else:
#     print("Não há homens no grupo.")

# if qtd_mulheres > 0:
#     print(f"A quantidade de mulheres com menos de 20 anos é: {qtd_mulheres}.")
# else:
#     print("Não há mulheres com menos de 20 anos no grupo.")

print("Quebrando o laço de repetição")
para = ""

# for i in range(1,6):
#     para = input("Digite N para sair do laço de repetição: ").upper().strip()
#     if para == "N":
#         break
#     print(f"passou no laço {i} vezes")

# print("Fora do laço de repetição")

# while True:
#     para = input("Digite N para sair do laço de repetição: ").upper().strip()
#     if para == "N":
#         break
#     print("Você não digitou N, o laço continua.")

# print("Fora do laço de repetição")


# print("Instrução continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro do laço.", i)
# print("Fora do laço.")

nome = input("Digite o seu nome: ").upper().strip()
for letra in nome:
    if letra in "AEIOU":
        continue
    print(letra)
