package main

import (
	"C"
	"fmt"
)

type NumTypes interface {
	int | int64 | float32 | float64 | uint | uint64
}

type Node[Numeric NumTypes] struct {
	data  Numeric
	left  *Node[Numeric]
	right *Node[Numeric]
}

type Tree[Numeric NumTypes] struct {
	root *Node[Numeric]
}

type Options struct {
	order string
}

func (node *Node[Numeric]) insert(data Numeric) {
	if node.data == data {
		return
	}
	if data < node.data {
		if node.left != nil {
			node.left.insert(data)
		} else {
			node.left = &Node[Numeric]{
				data:  data,
				left:  nil,
				right: nil,
			}
		}
	} else {
		if node.right != nil {
			node.right.insert(data)
		} else {
			node.right = &Node[Numeric]{
				data:  data,
				left:  nil,
				right: nil,
			}
		}
	}
}

func (node *Node[Numeric]) find(data Numeric) bool {
	if data == node.data {
		return true
	}
	if data < node.data {
		if node.left != nil {
			return node.left.find(data)
		}
		return false
	}
	if node.right != nil {
		return node.right.find(data)
	}
	return false
}

func (node *Node[Numeric]) show(options *Options) {
	if node != nil {
		switch options.order {
		case "pre":
			fmt.Print(node.data, " ")
			if node.left != nil {
				node.left.show(options)
			}
			if node.right != nil {
				node.right.show(options)
			}
			return
		case "in":
			if node.left != nil {
				node.left.show(options)
			}
			fmt.Print(node.data, " ")
			if node.right != nil {
				node.right.show(options)
			}
			return
		case "post":
			if node.left != nil {
				node.left.show(options)
			}
			if node.right != nil {
				node.right.show(options)
			}
			fmt.Print(node.data, " ")
			return
		default:
			fmt.Print(node.data, " ")
			if node.left != nil {
				node.left.show(options)
			}
			if node.right != nil {
				node.right.show(options)
			}
			return
		}
	}

}

func (tree *Tree[Numeric]) insert(data Numeric) *Tree[Numeric] {
	if tree.root != nil {
		tree.root.insert(data)
	} else {
		tree.root = &Node[Numeric]{
			data:  data,
			left:  nil,
			right: nil,
		}
	}
	return tree
}

func (tree *Tree[Numeric]) find(data Numeric) bool {
	var node *Node[Numeric] = tree.root
	if node != nil {
		return node.find(data)
	}
	return false
}

func (tree *Tree[Numeric]) show(options *Options) {
	var node *Node[Numeric] = tree.root
	fmt.Print(options.order, ": ")
	if node != nil {
		node.show(options)
	}
	fmt.Println()
}

func main() {
	var arr []int = []int{10, 12, 5, 4, 20, 8, 7, 15, 13}
	var tree Tree[int] = Tree[int]{
		root: nil,
	}
	for _, i := range arr {
		tree.insert(i)
	}
	fmt.Println(tree.find(1))
	fmt.Println(tree.find(12))
	tree.show(&Options{order: "pre"})
	tree.show(&Options{order: "in"})
	tree.show(&Options{order: "post"})
}
