from tqdm import tqdm
import random


def test_your_luck(bet):
    win = 0
    for i in tqdm(range(0, bet)):
        win_bet = 0
        result_num_1 = random.randrange(0, 10)
        result_num_2 = random.randrange(0, 10)
        result_num_3 = random.randrange(0, 10)
        if result_num_1 == 1 and result_num_2 == 1 and result_num_3 == 1:
            win_bet = 10
        elif result_num_1 == 3 and result_num_2 == 3 and result_num_3 == 3:
            win_bet = 15
        elif result_num_1 == 5 and result_num_2 == 5 and result_num_3 == 5:
            win_bet = 50
        elif result_num_1 == 9 and result_num_2 == 9 and result_num_3 == 9:
            win_bet = 100
        elif result_num_1 == 7 and result_num_2 == 7 and result_num_3 == 7:
            win_bet = 200
        elif result_num_2 == 0 and result_num_3 == 0:
            win_bet = 2
        elif result_num_3 == 0:
            win_bet = 1
        elif result_num_2 == 7 and result_num_3 == 7:
            win_bet = 5
        elif result_num_3 == 7:
            win_bet = 3
        win += win_bet
    win = ((win - bet) / bet) * 100
    if win > 0:
        print(f'Ставка: {bet}\n'
              f'Выигрыш: {win}\n')
    elif win < 0:
        print(f'Ставка: {bet}\n'
              f'Проигрыш: {win}\n')


test_your_luck(100000000)
