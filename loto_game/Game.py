from Card import Card
from Keg import Keg
from Kegs import Kegs
from Player import Player

if __name__ == '__main__':
    players = []
    p1 = Player()
    p1.set_name('Константин')
    c1 = Card()
    c1.set_header('------ Ваша карточка ----------')
    p1.set_card(c1)
    players.append(p1)

    p2 = Player()
    p2.set_name('Компьютер')
    c2 = Card()
    c2.set_header('---- Карточка компьютера ------')
    p2.set_card(c2)
    players.append(p2)

    k = Kegs()
    k.kreate_kegs()
    current = 0

    game_over = False
    winner = None
    while current < 91:
        cur_num = k.get_next().get_num()
        current = k.get_current()
        # print(f'cur_num={cur_num} current={current}')
        print(f'Новый бочонок: {cur_num} (осталось {90 - current})')

        for player in players:
            crd = player.get_card()
            crd.print_card()
            # TODO сюда отличие действий пользователя и компьютера
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
            print(f' *** Ура!!! Победил {winner}!!! ***')
            print(f' *** Игра окончена!!! ***')
            break

        if current == 90 :
            print(' Кончились боченки')
            break
