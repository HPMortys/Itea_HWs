# 2. Описать класс «домашняя библиотека».
# Предусмотреть возможность работы с произвольным числом книг, поиска книги по какому-либо признаку (например,
# по автору или по году издания), добавления книг в библиотеку, удаления книг из нее, сортировки книг по разным полям.
#


class HomeLib:
    def __init__(self, idb: int, year: int, author: str):
        self.idb = idb
        self.author = author
        self.year = year

    def setnewBook(self):
        self.author = input('Введите автора: ')
        self.year = int(input('Введите год:'))

    def retrnInfoBook(self, num):
        return [self.idb, self.author, self.year][num]


def printBook(book):
    print('%15s %15s %15s' % ('id', 'year', 'author'))
    print('%15i %15i %15s' % (book.idb, book.year, book.author))

def printHomelib(homelib):
    print('%15s %15s %15s' % ('id', 'year', 'author'))
    for book in homelib:
        print('%15i %15i %15s' % (book.idb, book.year, book.author))


def findBook(homelib):
    temp = int(input('Введите : 0 - id , 1 - год , 2 - автор\n = '))
    temp1 = int(input('Введите значения: '))
    for book in homelib:
        if temp1 == book.retrnInfoBook(temp):
            return book


def addBook(homelib):
    id = int(input('Введите id:'))
    year = int(input('Введите год: '))
    author = str(input('Введите автора: '))
    homelib.append(HomeLib(id, year, author))


def delBook(homelib):
    homelib.remove(findBook(homelib))

homelib = [HomeLib(1, 2001, 'Ab'), HomeLib(3, 1998, 'Basdfq ASD'), HomeLib(2, 2005, 'n')]

while True:
    temp = int(input('Введите : 1 - найти книгу , 2 - добавления книги , 3 - удалить книгу , 4 - сортировка\n = '))
    if temp == 1:
        printBook(findBook(homelib))
    elif temp == 2:
        addBook(homelib)
    elif temp == 3:
        delBook(homelib)
    elif temp == 4:
        temp1 = int(input('Введите : 0 - id , 1 - год , 2 - автор\n = '))
        if  temp1 == 1:
            homelib = sorted(homelib, key=lambda x: x.year)
        elif temp == 2:
            homelib = sorted(homelib, key=lambda x: x.author)
        else:
            homelib = sorted(homelib, key=lambda x: x.idb)
        printHomelib(homelib)