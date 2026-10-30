# Iniciando o PDV

print("\n""=== SISTEMA PDV INICIADO (Digite 0 no valor para encerrar) ===")

#Variaveis do PDV
vendas = []
qnt_compras = 0
total_bruto = 0.0
total_descontoIdade = 0.0
total_descontoExtra = 0.0
total_desconto = 0.0
total_final = 0.0

# Inicio do While
while True:
    # Inicio do APP
    valorCompra = float(input("\nDigite o valor numerico da sua Compra (R$): "))

    #Loop para verificar valores negativos
    while (valorCompra < 0):
        print("Valor inválido, insira um valor válido!!")
        valorCompra = float(input("\nDigite o valor numerico da sua Compra (R$): "))
    
    # Condição de parada: se digitar 0, o loop é encerrado imediatamente
    if valorCompra == 0:
        print("Saindo.....\n")
        break

    idade = int(float(input("Digite sua Idade: ")))

    #Loop para verificar idade negativa
    while (idade < 0):
        print("Idade inválida, insira uma idade válida!!")
        idade = int(float(input("\nDigite sua Idade: ")))

    valorFinal = valorCompra
    descontoCompra_Atual = 0.0
    valorDesconto_Idade = 0.0
    valorDesconto_Extra = 0.0

    #Verificação de Idade Para Descontos
    #O enunciado ficou meio ambíguo. Dessa forma, a regra de 10% de desconto sobre o valor é utilizada apenas se a regra de idade (>= 65 anos) for aplicada.
    if (idade >= 65):
        valorDesconto_Idade = valorCompra * (20/100)
        valorFinal = valorFinal - valorDesconto_Idade
        descontoCompra_Atual += valorDesconto_Idade
        
        #Verificação de Valor Para Descontos Extras
        if (valorFinal > 100):
            valorDesconto_Extra = valorFinal * (10/100)
            valorFinal = valorFinal - valorDesconto_Extra
            descontoCompra_Atual += valorDesconto_Extra
            
    print("==============================================")
    print("O valor final da sua compra é: R$ ", valorFinal)
    print("==============================================")

    #Salvando as Compras
    dadosCompras = {
        "Valor original": valorCompra,
        "Idade": idade,
        "Desconto Idade": valorDesconto_Idade,
        "Desconto Extra": valorDesconto_Extra,
        "Total Desconto": descontoCompra_Atual,
        "Valor Final": valorFinal
    }
    vendas.append(dadosCompras)

    #Atualizando os Dados do Dia
    qnt_compras += 1
    total_bruto += valorCompra
    total_descontoIdade += valorDesconto_Idade
    total_descontoExtra += valorDesconto_Extra
    total_desconto += descontoCompra_Atual
    total_final += valorFinal

#Fim do While

# Resumo final
print("\n" + "="*40)
print("           RELATÓRIO DO DIA          ")
print("="*40)
print(f"Quantidade de compras do dia: {qnt_compras}")
print(f"Valor total bruto do dia:         R$ {total_bruto:.2f}")
print(f"Valor total de descontos por Idade do dia:  R$ {total_descontoIdade:.2f}")
print(f"Valor total de descontos Extra do dia:  R$ {total_descontoExtra:.2f}")
print(f"Valor total de descontos do dia:  R$ {total_desconto:.2f}")
print(f"Valor total final do dia:         R$ {total_final:.2f}")
print("="*40)
