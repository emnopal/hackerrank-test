<?php

namespace BinaryTree {
    class Node
    {
        public int|float $data;
        public ?Node $left;
        public ?Node $right;

        public function __construct(int|float $data)
        {
            $this->data = $data;
            $this->left = null;
            $this->right = null;
        }

        public function insert(int|float $data): void
        {
            if ($this->data === $data) {
                return;
            }
            if ($data < $this->data) {
                if ($this->left) {
                    $this->left->insert($data);
                } else {
                    $this->left = new Node($data);
                }
            } else {
                if ($this->right) {
                    $this->right->insert($data);
                } else {
                    $this->right = new Node($data);
                }
            }
        }

        public function find(int|float $data): bool
        {
            if ($this->data === $data) {
                return true;
            }
            if ($data < $this->data) {
                if ($this->left) {
                    return $this->left->find($data);
                }
                return false;
            }
            if ($this->right) {
                return $this->right->find($data);
            }
            return false;
        }

        public function show(string $position = 'pre'): void
        {
            if ($this) {
                switch ($position) {
                    case 'pre':
                        echo $this->data . " ";
                        if ($this->left) {
                            $this->left->show($position);
                        }
                        if ($this->right) {
                            $this->right->show($position);
                        }
                        return;
                    case 'in':
                        if ($this->left) {
                            $this->left->show($position);
                        }
                        echo $this->data . " ";
                        if ($this->right) {
                            $this->right->show($position);
                        }
                        return;
                    case 'post':
                        if ($this->left) {
                            $this->left->show($position);
                        }
                        if ($this->right) {
                            $this->right->show($position);
                        }
                        echo $this->data . " ";
                        return;
                    default:
                        echo $this->data . " ";
                        if ($this->left) {
                            $this->left->show($position);
                        }
                        if ($this->right) {
                            $this->right->show($position);
                        }
                        return;
                }
            }
        }
    }

    class Tree
    {
        private ?Node $root;

        public function __construct()
        {
            $this->root = null;
        }

        public function insert(int|float $data): Tree
        {
            if ($this->root) {
                $this->root->insert($data);
            } else {
                $this->root = new Node($data);
            }
            return $this;
        }

        public function find(int|float $data): bool
        {
            if ($this->root) {
                return $this->root->find($data);
            }
            return false;
        }

        public function show(string $position = 'pre'): void
        {
            echo $position . ": " . PHP_EOL;
            if ($this->root) {
                $this->root->show($position);
            }
            echo PHP_EOL;
        }
    }

    function main() {

        $tree = new Tree();

        $arr = [10, 12, 5, 4, 20, 8, 7, 15, 13];
        foreach($arr as $i) {
            $tree->insert($i);
        }
        echo $tree->find(1) ? 'true' : 'false' .PHP_EOL;
        echo $tree->find(12) ? 'true' : 'false' .PHP_EOL;

        echo PHP_EOL .PHP_EOL;

        $tree->show(position: "pre");
        $tree->show(position: "in");
        $tree->show(position: "post");
    }

    main();

}
