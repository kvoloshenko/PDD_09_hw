import numpy as np
import random


def random_array(low, high, size):
    number_of_unique_attempts = 0
    while (number_of_unique_attempts != size):  # пока не получим 5 разных случайных чисел
        random_integer_array = np.random.randint(low, high, size)
        # print(random_integer_array)
        s_digits = set(random_integer_array)
        number_of_unique_attempts = len(s_digits)
        # print ('number_of_unique_attempts=',number_of_unique_attempts)
    return random_integer_array


class Card:
    nums = []
    lines = []

    def set_nums(self):
        random_integer_array = random_array(1, 90, 15)
        # print(random_integer_array)
        l1 = random_integer_array[0:5]
        l2 = random_integer_array[5:10]
        l3 = random_integer_array[10:15]
        # print(l1, l2, l3)
        # print(type(l1))
        l1.sort()
        l2.sort()
        l3.sort()
        # print(l1, l2, l3)
        cl1 = Card_line()
        cl1.set_nums(l1)
        self.lines.append(cl1)
        # n1 = cl1.get_nums()
        # print(type(n1), f'n1={n1}')
        cl2 = Card_line()
        cl2.set_nums(l2)
        self.lines.append(cl2)
        # n2 = cl2.get_nums()
        # print(type(n2), f'n2={n2}')
        cl3 = Card_line()
        cl3.set_nums(l3)
        self.lines.append(cl3)
        # n3 = cl3.get_nums()
        # print(type(n3), f'n3={n3}')

    def print_card(self):
        print('-------------------------------')
        for card_line in self.lines:
            nums = card_line.get_nums()
            # print(nums)
            s = ''
            for num in nums:
                if num == 0: s += '    '
                elif num == -1: s += '  - '
                elif num > 10: s += ' ' +str(num) + ' '
                else: s += '  ' + str(num) + ' '
            print(s)
        print('-------------------------------')

    def cross_out (self, num):
        rez = False
        for card_line in self.lines:
            index = card_line.cross_out(num)
            if index != -1:
                rez = True
                # print(f'index={index}')
        # print(f'rez={rez}')
        return rez

    def is_crossed(self):
        rezault = 0
        for card_line in self.lines:
            if card_line.is_crossed(): rezault +=1
        if rezault == 3: return True
        else: return  False


class Card_line:
    n = []

    def set_nums(self, nums):
        self.n = [0] * 9
        # print(type(self.n), self.n)
        pos = random_array(0, 8, 5)
        pos.sort()
        # print(F'pos={pos}')
        j = 0
        for i in nums:
            y = pos[j]
            # print(i, 'j=', j, ' pos[j]=', pos[j], ' y=',y)
            self.n[y] = i
            # print(f'n[y]={self.n[y]}')
            j += 1
        # print(f'n={self.n}')

    def get_nums(self):
        return self.n

    def cross_out (self, num):
        index = -1
        # print(f'count={self.n.count(num)}')
        if self.n.count(num):
            # print(f'  index={self.n.index(num)}')
            index = self.n.index(num)
            self.n[index] = -1
            # print(f'   self.n[{index}]={self.n[index]}')
        return index

    def is_crossed(self):
        if self.n.count(-1) == 5 : return True
        else: return False



if __name__ == '__main__':
    crd = Card()
    crd.set_nums()
    crd.print_card()
    rez = crd.cross_out(1)
    if rez: crd.print_card()
    rez = crd.cross_out(21)
    if rez: crd.print_card()
