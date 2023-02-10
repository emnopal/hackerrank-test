#include <iostream>

enum options {
    pre,
    in,
    post
};

options Options(std::string str) {
    if (str == "pre") return pre;
    if (str == "in") return in;
    if (str == "pre") return post;
    return pre;
}

class Node
{
public:
    int data;
    Node *left;
    Node *right;

    Node(int data)
    {
        this->data = data;
        this->left = nullptr;
        this->right = nullptr;
    }

    void insert(int data)
    {
        if (this->data == data)
        {
            return;
        }
        if (data < this->data)
        {
            if (this->left)
            {
                this->left->insert(data);
            }
            else
            {
                this->left = new Node(data);
            }
        }
        if (this->right)
        {
            this->right->insert(data);
        }
        else
        {
            this->right = new Node(data);
        }
    }

    bool find(int data)
    {
        if (this->data == data)
        {
            return true;
        }
        if (data < this->data)
        {
            if (this->left)
            {
                return this->left->find(data);
            }
            return false;
        }
        if (this->right)
        {
            return this->right->find(data);
        }
        return false;
    }

    void show(std::string position) {
        if (this) {
            switch (Options(position))
            {
            case pre:
                std::cout << this->data << std::endl;
                if (this->left) {
                    this->left->show(position);
                }
                if (this->right) {
                    this->right->show(position);
                }
                return;
            case in:
                if (this->left) {
                    this->left->show(position);
                }
                std::cout << this->data << std::endl;
                if (this->right) {
                    this->right->show(position);
                }
                return;
            case post:
                if (this->left) {
                    this->left->show(position);
                }
                if (this->right) {
                    this->right->show(position);
                }
                std::cout << this->data << std::endl;
                return;
            default:
                std::cout << this->data << std::endl;
                if (this->left) {
                    this->left->show(position);
                }
                if (this->right) {
                    this->right->show(position);
                }
                return;
            }
        }
    }

};

class Tree
{
    private:
        Node* root;
    public:
        Tree() {
            this->root = nullptr;
        }

        Tree* insert(int data) {
            if (this->root) {
                this->root->insert(data);
            } else {
                this->root = new Node(data);
            }
            return this;
        }

        bool find(int data) {
            if (this->root) {
                this->root->find(data);
            }
            return false;
        }

        void show(std::string position) {
            std::cout << position << ": " << std::endl;
            if (this->root) {
                this->root->show(position);
            }
            std::cout << std::endl;
        }
};

int main() {

    Tree *tree;
    int arr[] = {10, 12, 5, 4, 20, 8, 7, 15, 13};

    for(auto i : arr) {
        tree->insert(i);
    }

    std::string find1 = tree->find(1) ? "true" : "false";
    std::string find12 = tree->find(12) ? "true" : "false";


    std::cout << find1 << std::endl;
    std::cout << find12 << std::endl;

    std::cout << std::endl;

    tree->show("pre");
    tree->show("in");
    tree->show("post");

    return 0;
}
