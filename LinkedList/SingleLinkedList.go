package main

import "fmt"

type Node struct {
	data interface{}
	next *Node
}

type LinkedList struct {
	head   *Node
	length int
}

type appendOptions struct {
	position string
}

func (list *LinkedList) append(data interface{}, options *appendOptions) {
	var node *Node = &Node{
		data: data,
		next: nil,
	}

	if options.position == "front" {
		node.next = list.head
		list.head = node
		list.length++
		return
	}

	if list.head == nil {
		list.head = node
		list.length++
		return
	}

	var temp *Node = list.head
	for temp.next != nil {
		temp = temp.next
	}
	temp.next = node
	list.length++
	return
}

func (list *LinkedList) reverse() (newNode *Node) {
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

func (list *LinkedList) size() int {
	return list.length
}

func main() {
	var ll *LinkedList = &LinkedList{}
	var lld *LinkedList = &LinkedList{}

	for i := 0; i <= 5; i++ {
		ll.append(i, &appendOptions{})
	}

	ll.print()
	fmt.Println()
	ll.printBackwards()
	fmt.Println()
	fmt.Println(ll.length)
	fmt.Println()
	fmt.Println(ll.size())

	fmt.Println()

	for i := 0; i <= 5; i++ {
		lld.append(i, &appendOptions{position: "front"})
	}

	lld.print()
	fmt.Println()
	lld.printBackwards()
	fmt.Println()
	fmt.Println(lld.length)
	fmt.Println()
	fmt.Println(lld.size())

}
