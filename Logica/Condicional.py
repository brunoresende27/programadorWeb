# nota1 = 8
# nota2 = 6
# media = (nota1 + nota2) / 2
# if media >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
media = (n1 + n2 + n3 + n4) / 4
print("A média do aluno é:", media)
# >= Maior ou igual. <= Menor ou igual. > Maior. < Menor. == Igual. != Diferente.
if media >= 7: 
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim do programa")