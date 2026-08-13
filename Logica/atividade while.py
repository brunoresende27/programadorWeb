# qtd_alunos = int(input("Digite a quantidade de alunos: "))

# i = 0
# while qtd_alunos > i:
#     i += 1
#     aluno = input("Digite o nome do aluno: ")
#     print(f"Seja Bem-vindo, Aluno {i}: {aluno}")

# print("Fim do programa.")

# senha = "1234"

# senha_digitada = input("Digite a senha: ")

# while senha_digitada != senha:
#     print("Senha incorreta! Tente novamente.")
#     senha_digitada = input("Digite a senha: ")

# print("Senha correta! Acesso permitido.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
opcao = 0
while opcao != 5:
    print("Escolha uma opção:")
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Qual é o maior")
    print("4 - Escolher novos valores")
    print("5 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        resultado = numero1 + numero2
        print(f"A soma de {numero1} e {numero2} é: {resultado}")
        opcao = int(input("Digite 0 para continuar ou 5 para sair: "))
    elif opcao == 2:
        resultado = numero1 * numero2
        print(f"A multiplicação de {numero1} e {numero2} é: {resultado}")
        opcao = int(input("Digite 0 para continuar ou 5 para sair: "))
    elif opcao == 3:
        if numero1 > numero2:
            print(f"O maior número entre {numero1} e {numero2} é: {numero1}")
        elif numero2 > numero1:
            print(f"O maior número entre {numero1} e {numero2} é: {numero2}")
        else:
            print("Os números são iguais.")
        opcao = int(input("Digite 0 para continuar ou 5 para sair: "))
    elif opcao == 4:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
    elif opcao == 5:
        print("Saindo do programa...") 
    else:
        print("Opção inválida. Tente novamente.")

print("Fim do programa.")