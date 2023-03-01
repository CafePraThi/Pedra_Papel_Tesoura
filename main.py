import random

numWins = 0
numWinsComputer = 0

options = ["pedra", "papel", "tesoura"]

print('============= PEDRA -- PAPEL -- TESOURA =============')

while True:
    choice = input("Escolha: Pedra, Papel, Tesoura! Ou aperte s para Sair: ")
    choice = choice.lower()
    if choice == "s":
        break

    if choice not in options:
        print('Por favor, digite uma opção valida!')
        continue

    rand = random.randint(0, 2)
    computerChoice = options[rand]
    print("O Computador escolheu: {}".format(computerChoice))

    if choice == computerChoice:
        print("É um empate!")
    elif choice == 'pedra' and computerChoice == 'tesoura':
        print('Voce Ganhou! Pedra ganha da Tesoura.')
        numWins += 1
    elif choice == 'papel' and computerChoice == 'pedra':
        print('Voce Ganhou! Papel ganha da Pedra.')
        numWins += 1
    elif choice == 'tesoura' and computerChoice == 'papel':
        print('Voce Ganhou! Tesoura Ganha do Papel. ')
        numWins += 1
    else:
        print('Voce Perdeu! {} ganha de {}'.format(computerChoice, choice))
        numWinsComputer += 1

print('Suas vitorias: {}'.format(numWins))
print('Vitorias do Computador: {}'.format(numWinsComputer))
