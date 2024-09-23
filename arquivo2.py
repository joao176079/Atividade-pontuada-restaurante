lista_preco_acumulado = []
lista_dos_pratos = []

print ("""
    Cardápio :
    
1 - Pão com ovo = 4.00 R$
2 - Strogonoff " Acompanha-se arroz e batata palha " = 28.00
3 - Feijoada " Acompanha-se arroz e salada " = 24.00
4 - Bife à milanesa " Acompanha-se arroz e salada " = 28.00
5 - Hamburguer Artesanal " Acompanha fritas " = 30.00
6 - Filé com fritas " Acompanha-se arroz " = 26.00
7 - Salmão grelhado " Acompanha-se arroz e salada " = 32.00
    

    """)

    
while True:
    opcao = int(input("Insira o número do prato desejado: "))

    match(opcao):
        case 1:
            valor = 4
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("Pão com ovo")
        case 2:
            valor = 28
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("Strogonoff")
        case 3:
            valor = 24
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("Feijoada")
        case 4:
            valor = 28
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("Bife à milanesa")
        case 5: 
            valor = 30
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("Hamburguer artesanal")
        case 6:
            valor = 26
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("Filé com fritas")
        case 7:
            valor = 32
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("Salmão grelhado")
        case _:
            print("Opção inválida. Por favor, digite novamente.")

    outro_prato = input("Você deseja escolher outro prato? ").lower()
    if outro_prato == "não":
        break