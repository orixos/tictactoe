def find_valid_pos(board):
    return [i for i in range(9) if board[i] == 0]

def check_winner(board):
    win_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for pos in win_pos:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != 0:
            return board[pos[0]]
    if not find_valid_pos(board):
        return 0 # 平局
    return -1 # 未结束

def board_to_string(board):
    board_str = ''
    for i in board:
        board_str += str(i)
    return board_str

def calc_score(board, side):
    board_str = board_to_string(board)
    if dic.get(board_str) is None:
        winner = check_winner(board)
        score_dic = {1: 6, 2: -2, 0: 4} # 5, -2, 4
        if winner != -1:
            score = score_dic[winner]
        else:
            valid_pos = find_valid_pos(board)
            scores = []
            for pos in valid_pos:
                new_board = board[:]
                new_board[pos] = side
                new_side = 3 - side
                scores.append(calc_score(new_board, new_side))
            if side == 1 and score_dic[1] in scores:
                score = score_dic[1]
            elif side == 1 and score_dic[2] in scores:
                scores = [x for x in scores if x != score_dic[2]] # 删去-2再计算
                if len(scores) == 0:
                    score = score_dic[2]
                else:
                    score = sum(scores) / len(scores)
            else:
                score = sum(scores) / len(scores)
        dic[board_str] = round(score, 4)
    return dic.get(board_str)

def save_dict(filename):
    with open(filename, 'w'):
        pass
    with open(filename, 'a') as f:
        for key in dic.keys():
            content = str(key) + ',' + str(dic[key]) + '\n'
            f.write(content)

if __name__ == '__main__':
    init_board = [0] * 9

    dic = {}
    init_side = 1
    calc_score(init_board, init_side)
    save_dict('data_compfirst.csv')

    dic = {}
    init_side = 2
    calc_score(init_board, init_side)
    save_dict('data_userfirst.csv')
