

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class NodeQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def get(self):
        if self.queue_size > 0:
            old_head = self.head
            self.head = self.head.next
            self.queue_size -= 1
            print(old_head.value)
        else:
            print('error')

    def put(self, new_node):
        if self.queue_size > 0:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.queue_size += 1

    def size(self):
        print(self.queue_size)


if __name__ == '__main__':
    number_of_commands = int(input())
    linked_list_queue = NodeQueue()

    for _ in range(number_of_commands):
        command = input()
        try:
            command, node_value = command.split()
            queue_command = getattr(linked_list_queue, command)
            new_node = Node(node_value)
            queue_command(new_node)
        except:
            queue_command = getattr(linked_list_queue, command)
            queue_command()

# 
# 10
# put -34
# put -23
# get
# size
# get
# size
# get
# get
# put 80
# size
# 