# Fazer a lógica utilizando array

import random

print("\nBem-vindo ao Rock, Paper, Scissors, Lizard, Spock!")

conversao_numero_para_texto = {
    0: "Rock",
    1: "Spock",
    2: "Paper",
    3: "Lizard",
    4: "Scissors"
}

lista_com_escolhas_do_jogador = []        
lista_com_escolhas_aleatoria_da_maquina = []
lista_com_resultados = []

def mensagem_final():
    print(f"\nPlayer chooses {conversao_numero_para_texto[lista_com_escolhas_do_jogador[i]]}")
    print(f"Computer chooses {conversao_numero_para_texto[lista_com_escolhas_aleatoria_da_maquina[i]]}")

try:
    numero_rodadas = int(input("\nDigite o número de vezes que deseja jogar: "))

    if(numero_rodadas < 0):
        print("\nEntrada Inválida. Por favor, digite um número inteiro e positivo.")
    else:
        print("\nEscolha um dos números abaixo para fazer sua jogada:")
        print("0 - Rock (Pedra)")
        print("1 - Spock (Spock)")
        print("2 - Paper (Papel)")
        print("3 - Lizard (Lagarto)")
        print("4 - Scissors (Tesoura)\n")


        for i in range(1, numero_rodadas + 1):
            escolha_do_jogador = int(input(f"Rodada {i} de {numero_rodadas}. Faça sua jogada: "))
            escolha_aleatoria_da_maquina = random.randint(0,4)

            while escolha_do_jogador < 0 or escolha_do_jogador > 4:
                escolha_do_jogador = int(input(f"Número inválido. Rodada {i} de {numero_rodadas}. Faça sua jogada novamente: "))

            resultado_rodada = (escolha_do_jogador - escolha_aleatoria_da_maquina) % 5

            lista_com_escolhas_do_jogador.append(escolha_do_jogador)
            lista_com_escolhas_aleatoria_da_maquina.append(escolha_aleatoria_da_maquina)
            lista_com_resultados.append(resultado_rodada)


        for i in range(0, numero_rodadas):
            if lista_com_escolhas_do_jogador[i] == lista_com_escolhas_aleatoria_da_maquina[i]:
                mensagem_final()
                print("Player and computer tie!")
            elif lista_com_resultados[i] == 2 or lista_com_resultados[i] == 1:
                mensagem_final()
                print("Player wins!")
            else:
                mensagem_final()
                print("Computer wins!")
except ValueError:
    print("\nEntrada inválida. Por favor, digite um número inteiro e positivo.")