from Card import Card

class Player:

    def set_card(self, card):
        self.card = card

    def get_card(self):
        return self.card

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

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

    for player in players:
        print(f'{player.get_name()}')
        crd = player.get_card()
        crd.print_card()

