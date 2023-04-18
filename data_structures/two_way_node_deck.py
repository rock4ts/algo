# посылка 81847449


class Node:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class Deck:
    '''
    Дек, реализованный с помощью двусвязного списка.
    '''
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = None
        self.tail = self.head
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def has_one_elem(self):
        return self.size == 1

    def is_full(self):
        return self.size == self.max_size

    def push_back(self, new_node):
        if self.is_full():
            print('error')
            return
        if self.is_empty():
            self.tail = new_node
            self.head = self.tail
        else:
            previous_node = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.previous = previous_node
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            print('error')
            return
        former_tail_node = self.tail
        if self.has_one_elem():
            self.tail = None
            self.head = self.tail
        else:
            previous_node = self.tail.previous
            self.tail = previous_node
            self.tail.next = None
        self.size -= 1
        print(former_tail_node.value)

    def push_front(self, new_node):
        if self.is_full():
            print('error')
            return
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            next_node = self.head
            self.head.previous = new_node
            self.head = new_node
            self.head.next = next_node
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            print('error')
            return
        former_head_node = self.head
        if self.has_one_elem():
            self.head = None
            self.tail = self.head
        else:
            next_node = self.head.next
            self.head = next_node
            self.head.previous = None
        self.size -= 1
        print(former_head_node.value)


if __name__ == '__main__':
    number_of_commands = int(input())
    deck_max_size = int(input())
    deck = Deck(deck_max_size)

    for _ in range(number_of_commands):
        command = input()
        try:
            command, value = command.split()
            new_node = Node(value)
            deck_command = getattr(deck, command)
            deck_command(new_node)
        except ValueError:
            deck_command = getattr(deck, command)
            deck_command()

# 7
# 10
# push_front -855
# push_front 0
# pop_back
# pop_back
# push_back 844
# pop_back
# push_back 823
