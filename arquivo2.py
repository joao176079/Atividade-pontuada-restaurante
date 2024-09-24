import os
os.system("cls || clear")

lista_preco_acumulado = []
lista_dos_pratos = []

def calcular_desconto(a):
    subtotal = sum(a)
    desconto = subtotal * 0.1
    valor_com_desconto = subtotal - desconto
    return desconto, valor_com_desconto

def calcular_acrescimo(a):
    subtotal = sum(a)
    acrescimo = subtotal * 0.1
    valor_com_acrescimo = subtotal + acrescimo
    return acrescimo, valor_com_acrescimo

print ("""
====== Cardápio ======   
1 - Pão com ovo = R$4.00
2 - Strogonoff (Acompanha arroz e batata palha) = R$28.00
3 - Feijoada (Acompanha-se arroz e salada) = R$24.00
4 - Bife à milanesa (Acompanha arroz e salada) = R$28.00
5 - Hamburguer Artesanal (Acompanha fritas) = R$30.00
6 - Filé com fritas (Acompanha arroz) = R$26.00
7 - Salmão grelhado (Acompanha-se arroz e salada) = R$32.00
    
    """)

    
while True:
    opcao = int(input("Insira o número do prato desejado: "))

    match(opcao):
        case 1:
            print("Pão com ovo selecionado.")
            valor = 4
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("1 - Pão com ovo")
        case 2:
            print("Strogonoff selecionado.")
            valor = 28
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("2 - Strogonoff")
        case 3:
            print("Feijoada selecionada.")
            valor = 24
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("3 - Feijoada")
        case 4:
            print("Bife à milanesa selecionado.")
            valor = 28
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("4 - Bife à milanesa")
        case 5:
            print("Hamburguer artesanal selecionado.")
            valor = 30
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("5 - Hamburguer artesanal")
        case 6:
            print("Filé com fritas selecionado.")
            valor = 26
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("6 - Filé com fritas")
        case 7:
            print("Salmão grelhado selecionado.")
            valor = 32
            lista_preco_acumulado.append(valor)
            lista_dos_pratos.append("7 - Salmão grelhado")
        case _:
            print("Opção inválida. Por favor, digite novamente.")

    outro_prato = int(input("\nVocê deseja selecionar outro prato? Digite 1 se sim ou digite 0 caso queira ver a conta: "))
    match(outro_prato):
        case 1:
            print("\nEscolha outro prato.")
        case 0:
            break
        case _:
            outro_prato
            print("Opção inexistente. Tente novamente.")


subtotal = sum(lista_preco_acumulado)
desconto, valor_com_desconto = calcular_desconto(lista_preco_acumulado)
acrescimo, valor_com_acrescimo = calcular_acrescimo(lista_preco_acumulado)

print(f"\nCódigos inseridos e pratos selecionados: {lista_dos_pratos}")
print(f"Subtotal: R${subtotal:.2f}")

print("""
    \nFormas de pagamento disponíveis:
    1 - À vista (Desconto de 10%)
    2 - Cartão de crédito (Acréscimo de 10%)
    """)

forma_de_pagamento = int(input("Insira a forma de pagamento desejada: "))
match(forma_de_pagamento):
    case 1:
        print("\nPagamento à vista selecionado.")
        print(f"Desconto aplicado: R${desconto:.2f}")
        print(f"Total: R${valor_com_desconto:.2f}")
    case 2:
        print("\nPagamento via cartão de crédito selecionado.")
        print(f"Acréscimo aplicado: R${acrescimo:.2f}")
        print(f"Total: R${valor_com_acrescimo:.2f}")
    case _:
        print("Opção indisponível. Por favor, tente novamente.")