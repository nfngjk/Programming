#ifndef _contact_h_

#define _contact_h_

#include <string>
#include <fstream>

using namespace std;

struct Node {

    string name;
    string info;

    Node* next;

    Node(string name = "", string info = "", Node* pointer = NULL) {

        this -> name = name;
        this -> info = info;
        next = pointer;

    }

};

class Contact {

    protected:

        Node *head, *pointer, *temp;
        
        Node* Find(string);

        fstream file_input;
        fstream file_output;

        void Add(string, string);
        void Delete();
        void Print();
        void Load();
        void Save();
        void Clear();

    public:

        Contact();
        ~Contact();
        
        void Menu();
        
};

#endif