
class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print('None')


if __name__ == '__main__':
    number_of_commands = int(input())
    stack = StackMax()

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

# 8
# get_max
# push 7
# pop
# push -2
# push -1
# pop
# get_max
# get_max
# 