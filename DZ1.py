import random


class CounterD:
    def __init__(self, num, drange: range):
        self.num = num
        self.drange = drange

    def autoSetNumRange(self):
        self.num = 5
        self.drange = range(0, 100)
        self.getNumR()

    def randSetNumRange(self):
        self.drange = range(random.randint(-50, 0), random.randint(0, 51))
        self.num = random.choice(self.drange)
        self.getNumR()

    def __add__(self, other):
        if self.num + other not in self.drange:
            print('Не в диапозоне\n' + '-' * 25)
        else:
            self.num = self.num + other
            return self.num

    def __sub__(self, other):
        if self.num - other not in self.drange:
            print('Не в диапозоне\n' + '-' * 25)
        else:
            self.num = self.num - other
            return self.num

    def getNumR(self):
        print('Значения cчётчика: %s %s' % (self.num, self.drange))


counter = CounterD(0, range(0, 0))


def whattodo():
    temp = int(input('Введите : 1 -  значения счетчик по умолчанию  , 0 -  произвольные значения счётчика\n = '))
    if temp:
        counter.autoSetNumRange()
    else:
        counter.randSetNumRange()
    while True:
        temp1 = int(input('Введите : 0 - закончить, 1 - отнять число , 2 - добавить число \n = '))
        if temp1 == 1:
            num1 = int(input('Введите число: '))
            counter - num1
            counter.getNumR()
        elif temp1 == 2:
            num2 = int(input('Введите число: '))
            counter + num2
            counter.getNumR()
        else:
            counter.getNumR()
            break


whattodo()
