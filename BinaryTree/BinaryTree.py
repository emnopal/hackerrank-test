from __future__ import annotations
from typing import TypeVar

Numeric = TypeVar("Numeric", int, float)


class Node:
    def __init__(self, data: Numeric) -> None:
        self.data: Numeric = data
        self.left: Node = None
        self.right: Node = None

    def insert(self, data: Numeric):

        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)


    def find(self, data) -> bool:
        if data == self.data:
            return True
        if data < self.data:
            if self.left:
                self.left.find(data)
            return False
        if self.right:
            self.right.find(data)
        return False

    def show(self, order='pre') -> None:
        if self:

            if order == 'in':
                if self.left:
                    self.left.show(order)
                print(str(self.data), end = ' ')
                if self.right:
                    self.right.show(order)
                return

            if order == 'post':
                if self.left:
                    self.left.show(order)
                if self.right:
                    self.right.show(order)
                print(str(self.data), end = ' ')
                return

            print(str(self.data), end = ' ')
            if self.left:
                self.left.show(order)
            if self.right:
                self.right.show(order)
            return


class Tree:
    def __init__(self) -> None:
        self.root: Node = None

    def insert(self, data: Numeric) -> Tree:
        if self.root:
            return self.root.insert(data)
        self.root = Node(data)
        return self

    def find(self, data: Numeric) -> bool:
        if self.root:
            return self.root.find(data)
        return False

    def show(self, order='pre') -> None:
        if self.root:
            print(f'\n\n{order.capitalize()}order: ')
            self.root.show(order)

if __name__ == '__main__':
    tree = Tree()

    arr = [10,12,5,4,20,8,7,15,13]

    for i in arr:
        tree.insert(i)

    print(tree.find(1))
    print(tree.find(12))

    tree.show('pre')
    tree.show('in')
    tree.show('post')
