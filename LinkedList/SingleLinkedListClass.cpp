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
    LinkedList() {
        head = nullptr;
    }

    void append(int data, std::string position = "end") {
        Node* newNode = new Node(data);

        if (position == "front") {
            newNode->next = head;
            head = newNode;
            return;
        }

        if (!head) {
            head = newNode;
            return;
        }

        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
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

};

int main() {
    LinkedList ll, lld;
    for(int i = 0; i <= 10; i++) {
        ll.append(i);
    }
    ll.print();
    ll.reversePrint();

    std::cout << "\n";

    for(int i = 0; i <= 10; i++) {
        ll.append(i, "front");
    }
    ll.print();
    ll.reversePrint();
    return 0;
}
