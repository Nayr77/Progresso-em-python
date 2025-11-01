# Exercício 2 – Tabela de parcelamento do carro

valor = float(input("Digite o preço do carro: "))

# cálculo do valor à vista com 20% de desconto
avista = valor * 0.80
print(f"\nO preço final à vista com desconto 20% é: R$ {round(avista, 2)}")

# tabela de parcelamento / tomei atitude de alternar o cabeçalho para melhor facilitação na leitura da tabela
print("\nTabela de Parcelamento:")
parcelas = 6
incremento = 600  # acréscimo fixo a cada 6 parcelas
preco_final = valor + incremento

while parcelas <= 60:
    valor_parcela = preco_final / parcelas
    print(f"O preço final parcelado em {parcelas} X é de R$ {round(preco_final, 2)} com parcelas de R$ {round(valor_parcela, 2)}")
    parcelas += 6
    preco_final += incremento