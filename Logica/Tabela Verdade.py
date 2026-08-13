usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

usuario_correto = False
senha_correta = False

# Exemplo Operador se somente se
if usuario == "admin":
    usuario_correto = True

if senha == "1234":
    senha_correta = True

# Exemplo Operador E
# Para entrar, ambos PRECISAM ser True
if usuario_correto and senha_correta:
    print("Acesso permitido. Bem-vindo!")
else:
    print("Usuário ou senha incorretos.")
    
valor_compra_alto = False  
tem_cupom_frete = True     

# Se qualquer uma das duas condições for real, ele ganha o benefício
if valor_compra_alto or tem_cupom_frete:
    print("Parabéns! Você ganhou frete grátis.")
else:
    print("O frete para a sua região custa R$ 15,00.")

# Faça um programa que receba duas notas e calcule a média. 
# Se a média for maior ou igual a 7, exiba "Aprovado". Caso contrário, exiba "Reprovado".