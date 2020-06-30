import pickle
lista = []
while True:
    dados = (input("Digite um nome:"))
    lista.append(dados)
    if dados == "sair":
        break
    elif dados == "SAIR":
        break
    else:
        lista.sort()
    print("para sair digite sair ou SAIR")
    print("clientes:",lista)

    for x in enumerate(lista):
        print(x)

        #clientes = open('clientes.txt', 'w')
        #clientes.write((str(lista)))
        #clientes.close()
        n = open("nomes.pck","wb")
        pickle.dump(lista,n)
        n.close()
        nomes = open("nomes.pck", "rb")
        x = pickle.load(nomes)
        print(x)
        n.close()