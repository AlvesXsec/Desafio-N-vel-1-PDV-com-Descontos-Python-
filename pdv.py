# DESAFIO NÍVEL 1 - PVD COM DESCONTOS (PYTHON)

lista = []

while True:   
    valor_da_compra = float(input("Digite o valor da compra (0 para encerrar): R$ "))
    if valor_da_compra == 0:
        break
    if valor_da_compra < 0:
        print("Pedir novamente!")
        continue

    idade_do_cliente = int(input("Digite sua idade: "))
    if idade_do_cliente < 0:
        print(f"Pedir novamente!")
        continue

    valor_final = valor_da_compra
    if idade_do_cliente >= 65:
        valor_final = valor_da_compra * 0.80

    if valor_final > 100:
        valor_final = valor_final * 0.90

    desconto = valor_da_compra - valor_final

    print(f"Valor inicial: R$ {valor_da_compra:.2f}")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")

    compra = {
        "inicial": valor_da_compra ,
        "desconto": desconto ,
        "final": valor_final
    }

    lista.append(compra)

quantidade = len(lista)

total_bruto = sum(compra["inicial"] for compra in lista)
total_de_descontos_concedidos = sum(compra["desconto"] for compra in lista)
total_final = sum(compra["final"] for compra in lista)

print("\n -----RESUMO DO DIA-----")
print(f"Quantidade de compras: {quantidade}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_de_descontos_concedidos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
