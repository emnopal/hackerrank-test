package main

import "fmt"

type Node struct {
	data interface{}
	next *Node
}

type LinkedList struct {
	head *Node
}

func (list *LinkedList) append(data interface{}) {
	var node *Node = &Node{
		data: data,
		next: nil,
	}

	if list.head == nil {
		list.head = node
	} else {
		var temp *Node = list.head
		for temp.next != nil {
			temp = temp.next
		}
		temp.next = node
	}
}

func (list *LinkedList) reverse() (newNode *Node){
	// use bubble sort for reversing
	newNode = nil
	var temp *Node = list.head
	for temp != nil {
		var next_node *Node = temp.next
		temp.next = newNode
		newNode = temp
		temp = next_node
	}
	return
}

func (list *LinkedList) print() {
	var node *Node = list.head
	for node != nil {
		fmt.Println(node.data)
		node = node.next
	}
}

func (list *LinkedList) printBackwards() {
	var node *Node = list.reverse()
	for node != nil {
		fmt.Println(node.data)
		node = node.next
	}
}

func main() {
	var ll *LinkedList = &LinkedList{}

	for i := 0; i <= 5; i++ {
		ll.append(i)
	}

	ll.print()
	fmt.Println()
	ll.printBackwards()

}