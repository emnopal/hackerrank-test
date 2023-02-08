class Node{
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.length = 0;
    }

    append(data, position) {
        const node = new Node(data);

        if (position === 'front') {
            node.next = this.head;
            this.head = node;
            this.length++;
            return;
        }

        if (!this.head) {
            this.head = node;
            this.length++;
            return;
        }

        let temp = this.head;
        while(temp.next) {
            temp = temp.next;
        }
        temp.next = node;
        this.length++;
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

    size() {
        return this.length;
    }

}

const main = () => {
    const ll = new LinkedList();
    const lld = new LinkedList();
    const lla = new LinkedList();
    const llf = new LinkedList();
    const arr = [6,4,3,1,10,8,9,12,0];

    for (let i = 0; i <= 5; i++) {
        ll.append(i);
        lld.append(i, position='front');
    }

    arr.forEach(i => {
        lla.append(i);
        llf.append(i, position='front')
    });

    ll.print();
    console.log()
    ll.printBackwards();
    console.log()
    console.log(ll.length);
    console.log()
    console.log(ll.size());

    console.log()

    lld.print();
    console.log()
    lld.printBackwards();
    console.log()
    console.log(lld.length);
    console.log()
    console.log(lld.size());

    console.log()

    lla.print();
    console.log()
    lla.printBackwards();
    console.log()
    console.log(lla.length);
    console.log()
    console.log(lla.size());

    console.log()

    llf.print();
    console.log()
    llf.printBackwards();
    console.log()
    console.log(llf.length);
    console.log()
    console.log(llf.size());

}

main();
