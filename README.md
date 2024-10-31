# README - Cálculo de Quadrados e Cubos

## Descrição
Este programa lê um valor inteiro \( N \) (onde \( 1 < N < 1000 \)) e gera \( N \) linhas de saída. Cada linha contém três números:
1. O número da linha (de 1 a \( N \)).
2. O quadrado desse número.
3. O cubo desse número.

## Entrada
A entrada consiste em um único número inteiro \( N \) que representa a quantidade de linhas que serão impressas.

- **Formato:** Um único inteiro.
- **Restrições:** \( 1 < N < 1000 \)

## Saída
A saída consiste em \( N \) linhas, onde cada linha contém três valores:
- O número da linha.
- O quadrado do número da linha.
- O cubo do número da linha.

**Formato da Saída:**
```
1 1 1
2 4 8
3 9 27
...
N N^2 N^3
```

## Exemplo

### Exemplo de Entrada
```
5
```

### Exemplo de Saída
```
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
```

## Como Executar
1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Salve o código em um arquivo com a extensão `.py`, por exemplo, `quadrados_cubos.py`.
3. Abra o terminal (ou prompt de comando).
4. Navegue até o diretório onde o arquivo foi salvo.
5. Execute o programa usando o comando:
   ```
   python quadrados_cubos.py
   ```
6. Insira um número inteiro entre 2 e 999 e pressione Enter.

## Considerações Finais
Este programa é uma boa prática para entender laços de repetição e operações matemáticas básicas em Python. Agradecemos a Cássio F. pela inspiração no problema.
