print('Escolha um modelo de veículo:')
print('1 - Volkswagen')
print('2 - Ford')
print('3 - Chevrolet')
print('4 - Fiat')
marca = input('Digite o número correspondente à marca desejada de 1 a 4: ')

if marca == '1':
    print('Você escolheu Volkswagen.')
    print('Escolha um modelo de Volkswagen:')
    print('1 - Gol')
    print('2 - Polo')
    print('3 - Fusca')
    modelo = input('Digite o número correspondente ao modelo desejado de 1 a 3: ')
    if modelo == '1':
        print('Você escolheu o modelo Gol.')
        print('Escolha a versão do Gol:')
        print('1 - Gol 1.0')
        print('2 - Gol 1.6')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Gol 1.0.')
        elif versao == '2':
            print('Você escolheu a versão Gol 1.6.')
        else:
            print('Opção inválida para a versão do Gol.')
    elif modelo == '2':
        print('Você escolheu o modelo Polo.')
        print('Escolha a versão do Polo:')
        print('1 - Polo msi')
        print('2 - Polo tsi')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Polo msi.')
        elif versao == '2':
            print('Você escolheu a versão Polo tsi.')
        else:
            print('Opção inválida para a versão do Polo.')
    elif modelo == '3':
        print('Você escolheu o modelo Fusca.')
        print('Escolha a versão do Fusca:')
        print('1 - Fusca 1300')
        print('2 - Fusca 1600')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Fusca 1300.')
        elif versao == '2':
            print('Você escolheu a versão Fusca 1600.')
        else:
            print('Opção inválida para a versão do Fusca.')
    else:
        print('Opção inválida para o modelo de Volkswagen.')
elif marca == '2':
    print('Você escolheu Ford.')
    print('Escolha um modelo de Ford:')
    print('1 - Fiesta')
    print('2 - Focus')
    print('3 - EcoSport')
    modelo = input('Digite o número correspondente ao modelo desejado de 1 a 3: ')
    if modelo == '1':
        print('Você escolheu o modelo Fiesta.')
        print('Escolha a versão do Fiesta:')
        print('1 - Fiesta 1.0')
        print('2 - Fiesta 1.6')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Fiesta 1.0.')
        elif versao == '2':
            print('Você escolheu a versão Fiesta 1.6.')
        else:
            print('Opção inválida para a versão do Fiesta.')
    elif modelo == '2':
        print('Você escolheu o modelo Focus.')
        print('Escolha a versão do Focus:')
        print('1 - Focus SE')
        print('2 - Focus Titanium')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Focus SE.')
        elif versao == '2':
            print('Você escolheu a versão Focus Titanium.')
        else:
            print('Opção inválida para a versão do Focus.')
    elif modelo == '3':
        print('Você escolheu o modelo EcoSport.')
        print('Escolha a versão do EcoSport:')
        print('1 - EcoSport SE')
        print('2 - EcoSport Titanium')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão EcoSport SE.')
        elif versao == '2':
            print('Você escolheu a versão EcoSport Titanium.')
        else:
            print('Opção inválida para a versão do EcoSport.')
    else:
        print('Opção inválida para o modelo de Ford.')
elif marca == '3': 
    print('Você escolheu Chevrolet.')
    print('Escolha um modelo de Chevrolet:')
    print('1 - Onix')
    print('2 - Cruze')
    print('3 - S10')
    modelo = input('Digite o número correspondente ao modelo desejado de 1 a 3: ')
    if modelo == '1':
        print('Você escolheu o modelo Onix.')
        print('Escolha a versão do Onix:')
        print('1 - Onix Joy')
        print('2 - Onix LT')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Onix Joy.')
        elif versao == '2':
            print('Você escolheu a versão Onix LT.')
        else:
            print('Opção inválida para a versão do Onix.')
    elif modelo == '2':
        print('Você escolheu o modelo Cruze.')
        print('Escolha a versão do Cruze:')
        print('1 - Cruze LT')
        print('2 - Cruze Premier')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Cruze LT.')
        elif versao == '2':
            print('Você escolheu a versão Cruze Premier.')
        else:
            print('Opção inválida para a versão do Cruze.')
    elif modelo == '3':
        print('Você escolheu o modelo S10.')
        print('Escolha a versão da S10:')
        print('1 - S10 LS')
        print('2 - S10 LTZ')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão S10 LS.')
        elif versao == '2':
            print('Você escolheu a versão S10 LTZ.')
        else:
            print('Opção inválida para a versão da S10.')
    else:
        print('Opção inválida para o modelo de Chevrolet.')
elif marca == '4': 
    print('Você escolheu Fiat.')
    print('Escolha um modelo de Fiat:')
    print('1 - Uno')
    print('2 - Argo')
    print('3 - Toro')
    modelo = input('Digite o número correspondente ao modelo desejado de 1 a 3: ')
    if modelo == '1':
        print('Você escolheu o modelo Uno.')
        print('Escolha a versão do Uno:')
        print('1 - Uno Attractive')
        print('2 - Uno Way')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Uno Attractive.')
        elif versao == '2':
            print('Você escolheu a versão Uno Way.')
        else:
            print('Opção inválida para a versão do Uno.')
    elif modelo == '2':
        print('Você escolheu o modelo Argo.')
        print('Escolha a versão do Argo:')
        print('1 - Argo Drive')
        print('2 - Argo Trekking')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Argo Drive.')
        elif versao == '2':
            print('Você escolheu a versão Argo Trekking.')
        else:
            print('Opção inválida para a versão do Argo.')
    elif modelo == '3':
        print('Você escolheu o modelo Toro.')
        print('Escolha a versão da Toro:')
        print('1 - Toro Freedom')
        print('2 - Toro Volcano')
        versao = input('Digite o número correspondente à versão desejada de 1 a 2: ')
        if versao == '1':
            print('Você escolheu a versão Toro Freedom.')
        elif versao == '2':
            print('Você escolheu a versão Toro Volcano.')
        else:
            print('Opção inválida para a versão da Toro.')
    else:
        print('Opção inválida para o modelo de Fiat.')
else:
    print('Opção inválida para a marca de veículo.')

print('Obrigado por utilizar nosso sistema de escolha de veículos!')
