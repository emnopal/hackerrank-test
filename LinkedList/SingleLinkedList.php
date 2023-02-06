<?php

class Node{
    public mixed $data;
    public ?Node $next;

    public function __construct(mixed $data) {
        $this->data = $data;
        $this->next = null;
    }

}

class LinkedList {
    private ?Node $head;

    public function __construct()
    {
        $this->head = null;
    }

    public function append(mixed $data, ?string $options = 'end'): void {
        $node = new Node($data);

        if ($options == 'front') {
            $node->next = $this->head;
            $this->head = $node;
            return;
        }

        if (!$this->head) {
            $this->head = $node;
            return;
        }

        $temp = $this->head;
        while($temp->next) {
            $temp = $temp->next;
        }
        $temp->next = $node;
        return;

    }

    public function reverse(): Node {
        $reverseLL = null;
        $temp = $this->head;
        while($temp) {
            $next_node = $temp->next;
            $temp->next = $reverseLL;
            $reverseLL = $temp;
            $temp = $next_node;
        }
        return $reverseLL;
    }

    public function print(): void {
        $node = $this->head;
        while($node) {
            echo $node->data .' ';
            $node = $node->next;
        }
    }

    public function printReverse(): void {
        $node = $this->reverse();
        while($node) {
            echo $node->data .' ';
            $node = $node->next;
        }
    }

}

function main(): void {
    $ll = new LinkedList();
    $lld = new LinkedList();

    for($i = 0; $i <= 5; $i++) {
        $ll->append($i);
    }
    $ll->print();
    echo PHP_EOL;
    $ll->printReverse();

    echo PHP_EOL;

    for($i = 0; $i <= 5; $i++) {
        $lld->append($i, options: 'front');
    }
    $lld->print();
    echo PHP_EOL;
    $lld->printReverse();
}

main();
