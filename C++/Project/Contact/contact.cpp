#include "contact.h"
struct Node {
    
    string name;
    string info;

    Node* next;

    Node(string n, string i, Node* p = NULL) {

        name = n;
        info = i;

        next = p;

    }
    
};

Contact::Contact() {

    head = new Node();

}

Contact::~Contact() {

    for(; head -> next; ) {

        remove(head);

    }

    delete head;

}

void Contact::Add() {


}

void Contact::Delete() {


}

void Contact::Print() {


}

void Contact::Remove() {


}