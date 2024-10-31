# Passo 1: Leitura do valor de N
N = int(input())  # O usuário deve inserir apenas o número diretamente.

# Passo 2: Estrutura de repetição para gerar as linhas
for i in range(1, N + 1):
    # Passo 3: Cálculo dos valores
    quadrado = i ** 2  # i elevado ao quadrado
    cubo = i ** 3      # i elevado ao cubo
    
    # Passo 4: Impressão dos resultados
    print(i, quadrado, cubo)
