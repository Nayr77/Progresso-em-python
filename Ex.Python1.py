# Simulador de imposto de renda sobre investimentos

# Exibe opções de investimento
print("Escolha o tipo de investimento:")
print("1. CDB")
print("2. LCI")
print("3. LCA")

# Entrada do tipo de investimento
tipo = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

# Entrada do valor e tempo de investimento
valor_investido = float(input("Digite o valor a ser resgatado: "))
dias = int(input("Digite o número de dias que o investimento permanecerá investido: "))

# Define a taxa de imposto de renda conforme o tempo
if dias <= 180:
    taxa_ir = 22.5
elif dias <= 360:
    taxa_ir = 20.0
elif dias <= 720:
    taxa_ir = 17.5
else:
    taxa_ir = 15.0

# Calcula o imposto de renda apenas para CDB
if tipo == 1:
    valor_ir = valor_investido * (taxa_ir / 100)
    print(f"\nO valor do imposto de renda será de R$ {valor_ir:.2f}.")
elif tipo == 2 or tipo == 3:
    print("\nEsse tipo de investimento é isento de imposto de renda.")
else:
    print("\nTipo de investimento inválido.")