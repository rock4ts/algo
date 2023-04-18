# посылка 81894779


class EmptyDequeError(Exception):
    '''
    Raised on attempt to delete item from an empty deque object.
    '''
    def __init__(self, message='error'):
        self.message = message
        super().__init__(self.message)


class FullDequeError(EmptyDequeError):
    '''
    Raised on attempt to add item to a full deque object.
    '''


class Deque:

    def __init__(self, max_size):
        self._items = [None] * max_size
        self._max_size = max_size
        self._head = 0
        self._tail = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._max_size == self._size

    def push_back(self, value):
        if self.is_full():
            raise FullDequeError
        if self.is_empty():
            self._head = (self._head - 1) % self._max_size
        self._items[self._tail] = value
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1

    def push_front(self, value):
        if self.is_full():
            raise FullDequeError
        if self.is_empty():
            self._tail = (self._tail + 1) % self._max_size
        self._items[self._head] = value
        self._head = (self._head - 1) % self._max_size
        self._size += 1

    def pop_back(self):
        if self.is_empty():
            raise EmptyDequeError
        back_elem_idx = (self._tail - 1) % self._max_size
        deleted_elem = self._items[back_elem_idx]
        self._items[back_elem_idx] = None
        self._tail = back_elem_idx
        self._size -= 1
        if self.is_empty():
            self._head = (self._head + 1) % self._max_size
        return deleted_elem

    def pop_front(self):
        if self.is_empty():
            raise EmptyDequeError
        front_elem_idx = (self._head + 1) % self._max_size
        deleted_elem = self._items[front_elem_idx]
        self._items[front_elem_idx] = None
        self._head = front_elem_idx
        self._size -= 1
        if self.is_empty():
            self._tail = (self._tail - 1) % self._max_size
        return deleted_elem


if __name__ == '__main__':
    number_of_commands = int(input())
    deque_max_size = int(input())
    deque = Deque(deque_max_size)

    for _ in range(number_of_commands):
        command = input()
        try:
            command, value = command.split()
        except ValueError:
            value = None

        deque_command = getattr(deque, command)

        if value:
            try:
                deque_command(value)
            except FullDequeError as error:
                print(error)
        else:
            try:
                print(deque_command())
            except EmptyDequeError as error:
                print(error)
