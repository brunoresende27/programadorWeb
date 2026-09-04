# Ingredientes
farinha = 200  # gramas
açúcar = 150  # gramas
achocolatado = 50  # gramas   
fermento = 10  # gramas
ovos = 3  # unidades    
leite = 200  # ml
manteiga = 100  # gramas

forno = False  # forno desligado
tigela = []  # lista para misturar os ingredientes
# Modo de Preparo
# 1. Pré-aqueça o forno a 180°C.
ligar_forno = input("Deseja ligar o forno? (s/n): ").lower().strip()
if ligar_forno == 's':
    forno = True   
    print("Pré-aquecendo o forno a 180°C...")

# 2. Misture os ingredientes secos (farinha, açúcar, achocolatado e fermento) em uma tigela.
if forno == True:
    tigela.append(farinha)
    tigela.append(açúcar)
    tigela.append(achocolatado)
    tigela.append(fermento)
    print("Misturando os ingredientes secos na tigela...")
    # 3. Adicione os ovos, o leite e a manteiga derretida à tigela e misture bem até obter uma massa homogênea.
    tigela.append(ovos)
    tigela.append(leite)
    tigela.append(manteiga)
    print("Adicionando os ingredientes líquidos à tigela...")
    print("Misturando bem até obter uma massa homogênea...")
    # 4. Despeje a massa em uma forma untada e leve ao forno por aproximadamente 30 minutos ou até que um palito saia limpo ao ser inserido no centro do bolo.
    print("Despejando a massa em uma forma untada...")
    print("Levando ao forno por aproximadamente 30 minutos...")
    for i in range(30):
        if i+1 == 15:
            print("Passaram-se 15 minutos...")

        if i+1 == 30:
            print("O bolo está pronto! Retire do forno e deixe esfriar antes de servir.")
else:
    print("O forno não foi ligado. Não é possível prosseguir com o preparo do bolo.")
        

