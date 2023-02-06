from typing import Optional, TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: T = None

class SingleLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data: T, position: str = "end") -> None:
        new_node: Node = Node(data)

        if position == "front":
            new_node.next = self.head
            self.head = new_node
            return

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return

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
    s = SingleLinkedList()
    sb = SingleLinkedList()

    for i in range(10):
        s.append(i)
    s.print_forward()
    s.print_backward()

    print()

    for i in range(10):
        sb.append(i, position="front")
    sb.print_forward()
    sb.print_backward()
