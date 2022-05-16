# from Card import Card
# from Keg import Keg
from loto_game.Kegs import Kegs
from loto_game.Player import Player


def enter_yn(msg):
    while True:
        answer = input(msg).upper()
        if answer == 'Y' or answer == 'N':
            return answer
            break
        else:
            print('Введите Y или N')
    return answer

class Game:

    def run(self):
        players = []
        p1 = Player()
        p1.set_name('Константин')
        c1 = p1.get_card()
        c1.set_header('------ Ваша карточка ----------')
        players.append(p1)

        p2 = Player()
        p2.set_name('Компьютер')
        p2.set_type('computer')
        c2 = p2.get_card()
        c2.set_header('---- Карточка компьютера ------')
        players.append(p2)

        k = Kegs()
        k.kreate_kegs()
        current = 0

        game_over = False
        winner = None
        loser = None
        while current < 91:
            cur_num = k.get_next().get_num()
            current = k.get_current()
            # print(f'cur_num={cur_num} current={current}')
            print(f'Новый бочонок: {cur_num} (осталось {90 - current})')

            for player in players:
                crd = player.get_card()
                crd.print_card()
            for player in players:
                crd = player.get_card()
                # crd.print_card()
                if player.get_type() == 'Human':
                    # Здесь отличия действий пользователя и компьютера
                    answer = enter_yn('Зачеркнуть цифру? (y/n)')
                    #print(f'answer={answer}')
                    if answer == 'Y':
                        rez = crd.cross_out(cur_num)
                        # print(f'answer={answer} rez={rez}')
                        if not rez:
                            game_over = True
                            loser = player.get_name()
                            print(f' *** {loser}, Вы проиграли: нет цифры {cur_num} в Вашей карточке ***')
                    else:
                        rez = crd.cross_out(cur_num)
                        # print(f'answer={answer} rez={rez}')
                        if rez:
                            game_over = True
                            loser = player.get_name()
                            print(f' *** {loser}, Вы проиграли: цифрf {cur_num} есть в Вашей карточке ***')
                else:  # Действия для компьютера
                    rez = crd.cross_out(cur_num)
                    if rez:
                        print(f'   Бочонок {cur_num} сыграл!!!')
                        crd.print_card()
                    if crd.is_crossed():
                        print('Карточка вычеркнута польностью')
                        game_over = True
                        winner = player.get_name()
                        break

            if game_over:
                if not loser: print(f' *** Ура!!! Победил {winner}!!! ***')
                print(f' *** Игра окончена!!! ***')
                break

            if current == 90:
                print(' Кончились боченки')
                break


if __name__ == '__main__':
    game = Game()
    game.run()
