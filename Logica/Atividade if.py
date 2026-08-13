# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))

# if numero1 > numero2:
#     print("O maior número é: ", numero1)
# elif numero2 > numero1:
#     print("O maior número é: ", numero2)
# else:
#     print("Os números são iguais.")

# altura = float(input("Digite a altura em metros: "))
# sexo = str(input("Digite o sexo Masculino ou Feminino (M/F): ")).upper()
# if sexo == "M":
#     peso_ideal = (72.7 * altura) - 58
#     print("O peso ideal para homens é: ", peso_ideal, "kg")
# elif sexo == "F":
#     peso_ideal = (62.1 * altura) - 44.7
#     print("O peso ideal para mulheres é: ", peso_ideal, "kg")
# else:
#     print("Opção inválida. Por favor, digite 'M' para Masculino ou 'F' para Feminino.")

# altura = float(input("Digite a altura em metros: "))
# peso = float(input("Digite o peso em kg: "))
# imc = peso / (altura * altura)
# print("O seu IMC é: ", imc)
# if imc <= 18.5: # if é o SE e os : é o então
#     print("Abaixo do peso")
# elif imc <= 24.9: # elif é o SENÃO SE e os : é o então
#     print("Peso normal")
# elif imc <= 29.9: 
#     print("Sobrepeso")
# else: # else é o SENÃO e os : é o então
#     print("Obesidade")

# numero = int(input("Digite um número inteiro: "))
# print(numero," X 1 = ", numero * 1)
# print(numero," X 2 = ", numero * 2)
# print(numero," X 3 = ", numero * 3)
# print(numero," X 4 = ", numero * 4)
# print(numero," X 5 = ", numero * 5)
# print(numero," X 6 = ", numero * 6)
# print(numero," X 7 = ", numero * 7)
# print(numero," X 8 = ", numero * 8)
# print(numero," X 9 = ", numero * 9)
# print(numero," X 10 = ", numero * 10)


# Faça um programa que compare 3 números e exiba o maior deles. 
# Caso os números sejam iguais, exiba uma mensagem informando que todos 
# são iguais.

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))

# if num1 == num2 == num3:
#     print("Todos os números são iguais.")
# else:
#     if num1 >= num2 and num1 >= num3:
#         maior = num1
#         if num2 <= num3:
#             menor = num2
#             intermediario = num3
#         else:
#             menor = num3
#             intermediario = num2
#     elif num2 >= num1 and num2 >= num3:
#         maior = num2
#         if num1 <= num3:
#             menor = num1
#             intermediario = num3
#         else:
#             menor = num3
#             intermediario = num1
#     else:
#         maior = num3
#         if num1 <= num2:
#             menor = num1
#             intermediario = num2
#         else:
#             menor = num2
#             intermediario = num1

#     print("O menor número digitado foi: ", menor)
#     print("O número intermediário digitado foi: ", intermediario)
#     print("O maior número digitado foi: ", maior)

# Faça um program que receba a idade do usuário e informe se ele é uma 
# criança (0 a 12 anos), 
# adolescente (13 a 17 anos), 
# adulto (18 a 59 anos) ou 
# idoso (60 anos ou mais).

# idade = int(input("Digite a sua idade: "))

# if idade <= 12:
#     print("Você é uma criança.")
# elif idade <= 17:
#     print("Você é um adolescente.")
# elif idade <= 59:
#     print("Você é um adulto.")
# else:
#     print("Você é um idoso.")

# Faça um programa que o usuário deve digitar a quantidade de memória RAM e dependendo da quantidade
# o sistema deve calcular um desconto no valor total da compra.
# Se a quantidade de memória RAM for maior ou igual a 2, o desconto será de 5%.
# Se a quantidade de memória RAM for maior ou igual a 4, o desconto será de 10%.

# print("Você está adquirindo memória RAM de 8GB para o seu computador no valor de R$ 300,00.")
# qtd = int(input("Por favor, digite a quantidade de memória RAM que deseja comprar (1, 2, 3, 4...): "))

# if qtd >= 4:
#     desconto = 0.10
#     valor_desconto = 300 * qtd * desconto
#     valor_total = 300 * qtd - valor_desconto
#     print("Você recebeu um desconto de 10%. O valor total da compra é: R$ ", valor_total)
# elif qtd >= 2:
#     desconto = 0.05
#     valor_total = 300 * qtd * (1 - desconto)
#     print("Você recebeu um desconto de 5%. O valor total da compra é: R$ ", valor_total)
# else:
#     valor_total = 300 * qtd
#     print("Você não recebeu desconto. O valor total da compra é: R$ ", valor_total)


# Minha casa minha divida
# Faça um programa que receba:
# O valor do imóvel
# O valor da renda do comprador
# O valor da entrada
# O programa deve calacular o valor máximo da parcela que o comprador pode pagar, que é 30% da renda.
# e quanto meses será necessário para pagar o imóvel, considerando o valor máximo da parcela

valor_imovel = float(input("Digite o valor do imóvel: R$ "))
renda = float(input("Digite o valor da sua renda: R$ "))
valor_entrada = float(input("Digite o valor da entrada: R$ "))

valor_financiado = valor_imovel - valor_entrada
valor_parcela_maxima = renda * 0.3
numero_meses = valor_financiado / valor_parcela_maxima
print("O valor máximo da parcela que você pode pagar é: R$ ", round(valor_parcela_maxima, 2))
print("O número de meses necessário para pagar o imóvel é: ", numero_meses) 
