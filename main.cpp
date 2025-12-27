#include "DLL.h"
#include <iostream>
using namespace std;

int main() {
    // A. SETUP: Create the initial browser history
    cout << "=== 1. POPULATING HISTORY ===" << endl;
    Node* head = new Node("Home (Start Page)");
    Node* current = head; // The browser's current view pointer

    // Simulate user browsing 5 pages
    visitPage(current, "www.google.com");
    visitPage(current, "www.youtube.com");
    visitPage(current, "www.github.com");
    visitPage(current, "stackoverflow.com");
    visitPage(current, "chatgpt.com");
    
    cout << "\n[Current Page]: " << current->url << endl;
    cout << "------------------------------------------------" << endl;

    // B. SIMULATION: Go Back (Iterative)
    cout << "\n=== 2. TEST: Go Back 3 Steps (Iterative) ===" << endl;
    cout << "Action: User clicks Back button 3 times..." << endl;
    
    current = goBackIterative(current, 3);
    
    cout << "Expected: www.youtube.com" << endl;
    cout << "Actual:   " << current->url << endl;

    // C. SIMULATION: Go Forward (Recursive)
    cout << "\n=== 3. TEST: Go Forward 2 Steps (Recursive) ===" << endl;
    cout << "Action: User clicks Forward button 2 times..." << endl;
    
    current = goForwardRecursive(current, 2);
    
    cout << "Expected: stackoverflow.com" << endl;
    cout << "Actual:   " << current->url << endl;

    // D. SIMULATION: Boundary Check (Go Back too far)
    cout << "\n=== 4. TEST: Boundary Check (Go Back 100 Steps) ===" << endl;
    cout << "Action: User holds Back button..." << endl;
    
    // Using Recursive Back for this test
    current = goBackRecursive(current, 100);
    
    cout << "Expected: Home (Start Page)" << endl;
    cout << "Actual:   " << current->url << endl;

    // E. SIMULATION: Boundary Check (Go Forward too far)
    cout << "\n=== 5. TEST: Boundary Check (Go Forward 100 Steps) ===" << endl;
    cout << "Action: User holds Forward button..." << endl;
    
    // Using Iterative Forward for this test
    current = goForwardIterative(current, 100);
    
    cout << "Expected: chatgpt.com (Last visited page)" << endl;
    cout << "Actual:   " << current->url << endl;

    cout << "\n=== Simulation Complete ===" << endl;

    return 0;
}