# посылка 81816973

#    '''
#    Дек, где после добавления первого элемента, индексы head и tail расходятся
#    относительно его индекса на шаг назад и вперёд соответственно, 
#    и указывают на разные пустые ячейки последовательности,
#    если её максимальная длина больше единицы, 
#    или на одну и ту же пустую ячейку, если максимальная длина равна двум.
#    При удалении последнего элемента индексы head и tail снова сходятся и
#    указывают на одну и то же пустую ячейку последовательности.
#    '''

class Deck:
    '''
    Дек, где по индексам head и tail можно сразу найти значения начала и конца
    последовательности (без прибавления или вычитания единицы соответственно)
    Поэтому при добавлении или удалении единственного элемента последовательности,
    нет необходимости смещать индексы head или tail.
    '''
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def has_one_elem(self):
        return self.size == 1

    def is_full(self):
        return self.max_size == self.size

    def push_back(self, value):
        if self.is_full():
            print('error')
            return
        if not self.is_empty():
            self.tail = (self.tail + 1) % self.max_size
        self.queue[self.tail] = value
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            print('error')
            return
        if not self.is_empty():
            self.head = (self.head - 1) % self.max_size
        self.queue[self.head] = value
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            print('error')
            return
        deleted_elem = self.queue[self.tail]
        self.queue[self.tail] = None
        if not self.has_one_elem():
            self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        print(deleted_elem)

    def pop_front(self):
        if self.is_empty():
            print('error')
            return
        deleted_elem = self.queue[self.head]
        self.queue[self.head] = None
        if not self.has_one_elem():
            self.head = (self.head + 1) % self.max_size
        self.size -= 1
        print(deleted_elem)


if __name__ == '__main__':
    number_of_commands = int(input())
    deck_max_size = int(input())
    deck = Deck(deck_max_size)

    for _ in range(number_of_commands):
        command = input()
        try:
            command, value = command.split()
            deck_command = getattr(deck, command)
            deck_command(value)
        except ValueError:
            deck_command = getattr(deck, command)
            deck_command()
