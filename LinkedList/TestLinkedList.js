class Node{
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    append(data) {
        const node = new Node(data);
        if (!this.head) {
            this.head = node;
        } else {
            let temp = this.head;
            while(temp.next) {
                temp = temp.next;
            }
            temp.next = node;
        }
    }

    reverse() {
        let new_node = null;
        let temp = this.head;
        while (temp) {
            let next_node = temp.next;
            temp.next = new_node;
            new_node = temp;
            temp = next_node;
        }
        return new_node;
    }

    print() {
        let node = this.head;
        while(node.next){
            console.log(node.data);
            node = node.next;
        }
    }

    printBackwards() {
        let node = this.reverse()
        while(node.next){
            console.log(node.data);
            node = node.next;
        }
    }

}

const ll = new LinkedList();

for (let i = 0; i <= 5; i++) {
    ll.append(i);
}

ll.print();
console.log()
ll.printBackwards();