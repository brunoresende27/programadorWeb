# numero = [10,5,7,2,1]
# numero[0] = 111
# print(numero)
# print(len(numero))
# del numero[1]
# print(numero)
# print(numero[-2])
# numero.append(55)
# print(numero)
# numero.insert(2, 99)
# print(numero)

# cont = 0
# lista = ["Gustavo","Andrey","Leonardo","Vinicius","Rosane"]
# #print(lista[1])
# for i in lista:
#     cont = cont + 1
#     if cont == len(lista):
#         print(i)
#     else:
#         print(i,end="-")

lista_compras = []
carrinho = []
continuar = "S"

while continuar == "S":
    item = input("Digite o item que deseja adicionar à lista de compras: ")
    lista_compras.append(item)
    continuar = input("Deseja adicionar outro item? (S/N): ").upper().strip()


while len(lista_compras) > 0:
    print("Lista de Compras")
    for i in range(len(lista_compras)):
        print(f"{i} - {lista_compras[i]}")
 
    print(f"No carrinho: {carrinho}")
    
    posicao = int(input("Digite o número do item que colocou no carrinho: "))

    item_comprado = lista_compras[posicao]
    del lista_compras[posicao]
    #item_comprado = lista_compras.pop(posicao)
    carrinho.append(item_comprado)

print("Lista de compras finalizada.")
for i, item in enumerate(carrinho):
    print(f"{i+1} - {item}")
