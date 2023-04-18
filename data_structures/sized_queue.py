
class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def size(self):
        print(self.queue_size)

    def push(self, value):
        if self.queue_size == self.max_size:
            print('error')
        else:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.queue_size += 1

    def peek(self):
        if self.queue_size == 0:
            print('None')
        else:
            print(self.queue[self.head])

    def pop(self):
        if self.queue_size == 0:
            print('None')
        else:
            value = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.queue_size -= 1
            print(value)


if __name__ == '__main__':
    number_of_commands = int(input())
    max_size = int(input())
    sized_queue = MyQueueSized(max_size)

    for _ in range(number_of_commands):
        command = input()
        try:
            command, value = command.split()
            queue_command = getattr(sized_queue, command)
            queue_command(value)
        except:
            queue_command = getattr(sized_queue, command)
            queue_command()


# 10
# 1
# push 1
# size
# push 3
# size
# push 1
# pop
# push 1
# pop
# push 3
# push 3
