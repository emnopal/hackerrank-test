#include <iostream>
#include <string>

class Node {
public:
    int data;
    Node* next;
    Node(int data){
        this->data = data;
        this->next = nullptr;
    }
};

class LinkedList {
private:
    Node* head;
public:
    int length;

    LinkedList() {
        head = nullptr;
        length = 0;
    }

    void append(int data, std::string position = "end") {
        Node* newNode = new Node(data);

        if (position == "front") {
            newNode->next = head;
            head = newNode;
            length++;
            return;
        }

        if (!head) {
            head = newNode;
            length++;
            return;
        }

        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
        length++;
        return;

    }

    Node *reverse() {
        Node *reverseLL = nullptr, *next_node, *temp = head;
        while(temp != nullptr) {
            next_node = temp->next;
            temp->next = reverseLL;
            reverseLL = temp;
            temp = next_node;
        }
        return reverseLL;
    }

    void print() {
        Node* temp = head;
        while (temp != nullptr) {
            std::cout << temp->data << " ";
            temp = temp->next;
        }
    }

    void reversePrint() {
        Node* temp = reverse();
        while (temp != nullptr) {
            std::cout << temp->data << " ";
            temp = temp->next;
        }
    }

    int size() {
        return length;
    }

};

int main() {
    LinkedList ll, lld, lla, llf;
    int arr[] = {6,4,3,1,10,8,9,12,0};

    for(int i = 0; i <= 10; i++) {
        ll.append(i);
        lld.append(i, "front");
    }

    for(auto i: arr) {
        lla.append(i);
        llf.append(i, "front");
    }

    ll.print();
    std::cout << std::endl;
    ll.reversePrint();
    std::cout << std::endl;
    std::cout << ll.length << std::endl;
    std::cout << ll.size() << std::endl;

    std::cout << std::endl;

    lld.print();
    std::cout << std::endl;
    lld.reversePrint();
    std::cout << std::endl;
    std::cout << lld.length << std::endl;
    std::cout << lld.size() << std::endl;

    std::cout << std::endl;

    lla.print();
    std::cout << std::endl;
    lla.reversePrint();
    std::cout << std::endl;
    std::cout << lla.length << std::endl;
    std::cout << lla.size() << std::endl;

    std::cout << std::endl;

    llf.print();
    std::cout << std::endl;
    llf.reversePrint();
    std::cout << std::endl;
    std::cout << llf.length << std::endl;
    std::cout << llf.size() << std::endl;

    return 0;
}
