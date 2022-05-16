from loto_game.Keg import Keg
import random


# keg_1 = Keg()
# print(f'keg_1.get_num()={keg_1.get_num()}')
# keg_1.set_num(99)
# print(f'keg_1.get_num()={keg_1.get_num()}')

class Kegs:
    kegs = []
    i = 0

    def __int__(self):
        pass

    def kreate_kegs(self):
        for i in range(1, 91):
            keg = Keg()
            keg.set_num(i)
            # print(f'keg.get_num()={keg.get_num()}')
            self.kegs.append(keg)
        random.shuffle(self.kegs)

    def get_kegs(self):
        return self.kegs

    def get_next(self):
        # print(f' i before get_nex={self.i}')
        k = self.kegs[self.i]
        self.i += 1
        return k

    def get_current(self):
        return self.i


if __name__ == '__main__':
    k = Kegs()
    k.kreate_kegs()
    kegs = k.get_kegs()
    print(type(kegs), f' len(kegs)={len(kegs)} kegs={kegs}')
    keg = kegs[0]
    print(type(keg), keg.get_num())
    for kk in kegs:
        print(f'keg_num={kk.get_num()}')
    print(f'get_next={k.get_next().get_num()} curent={k.get_current()}')
    print(f'get_next={k.get_next().get_num()} curent={k.get_current()}')
