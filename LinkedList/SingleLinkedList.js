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

    append(data, position) {
        const node = new Node(data);

        if (position === 'front') {
            node.next = this.head;
            this.head = node;
            return;
        }

        if (!this.head) {
            this.head = node;
            return;
        }

        let temp = this.head;
        while(temp.next) {
            temp = temp.next;
        }
        temp.next = node;
        return;
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
        while(node){
            console.log(node.data);
            node = node.next;
        }
    }

    printBackwards() {
        let node = this.reverse()
        while(node){
            console.log(node.data);
            node = node.next;
        }
    }

}

const main = () => {
    const ll = new LinkedList();
    const lld = new LinkedList();

    for (let i = 0; i <= 5; i++) {
        ll.append(i);
    }

    ll.print();
    console.log()
    ll.printBackwards();

    console.log()

    for (let i = 0; i <= 5; i++) {
        lld.append(i, position='front');
    }

    lld.print();
    console.log()
    lld.printBackwards();
}

main();