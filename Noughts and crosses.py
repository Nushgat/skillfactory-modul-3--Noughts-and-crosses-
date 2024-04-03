print('-------------------------------------------------')
print('*** Добро пожаловать в игру "Крестики-нолики" ***')
print('-------------------------------------------------')
print('Формат ввода: номер строки и номер столбца')


board = [[' ' for _ in range(3)] for _ in range(3)]

# Функция для отображения игрового поля
def display_board(board):
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(board[i])
        print(f"{i} {row_info}")

# Функция для проверки, есть ли победитель
def check_winner(board):
    # Проверка по горизонтали
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    # Проверка по вертикали
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    # Проверка по диагонали
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False
# Функция для хода игрока
def make_move(board, row, col, current_player):
    if 0 <= row <= 2 and 0 <= col <= 2:
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print('Клетка занята')
    else:
        print("Строка и столбец должны находиться в диапазоне от 0 до 2")

 # Функция для проверки ничьей
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True
# Основной цикл игры
def play_game():
    current_player = "X"
    while True:
        current_player = "O" if current_player == "X" else "X"
        display_board(board)
        row = int(input(f"Игрок {current_player}, введите номер строки (0-2): "))
        col = int(input("Введите номер столбца (0-2): "))
        make_move(board, row, col, current_player)
        if check_winner(board):
            display_board(board)
            print(f"{current_player} победил!")
            break
        if check_tie(board):
            display_board(board)
            print("Ничья!")
            break

play_game()






