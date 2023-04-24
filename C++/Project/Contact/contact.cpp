#include "contact.h"
#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <fstream>

using namespace std;

Contact::Contact() {

    head = new Node();

};

Contact::~Contact() {

    for(pointer = head; pointer -> next;) {

        Delete();

    }

    delete head;

}

void Contact::Menu() {

    string name, info;
    string file_name;
    string input;

    cout << "Enter the contact you want to open: ";

    cin >> file_name;
    
    file_input.open(file_name.c_str(), ios::in); 

    if(file_input.is_open()) {
    	
    	while(!file_input.eof()) {
    		
    		file_input >> input;
    		
		}
		
	}
    
    else {

        file_name = file_name + ".txt";

        file_input.open(file_name.c_str(), ios::out);

    }
    
    while(true) {

        cout << "\n===================================" << endl;
        cout << setw(10) << "<1> Add" << endl;
        cout << setw(10) << "<2> Delete" << endl;
        cout << setw(10) << "<3> Print" << endl;
        cout << setw(10) << "<4> Find" << endl;
        cout << setw(10) << "<5> Clear" << endl;
		cout << setw(10) << "<6> Load" << endl;
		cout << setw(10) << "<7> Save" << endl; 
        cout << setw(10) << "<8> Quit" << endl;
        cout << "===================================" << endl;
        
        cout << "Enter your option: ";

        int selection;

        cin >> selection;

        switch(selection) {

            case 1:

                cout << "Enter the name you want to add: ";

                cin >> name;

                file_input >> name;

                cout << "Enter the info you want to add: ";

                cin >> info;
                
                Add(name, info);

                file_input >> info;

                break;

            case 2:

                cout << "Enter the name you want to delete: ";

                cin >> name;

                pointer = Find(name);

                if(pointer -> next -> name == name) {

                    Delete();

                }

                break;

            case 3:

                Print();

                break;

            case 4:

                cout << "Enter the name you want to Find: ";

                cin >> name;

                Find(name);
                
            case 5:
            	
            	Clear();
            	
            	break;
            	
            case 6:
            	
            	Load();
            	
            	break;
            	
            case 7:
            	
            	Save();
            	
            	break;

            case 8:

                cout << "See you next time." << endl;
                
                return ;

            default:

                cout << "Please enter your selection correctly!" << endl;

    	}

	}

void Contact::Add(name, info) {

    pointer = Find(name);

    if(pointer -> name < name) {

        temp = new Node(name);

        temp -> next = pointer -> name;

        pointer -> next = name;
        
    }
}
void Contact::Delete() {

    if(pointer -> next) {

        temp = pointer -> next;
        pointer -> next = temp -> next;
        
        delete temp;

    }

}

void Contact::Print() {

    for(pointer = head -> next; pointer; pointer = pointer -> next) {

        cout << setw(10) << pointer -> name << setw(10) << pointer -> info << endl;

    }

}

Node* Contact::Find(string name) {

    for(temp = head; temp -> next; temp = temp -> next) {

        if(name <= temp -> next -> name) {

            break;

        }

        return temp;

    }

}

void Contact::Load() {

    
}

void Contact::Save() {

    file_output.close();

}

void Contact::Clear() {

    file_output.clear();

}
