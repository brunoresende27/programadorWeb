# Chatbot de suporte:
print("Olá! Eu sou o Chatbot de suporte. Como posso ajudá-lo hoje?")
print("1. Problemas com login")
print("2. Segunda via do boleto")
print("3. Cancelamento do serviço")
print("4. Problemas com a internet")
print("5. Falar com um atendente")
print("6. Encerrar atendimento")

opcao = input("Digite o número da opção desejada: ")

if opcao == "1": # Se o usuário escolher a opção 1, vai entrar aqui
    print("Para problemas com login, por favor, siga os seguintes passos:")
    print("verifique se você está usando o e-mail e senha corretos.")
    print("Se ainda assim não conseguir acessar, tente redefinir sua senha.")
elif opcao == "2": # Se não se o usuário escolher a opção 2, vai entrar aqui
    cpf = input("Por favor, digite seu CPF para gerar a segunda via do boleto: ")
    mes = input("Digite o mês do boleto (MM): ")
    print("A segunda via do boleto foi gerada com sucesso e enviada para o seu e-mail.")
elif opcao == "3": # Se não se o usuário escolher a opção 3, vai entrar aqui
    confirmar = input("Tem certeza que deseja cancelar o serviço? (s/n): ").lower().strip()
    if confirmar == "s":
        print("O serviço foi cancelado com sucesso.")
    else:
        print("O cancelamento do serviço foi abortado.")
elif opcao == "4": # Se não se o usuário escolher a opção 4, vai entrar aqui
    print("Para problemas com a internet, por favor, siga os seguintes passos:")
    print("1. Verifique se o modem está ligado e conectado corretamente.")
    print("2. Reinicie o modem e o roteador.")
    confirmar = input("Se o problema persistir, deseja a visita de um técnico? (s/n): ").lower().strip()
    if confirmar == "s":
        print("Um técnico será agendado para visitar sua residência.")
    else:
        print("Ok, você será redirecionado para o menu principal.")
elif opcao == "5": # Se não se o usuário escolher a opção 5, vai entrar aqui
    print("Você será transferido para um atendente. Por favor, aguarde...")
elif opcao == "6": # Se não se o usuário escolher a opção 6, vai entrar aqui
    print("Obrigado por utilizar o Chatbot de suporte. Até mais!")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")