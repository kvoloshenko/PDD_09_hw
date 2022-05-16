# from Card import Card
# from Keg import Keg
from loto_game.Kegs import Kegs
from loto_game.Player import Player

class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

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

    def enter_num_players(self, msg):
        while True:
            try:
                # Тот код который может вызвать исключение
                sum = int(input(msg))
                if sum < 2: raise ValueTooSmallError
            except ValueTooSmallError:
                print('Введите число больше или равное 2-м')
            except ValueError:
                # Этот блок срабатывает если было исключение
                print('Вы ввели не число')
                print('Введите верное число')
            else:
                # Выполняется когда нету ошибок
                # print(f'sum={sum}')
                break
        return sum

    def enter_num_coms(self, msg):
        while True:
            try:
                # Тот код который может вызвать исключение
                sum = int(input(msg))
                if sum > self.num_players: raise ValueTooLargeError
            except ValueTooLargeError:
                print('Введите число меньшее или равное количеству игроков')
            except ValueError:
                # Этот блок срабатывает если было исключение
                print('Вы ввели не число')
                print('Введите верное число')
            else:
                # Выполняется когда нету ошибок
                # print(f'sum={sum}')
                break
        return sum

    def create_players(self):
        self.players = []
        self.num_players = self.enter_num_players('Введите количество игроков:')
        self.comp_players = self.enter_num_coms('Введите количество компьютеров в игре:')
        # print(f' num_players={self.num_players} comp_players={self.comp_players}')
        self.human_players = self.num_players - self.comp_players
        for i in range (1, self.human_players+1):
            # print(f'i={i}')
            p = Player()
            p.set_name('Игрок №' + str(i))
            c = p.get_card()
            c.set_header('--- Ваша карточка: ' + p.get_name() + ' ---')
            self.players.append(p)

        for i in range(1, self.comp_players + 1):
            p = Player()
            p.set_name('Компьютер №' + str(i))
            p.set_type('computer')
            c = p.get_card()
            c.set_header('--- Ваша карточка: ' + p.get_name() + ' ---')
            self.players.append(p)


    def run(self):
        k = Kegs()
        k.kreate_kegs()
        current = 0
        game_over = False
        winner = None
        loser = None
        self.create_players()

        while current < 91:
            cur_num = k.get_next().get_num()
            current = k.get_current()
            # print(f'cur_num={cur_num} current={current}')
            print(f'Новый бочонок: {cur_num} (осталось {90 - current})')

            for player in self.players:
                crd = player.get_card()
                crd.print_card()
            for player in self.players:
                crd = player.get_card()
                # crd.print_card()
                if player.get_type() == 'Human':
                    # Здесь отличия действий пользователя и компьютера
                    answer = enter_yn(player.get_name() + ': Зачеркнуть цифру? (y/n)')
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
                        # print(f'   Бочонок {cur_num} сыграл!!!')
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
