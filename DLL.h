#include <iostream>
#include <string>

using namespace std;

struct Node {
    string url;
    Node* prev;
    Node* next;

    // Simple constructor
    Node(string u) {
        url = u;
        prev = nullptr;
        next = nullptr;
    }
};

Node* goBackIterative(Node* current, int steps);
Node* goBackRecursive(Node* current, int steps);
Node* goForwardIterative(Node* current, int steps);
Node* goForwardRecursive(Node* current, int steps);
void visitPage(Node*& current, string newUrl);