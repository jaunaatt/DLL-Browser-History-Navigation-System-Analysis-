#include "DLL.h"
using namespace std;

Node* goBackIterative(Node* current, int steps) {
    while (steps > 0 && current != nullptr && current->prev != nullptr) {
        current = current->prev;
        steps--;
    }
    return current;
}

Node* goBackRecursive(Node* current, int steps) {
    if (steps == 0) return current;
    
    if (current == nullptr || current->prev == nullptr) return current;

    return goBackRecursive(current->prev, steps - 1);
}

Node* goForwardIterative(Node* current, int steps) {
    while (steps > 0 && current != nullptr && current->next != nullptr) {
        current = current->next;
        steps--;
    }
    return current;
}

Node* goForwardRecursive(Node* current, int steps) {
    if (steps == 0) return current;

    if (current == nullptr || current->next == nullptr) return current;

    return goForwardRecursive(current->next, steps - 1);
}

void visitPage(Node*& current, string newUrl) {
    Node* newNode = new Node(newUrl);
    
    if (current != nullptr) {
        current->next = newNode;
        newNode->prev = current;
    }
    
    current = newNode;
    cout << "Visited: " << current->url << endl;
}