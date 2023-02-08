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
    public int $length;

    public function __construct()
    {
        $this->head = null;
        $this->length = 0;
    }

    public function append(mixed $data, ?string $options = 'end'): void {
        $node = new Node($data);

        if ($options == 'front') {
            $node->next = $this->head;
            $this->head = $node;
            $this->length++;
            return;
        }

        if (!$this->head) {
            $this->head = $node;
            $this->length++;
            return;
        }

        $temp = $this->head;
        while($temp->next) {
            $temp = $temp->next;
        }
        $temp->next = $node;
        $this->length++;
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

    public function size(): int {
        return $this->length;
    }

}

function main(): void {

    $ll = new LinkedList();
    $lld = new LinkedList();
    $lla = new LinkedList();
    $llf = new LinkedList();

    $arr = [6,4,3,1,10,8,9,12,0];

    for($i = 0; $i <= 5; $i++) {
        $ll->append($i);
        $lld->append($i, options: 'front');
    }

    foreach($arr as $i) {
        $lla->append($i);
        $llf->append($i, options: 'front');
    }

    $ll->print();
    echo PHP_EOL;
    $ll->printReverse();
    echo PHP_EOL .$ll->length .PHP_EOL;
    echo $ll->size() .PHP_EOL;

    echo PHP_EOL;

    $lld->print();
    echo PHP_EOL;
    $lld->printReverse();
    echo PHP_EOL .$lld->length .PHP_EOL;
    echo $lld->size() .PHP_EOL;

    echo PHP_EOL;

    $lla->print();
    echo PHP_EOL;
    $lla->printReverse();
    echo PHP_EOL .$lla->length .PHP_EOL;
    echo $lla->size() .PHP_EOL;

    echo PHP_EOL;

    $llf->print();
    echo PHP_EOL;
    $llf->printReverse();
    echo PHP_EOL .$llf->length .PHP_EOL;
    echo $llf->size() .PHP_EOL;

}

main();
