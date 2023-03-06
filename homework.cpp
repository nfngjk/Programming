#include <iostream>
#include <cstdlib>
#include <ctime>

#define max_size 10

using namespace std;

class Stack {

    private:

        // declare the object
        int stack[max_size];
        int top;

    public:

        // declare the constructor and the member function in the class Stack
        Stack();

        void push(int value);
        int pop();
        void output();

};

Stack::Stack() {

    // initialize the element in the stack
    top = -1;

}

void Stack::push(int value) {

    // check if the stack is full
    if(top > max_size - 1) {

        cout << "Stack is full" << endl;

        exit(-1);

    }

    top++;

    // update the stack
    stack[top] = value;
    
}

int Stack::pop() {

    int temp;

    // check if the stack is empty
    if(top < 0) {

        cout << "Stack is empty" << endl;

    }

    temp = stack[top];

    top--;

    return temp;

}

void Stack::output() {

    for(int i = top; i >= 0; i--) {

        // output the element in stack
        cout << "[ " << stack[i] << " ]" << endl;

    }

}

int main() {

    int number_of_data = 5;
    Stack stack;

    srand(time(NULL));

    for(int i = 0; i < number_of_data; i++) {

        // add the number into stack randomly
        stack.push(rand() % 13 + 1);

    }

    return 0;

}