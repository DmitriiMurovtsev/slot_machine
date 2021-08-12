from tqdm import tqdm
import random


class Gamer:
    def __init__(self):
        self.luck = 0
        self.win = 0


class Automate:

    def test_your_luck(Gamer, bet):
        win_dict = {
            '111': 10,
            '333': 15,
            '555': 50,
            '999': 100,
            '777': 200
        }
        for i in tqdm(range(0, bet)):
            win_bet = 0
            result_num_1 = random.randrange(0, 10)
            result_num_2 = random.randrange(0, 10)
            result_num_3 = random.randrange(0, 10)
            sum_result = str(result_num_1) + str(result_num_2) + str(result_num_3)
            if sum_result in win_dict:
                win_bet = win_dict[sum_result]
            elif sum_result[-1] == '0':
                win_bet = 1
            elif sum_result[-2] == '00':
                win_bet = 2
            elif sum_result[-1] == '7':
                win_bet = 3
            elif sum_result[-2] == '77':
                win_bet = 5
            Gamer.win += win_bet
        Gamer.win = Gamer.win - bet
        Gamer.luck = '{:.2f}'.format((Gamer.win / bet) * 100) + '%'
        if Gamer.win > 0:
            print(f'Ставка: {bet}\n'
                  f'Выигрыш: {Gamer.win}\n'
                  f'Процент выигрыша: {Gamer.luck}')
        elif Gamer.win < 0:
            print(f'Ставка: {bet}\n'
                  f'Проигрыш: {Gamer.win}\n'
                  f'Процент проигрыша: {Gamer.luck}')


lark = Gamer()
auto = Automate

auto.test_your_luck(lark, 1000000)
