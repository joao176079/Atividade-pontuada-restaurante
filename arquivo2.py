lista_preco_acumulado = []


while True:
    opcao = int(input("Insira o número do prato desejado: "))
    match(opcao):
        case 1:
            valor = 4
            lista_preco_acumulado.append(valor)