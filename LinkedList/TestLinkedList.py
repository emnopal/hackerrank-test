from typing import Optional, Self, TypeVar


T = TypeVar("T")

class Node:
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.prev: T = None
        self.next: T = None

class TestLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        a = ''
        while self.head:
            a += str(self.head)
            self.head = self.head.next
        return a

    def append(self, data: T) -> None:
        new_node: Node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def reverse(self) -> Node:
        new_list: Node = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = new_list
            new_list = temp
            temp = next_node
        return new_list

    def print_forward(self) -> None:
        node = self.head
        print('[', end='')
        while node:
            print(node.data, end=',')
            node = node.next
        print(']')

    def print_backward(self) -> None:
        node = self.reverse()
        print('[', end='')
        while node:
            print(node.data, end=',')
            node = node.next
        print(']')

if __name__ == '__main__':
    s = TestLinkedList()
    # for i in [1,2,3,4,5]:
    #     s.append(i)
    # s.print_forward()
    # s.print_backward()

    # a = TestLinkedList()
    # a.append(10)
    # a.print_backward()
    # a.print_forward()

    for i in range(10):
        s.append(i)
    s.print_forward()
    s.print_backward()

