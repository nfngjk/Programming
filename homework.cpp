#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iomanip>

#define max_size 52

using namespace std;

class Stack {

    private:

        // declare the object
        int stack[max_size];
        int top;

    public:

        // introduce the member function
        Stack();
        void push(int value);
        int pop();
        string output();

};

Stack::Stack() {

    // initialize the stack
    top = -1;

}

void Stack::push(int value) {

    // check if the stack is full
    if(top >= max_size - 1) {

        cout << "the stack is full" << endl;

        exit(-1);

    }

    // update the stack
    top++;

    stack[top] = value;

}

int Stack::pop() {

    int temp;

    // check if the stack is empty
    if(top < 0) {

        cout << "the stack is empty" << endl;

        return -1;

    }

    temp = stack[top];

    // update the stack
    top--;

    return temp;

}

string Stack::output() {

    // output the element in the stack
    for(int i = top; i >= 0; i--) {

        cout << stack[i] << endl;

    }

}

int main() {

    
    int number_of_data = 5;

    Stack shuffle, deal;

    srand(time(NULL));

    for(int i = 0; i < max_size; i++) {

        shuffle.push(rand() % 13 + 1);

    } 

    for(int i = 0; i < number_of_data; i++) {

        deal.push(shuffle.pop());

    }

    deal.output();

    return 0;

}