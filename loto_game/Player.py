from loto_game.Card import Card

class Player:

    def set_card(self, card):
        self.card = card

    def get_card(self):
        return self.card

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def __init__(self):
        self.set_type('Human')
        self.set_card(Card())


if __name__ == '__main__':
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

    for player in players:
        print(f'{player.get_name()}')
        crd = player.get_card()
        crd.print_card()

