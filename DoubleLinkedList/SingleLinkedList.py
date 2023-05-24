from typing import Optional, Any, Self


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional[Self] = None


class SingleLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.length: int = 0

    def append(self, data: Any, position: str = "end") -> None:
        new_node: Node = Node(data)

        if position == "front":
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return

        if not self.head:
            self.head = new_node
            self.length += 1
            return

        temp: Node = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        self.length += 1
        return

    def reverse(self) -> Optional[Node]:
        new_list: Optional[Node] = None
        temp: Optional[Node] = self.head
        while temp:
            next_node = temp.next
            temp.next = new_list
            new_list = temp
            temp = next_node
        return new_list

    def print_forward(self) -> None:
        node: Optional[Node] = self.head
        print('[', end='')
        while node:
            print(node.data, end=',')
            node = node.next
        print(']')

    def print_backward(self) -> None:
        node: Optional[Node] = self.reverse()
        print('[', end='')
        while node:
            print(node.data, end=',')
            node = node.next
        print(']')

    def size(self) -> int:
        return self.length


if __name__ == '__main__':
    s: SingleLinkedList = SingleLinkedList()
    sb: SingleLinkedList = SingleLinkedList()
    sa: SingleLinkedList = SingleLinkedList()
    sf: SingleLinkedList = SingleLinkedList()

    for i in range(11):
        s.append(i)
        sb.append(i, position="front")

    for i in [6,4,3,1,10,8,9,12,0]:
        sa.append(i)
        sa.append(i, position="front")

    s.print_forward()
    s.print_backward()
    print(s.size())

    print()

    sb.print_forward()
    sb.print_backward()
    print(sb.size())

    print()

    sa.print_forward()
    sa.print_backward()
    print(sa.size())

    print()

    sf.print_forward()
    sf.print_backward()
    print(sf.size())
