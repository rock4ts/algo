
class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_stack = []

    def push(self, item):
        if not self.max_stack or self.max_stack[-1] < item:
            self.max_stack.append(item)
        else:
            self.max_stack.append(self.max_stack[-1])
        self.items.append(item)

    def pop(self):
        if self.items:
            self.items.pop()
            self.max_stack.pop()
        else:
            print('error')

    def get_max(self):
        if self.max_stack:
            print(self.max_stack[-1])
        else:
            print('None')


if __name__ == '__main__':
    number_of_commands = int(input())
    stack = StackMaxEffective()

    for _ in range(number_of_commands):
        input_vals = input()
        try:
            command, value = input_vals.split()
            stack_command = getattr(stack, command)
            stack_command(int(value))
        except:
            command = input_vals
            stack_command = getattr(stack, command)
            stack_command()


# 10
# get_max
# push -6
# pop
# pop
# get_max
# push 2
# get_max
# pop
# push -2
# push -6
