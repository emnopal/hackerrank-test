#include <iostream>
#include <string>

struct Node {
    int data;
    Node* next;
};

struct LinkedList {
    Node* head;
    int length;
};

void append(LinkedList *LL, int data, std::string position = "end") {
    Node* newNode = new Node{
        data,
        NULL
    };

    if (position == "front") {
        newNode->next = LL->head;
        LL->head = newNode;
        LL->length++;
        return;
    }

    if (!LL->head) {
        LL->head = newNode;
        LL->length++;
        return;
    }

    Node* temp = LL->head;
    while(temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = newNode;
    LL->length++;

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
        std::cout << temp->data << " ";
        temp = temp->next;
    }
}

void reversePrint(LinkedList *LL) {
    Node* temp = reverse(LL);
    while(temp != nullptr) {
        std::cout << temp->data << " ";
        temp = temp->next;
    }
}

int size(LinkedList *LL) {
    return LL->length;
}

int main(){
    LinkedList *ll = new LinkedList{};
    LinkedList *lld = new LinkedList{};

    for(int i = 0; i <= 10; i++) {
        append(ll, i);
    }
    print(ll);
    reversePrint(ll);
    std::cout << std::endl;
    std::cout << ll->length << std::endl;
    std::cout << size(ll) << std::endl;

    std::cout << "\n";

    for(int i = 0; i <= 10; i++) {
        append(lld, i, "front");
    }
    print(lld);
    reversePrint(lld);
    std::cout << std::endl;
    std::cout << lld->length << std::endl;
    std::cout << size(lld) << std::endl;

    return 0;
}
