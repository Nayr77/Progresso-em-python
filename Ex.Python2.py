# Programa de votação para escolha do melhor dia da semana para lives

# Lista de dias válidos
dias_validos = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

# Dicionário para contar os votos
votos = {dia: 0 for dia in dias_validos}

# Pergunta quantos colaboradores vão votar
num_colaboradores = int(input("informe o número de colaboradores que irão votar: "))

# Coleta os votos
for i in range(num_colaboradores):
    voto = input(f"{i+1}. Informe o dia da semana de sua preferência: ").strip().lower()
    if voto in votos:
        votos[voto] += 1
    else:
        print("Dia inválido. Tente novamente.")
        i -= 1  # repete a votação para esse colaborador

# Verifica o(s) dia(s) mais votado(s)
max_votos = max(votos.values())
dias_mais_votados = [dia for dia, qtd in votos.items() if qtd == max_votos]

# Exibe o resultado final
print("\nO dia escolhido pelos colaboradores é:", end=" ")
if len(dias_mais_votados) == 1:
    print(dias_mais_votados[0])
else:
    print("empate entre os dias:")
    for dia in dias_mais_votados:
        print("-", dia)