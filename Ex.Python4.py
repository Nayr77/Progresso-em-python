# Programa para calcular parcelas de uma dívida com diferentes taxas de juros

# Tabela de parcelas e suas respectivas taxas de juros
tabela_juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

# Entrada do valor da dívida
valor_divida = float(input("Digite o valor da dívida: "))

# Exibição da tabela de resultados
for parcelas, taxa in tabela_juros.items():
    valor_juros = valor_divida * (taxa / 100)
    total = valor_divida + valor_juros
    valor_parcela = total / parcelas
    print(f"Total:R$ {total:.2f} Juros:R$ {valor_juros:.2f} Número de parcelas:{parcelas} Valor da Parcela:R$ {valor_parcela:.2f}")