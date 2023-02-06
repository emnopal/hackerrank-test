#include <iostream>

struct Node {
    int data;
    Node* next;
};

struct LinkedList {
    Node* head;
};

void append(LinkedList *LL, int data) {
    Node* newNode = new Node{
        data,
        NULL
    };

    if (!LL->head) {
        LL->head = newNode;
    } else {
        Node* temp = LL->head;
        while(temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

Node *reverse(LinkedList *LL) {
    Node *reverseLL = nullptr, *next_node, *temp = LL->head;
    while(temp != nullptr) {
        next_node = temp->next;
        temp->next = reverseLL;
        reverseLL = temp;
        temp = next_node;
    }
    return reverseLL;
}

void print(LinkedList *LL) {
    Node* temp = LL->head;
    while(temp != nullptr) {
        std::cout << temp->data << std::endl;
        temp = temp->next;
    }
}

void reversePrint(LinkedList *LL) {
    Node* temp = reverse(LL);
    while(temp != nullptr) {
        std::cout << temp->data << std::endl;
        temp = temp->next;
    }
}

int main(){
    LinkedList *ll = new LinkedList{};
    for(int i = 0; i <= 10; i++) {
        append(ll, i);
    }
    print(ll);
    reversePrint(ll);
    return 0;
}
