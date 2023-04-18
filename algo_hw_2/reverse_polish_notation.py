# посылка 81889791

import operator

operations_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


class EmptyStackError(Exception):
    '''Raised on attempt to get or delete element of an empty stack object.'''

    def __init__(
            self,
            message='Failed to get item from empty stack object.'
        ):
        self.message = message
        super().__init__(self.message)


class Stack:
    def __init__(self):
        self._items = []
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, item):
        self._items.append(item)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError
        self._size -= 1
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError
        return self._items[-1]


def calculate_polish_sequence(sequence, stack_object, operations_dict):
    for symbol in sequence:
        if symbol in operations_dict:
            second_operand = stack_object.pop()
            first_operand = stack_object.pop()
            current_calculation_result = (
                operations_dict[symbol](first_operand, second_operand)
            )
            stack_object.push(current_calculation_result)
        else:
            stack_object.push(int(symbol))
    return stack_object.peek()


if __name__ == '__main__':
    polish_sequence = input().split()
    stack_object = Stack()

    try:
        print(
            calculate_polish_sequence(
                polish_sequence, stack_object, operations_dict
            )
        )
    except EmptyStackError as error:
        print(
            error,
            'Not enough operands to perform calculation.'
        )
