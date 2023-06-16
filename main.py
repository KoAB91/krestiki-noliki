win_combinations = [[[0, 0], [0, 1], [0, 2]],
                        [[1, 0], [1, 1], [1, 2]],
                        [[2, 0], [2, 1], [2, 2]],
                        [[0, 0], [1, 0], [2, 0]],
                        [[0, 1], [1, 1], [2, 1]],
                        [[0, 2], [1, 2], [2, 2]],
                        [[0, 0], [1, 1], [2, 2]],
                        [[0, 2], [1, 1], [2, 0]]]
game_field = None
players_turns = {'x': [], 'o': []}
has_winner = False
score = [0, 0]
counter = 0


def start_new_game():
    global game_field, players_turns, has_winner, counter
    game_field = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    players_turns = {'x': [], 'o': []}
    has_winner = False
    counter = 0
    draw_field()


def draw_field():
    print('', 0, 1, 2, sep='\t')
    print(0, *game_field[0], sep='\t')
    print(1, *game_field[1], sep='\t')
    print(2, *game_field[2], sep='\t')


def make_a_move(player, turns: list):
    global game_field
    print(f'Ход {player.upper()} игрока')
    while True:
        x, y = None, None
        try:
            x = int(input('Введите номер позиции по горизонтали: '))
            y = int(input('Введите номер позиции по вертикали: '))
        except ValueError:
            print('Необходимо ввести целое число в диапозоне 0-2. Попробуйте еще раз.')
            continue

        if 0 <= x <= 2 and 0 <= y <= 2:
            if [x, y] not in players_turns['x'] and [x, y] not in players_turns['o']:
                turns.append([x, y])
                game_field[x][y] = player
                draw_field()
                break
            else:
                print('Упс, позиция уже занята. Выберите другую.')
                continue
        else:
            print('Необходимо ввести число в диапозоне 0-2. Попробуйте еще раз.')
            continue


def check_win(all_players_turns: dict, counter: int):
    key = 'x' if counter % 2 == 1 else 'o'
    player_turns = all_players_turns[key]
    for win_combination in win_combinations:
        if all(wp in player_turns for wp in win_combination):
            return True, key
    return False, ''


def end_round(player: str, score: list):
    print('-' * 12)
    if player:
        print(f'{player.upper()} игрок победил!')
        if player == 'x':
            score[0] += 1
        else:
            score[1] += 1
    else:
        print('Ничья!')
    print('-' * 12, f'Промежуточный счет {score[0]}:{score[1]}', '-' * 12, sep='\n')
    ng = input('Хотите продолжить игру? [y/n] ')
    return True if ng == 'y' else False


def main():
    global counter, has_winner
    print('Добро пожаловать в игру.....')
    print('<' * 12, 'Крестики-нолики', '>' * 12)
    print('-' * 24, '-' * 24, sep='\n')
    start_new_game()

    while True:
        if counter % 2 == 0:
            make_a_move('x', players_turns['x'])
        else:
            make_a_move('o', players_turns['o'])
        counter += 1
        if counter > 4:
            has_winner, player = check_win(players_turns, counter)
            if has_winner:
                new_game = end_round(player, score)
                if new_game:
                    start_new_game()
                    continue
                else:
                    break

        if counter > 8:
            new_game = end_round('', score)
            if new_game:
                start_new_game()
                continue
            else:
                break

    print('-' * 12, f'Финальный счет {score[0]}:{score[1]}','-' * 12, sep='\n')
    print('Спасибо за игру!')


main()
