from Card import Card
from Keg import Keg
from Kegs import Kegs

if __name__ == '__main__':
    crd = Card()
    crd.set_nums()
    crd.print_card()
    k = Kegs()
    k.kreate_kegs()
    current = 0
    while current < 91:
        cur_num = k.get_next().get_num()
        current = k.get_current()
        # print(f'cur_num={cur_num} current={current}')
        print(f'Новый бочонок: {cur_num} (осталось {90 - current})')
        rez = crd.cross_out(cur_num)
        if rez: crd.print_card()
        if current == 90 :
            print(' Кончились боченки')
            break
        if crd.is_crossed():
            print('Карточка вычеркнута польностью')
            break