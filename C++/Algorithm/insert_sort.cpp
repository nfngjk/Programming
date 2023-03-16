#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <ctime>

using namespace std;

struct Node {
	
	int value;
	Node* next;
	
	Node(int v = 999, Node* n = NULL) {
		
		value = v;
		next = n;
		
	}
	
};

void output(Node* head) {
	
	for (Node* pointer = head -> next; pointer; pointer = pointer -> next) {
		
		cout << "->" <<  setw(3) << pointer -> value;
		
	}
	
}			

int main() {
	
	int n;
	
	cin >> n;
	
	int number = 0;
	
	Node *head = new Node(-1);
	Node *pointer = 0, *temp = 0;
	
	srand(time(NULL));
	
	for(int i = 0; i < n; i++) {
		
		int number = rand() % 100;
		
		Node *temp = new Node(number);
		
		for(pointer = head; pointer -> next != NULL; pointer = pointer -> next) {
			
			if(pointer -> next -> value > number) {
				
				break;
				
			}
			
		}
		
		temp -> next = pointer -> next;
		
		pointer -> next = temp;
		
	}
	
	output(head);
	
	cout << endl << "Delete a number: ";
	
	cin >> number;
	
	for(pointer = head; pointer -> next; pointer = pointer -> next) {
			
		if(pointer -> next -> value == number) {
			
			temp = pointer -> next;
			
			pointer -> next = temp -> next;
			
			delete temp;	
	
			break;
				
		}
			
	}
	
	output(head);
	
	return 0;
	
}