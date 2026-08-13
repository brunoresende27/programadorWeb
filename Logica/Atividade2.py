nome_completo = str(input("Digite seu nome completo: "))
#1 - Todas as letras maiúsculas
print(nome_completo.upper())

#2 - Todas as letras minúsculas
print(nome_completo.lower())

#3 - A quantidade de caracteres do nome
print(len(nome_completo))

#4 - A quantidade de caracteres do primeiro nome do usuário
primeiro_nome = nome_completo.split()[0]
print(len(primeiro_nome))

#5 - Verifique se o nome completo existe "Silva"
print("Silva" in nome_completo.title())

#6 - Mostre quantas vezes aparece a letra "a" no nome completo
print(nome_completo.lower().count("a"))

#7 - Mostre em qual posição aparece a letra "a" pela primeira vez
print(nome_completo.lower().find("a"))

#8 - Mostre em qual posição aparece a letra "a" pela última vez
print(nome_completo.lower().rfind("a"))

#9 - Mostre apenas o primeiro nome do usuário
print(nome_completo.split()[0])

#10 - Mostre apenas o último nome do usuário
print(nome_completo.split()[-1])
