import csv
import random

data_dic = {}
board = [0] * 9
side = 1

def read_data(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            key = row[0]
            value = row[1]
            data_dic[key] = value

def show_board():
    side_dic = {1: 'O', 2: 'X', 0: '.'}
    for i in range(3):
        for j in range(3):
            print(side_dic[board[i * 3 + j]], '', end='')
        print()

def find_valid_pos():
    return [i for i in range(9) if board[i] == 0]

def down(pos):
    global side
    board[pos] = side
    show_board()

def check_winner():
    global end_flag
    win_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for pos in win_pos:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != 0:
            if board[pos[0]] == 1:
                print('You lose.')
                return 1
            else:
                print('You win.')
                return 1
    if not find_valid_pos():
        print('Draw.')
        return 1
    return 0

def board_to_string(board_in):
    board_str = ''
    for i in board_in:
        board_str += str(i)
    return board_str

def computer_down():
    global side
    valid_pos = find_valid_pos()

    # 收集所有有效位置的分数
    scores = []
    for pos in valid_pos:
        new_board = board[:]
        new_board[pos] = side
        score = data_dic.get(board_to_string(new_board))
        if score is not None:
            scores.append(score)
        else:
            print(f'Error: Board {board_to_string(board)} does not exist.')
            return

    # 如果没有有效位置
    if not scores:
        print('Error: No valid position found.')
        return

    # 获取最大分数的所有索引
    max_score = max(scores)
    max_indices = [i for i, score in enumerate(scores) if score == max_score]

    # 随机选择一个最佳位置
    move = valid_pos[random.choice(max_indices)]
    print(f'Computer: {move}')
    down(move)

def user_down():
    while True:
        try:
            pos = int(input('User: '))
            if 8 >= pos >= 0 == board[pos]:
                down(pos)
                break
            else:
                print('Error: Invalid position, please enter again.')
        except:
            print('Error: Chess down error.')

def play(mode):
    global side
    if mode == '1':
        read_data('data_compfirst.csv')
        side = 1
    elif mode == '2':
        read_data('data_userfirst.csv')
        side = 2
    else:
        print('Error: Invalid mode.')
        return

    show_board()
    while True:
        if side == 1:
            computer_down()
        elif side == 2:
            user_down()
        if check_winner():
            break
        side = 3 - side

if __name__ == '__main__':
    count = 1
    while True:
        print(f'Round %d:' % count)
        print('Welcome to TicTacToe!')
        print('Input the side that begins first. 1 for computer first, 2 for user first.')
        print('Please remember, your chess is \'X\', no matter which side begins first.')
        print('Input 0 - 8 to place a chess.')
        play(input('> '))
        print()
        count += 1
