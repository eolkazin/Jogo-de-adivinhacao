# Jogo de Adivinhação Interativo (Versão Profissional)

Este projeto implementa um jogo de adivinhação interativo onde o jogador tenta descobrir um número inteiro secreto, gerado aleatoriamente dentro de um intervalo predefinido (atualmente de 1 a 10). O sistema fornece feedback imediato após cada tentativa, indicando se o número alvo é maior ou menor que o palpite do jogador. O jogo rastreia o número de tentativas incorretas e as exibe ao final da partida.

## Funcionalidades

* **Geração Aleatória:** O número secreto é gerado de forma pseudoaleatória dentro do intervalo especificado.
* **Feedback Interativo:** O jogador recebe dicas claras ("O número é maior" ou "O número é menor") após cada tentativa.
* **Interface de Terminal Limpa:** A tela do terminal é limpa a cada nova tentativa (em sistemas compatíveis), proporcionando uma experiência de jogo mais focada.
* **Contagem de Erros:** O sistema contabiliza o número de tentativas incorretas, fornecendo uma métrica de desempenho ao jogador.
* **Mensagem de Vitória:** Uma mensagem de sucesso clara é exibida quando o jogador adivinha o número correto.

## Arquivos do Projeto

* `adivinhacao.py`: Contém o código fonte principal do jogo.
* `README.md`: Este arquivo, fornecendo informações sobre o projeto.

## Pré-requisitos

* **Python 3.x:** Certifique-se de que o Python 3 esteja instalado em seu sistema. Você pode verificar a instalação abrindo um terminal ou prompt de comando e executando `python --version` ou `python3 --version`.

## Como Executar o Jogo

1.  **Navegue até o Diretório do Projeto:** Abra um terminal ou prompt de comando e utilize o comando `cd` para acessar o diretório onde o arquivo `adivinhacao.py` está localizado.
2.  **Execute o Script:** Execute o jogo utilizando o seguinte comando:

    ```bash
    python adivinhacao.py
    ```

3.  **Siga as Instruções:** O jogo solicitará que você insira um número. Digite seu palpite e pressione Enter. Siga as dicas fornecidas até acertar o número secreto.

## Estrutura do Código

```python
import random
import os

# Inicialização das variáveis
tentativas_incorretas = 0
numero_secreto = random.randrange(1, 10)

# Solicita a primeira tentativa do jogador
palpite_jogador = int(input("Digite seu palpite (entre 1 e 9): "))

# Loop principal do jogo
while palpite_jogador != numero_secreto:
    # Fornece feedback ao jogador
    if numero_secreto > palpite_jogador:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

    # Incrementa o contador de tentativas incorretas
    tentativas_incorretas += 1

    # Solicita uma nova tentativa do jogador
    palpite_jogador = int(input("Digite outro palpite: "))

# Mensagem de vitória
print("Parabéns! Você acertou o número secreto:", numero_secreto)
print("Você precisou de", tentativas_incorretas + 1, "tentativas.")
if tentativas_incorretas > 0:
    print("Você cometeu", tentativas_incorretas, "erros.")
else:
    print("Você acertou de primeira!")