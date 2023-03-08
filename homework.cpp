#include <iostream>
#include <cstdlib>
#include <ctime>

// define the stack size
#define max_size 52

using namespace std;

class Stack {

    private:

        // declare the object
        int number_of_data = 5;
        int stack1[max_size], stack2[number_of_data];
        int top;

    public:

        // declare the constructor and the member function in the class Stack
        Stack();

        void push(int value);
        int pop();
        void output();

};

Stack::Stack() {

    // initialize the elements in the stack
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
    stack1[top] = value;
    
}

int Stack::pop() {

    int temp;

    // check if the stack is empty
    if(top < 0) {

        cout << "Stack is empty" << endl;

        return -1;

    }

    temp = stack1[top];

    top--;

    return temp;

}

void Stack::output() {

    for(int i = top; i >= 0; i--) {

        // output the element in stack
        cout << "[ " << stack2[i] << " ]" << endl;

    }

}

int main() {

    int number_of_data = 5;
    Stack stack;

    srand(time(NULL));

    for(int i = 0; i < max_size; i++) {

        // add the number into stack randomly
        stack.push(rand() % 13 + 1);

    }

    for(int i = 0; i < number_of_data; i++) {


    }

    stack.output();

    return 0;

}