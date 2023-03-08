#include <iostream>
#include <cstdlib>
#include <ctime>

#define max_size 52

using namespace std;

class Stack {

    private:

        int stack[max_size];
        int top;

    public:

<<<<<<< HEAD
=======
        // introduce the member function
>>>>>>> 54e12c0704221ab7297c955ffb7d729f14468dee
        Stack();
        void push(int value);
        int pop();
        void output();

};

Stack::Stack() {

<<<<<<< HEAD
=======
    // initialize the stack
>>>>>>> 54e12c0704221ab7297c955ffb7d729f14468dee
    top = -1;

}

void Stack::push(int value) {

<<<<<<< HEAD
=======
    // check if the stack is full
>>>>>>> 54e12c0704221ab7297c955ffb7d729f14468dee
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

    if(top < 0) {

        cout << "the stack is empty" << endl;
        return -1;

    }

    temp = stack[top];

    // update the stack
    top--;

    return temp;

}

void Stack::output() {

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