from velha import criarBoard, fazMovimento, getInputValido, \
    printBoard, verificaGanhador, verificaMovimento

jogador = 0  # jogador 1
board = criarBoard()
ganhador = verificaGanhador(board)
while (not ganhador):
    printBoard(board)
    print("===================")
    i = getInputValido("Digite a linha: ")
    j = getInputValido("Digite a coluna: ")

    if (verificaMovimento(board, i, j)):
        fazMovimento(board, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("A posicao informado ja esta ocupada")

    ganhador = verificaGanhador(board)

print("===================")
printBoard(board)
print("Ganhador = ", ganhador)
print("===================")
