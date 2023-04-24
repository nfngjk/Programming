#include <iostream>
using namespace std;

class Parent {
public:
    int x;
    Parent(int a = 0) { x = a; }
    Parent(const Parent& p) { x = p.x; cout << "Parent copy constructor called" << endl; }
};

class Child : public Parent {
public:
    int y;
    Child(int a = 0, int b = 0) : Parent(a) { y = b; }
    void display() { cout << "x = " << x << ", y = " << y << endl; }
};

int main() {
    Parent p1(10);
    Parent p2 = p1;   
    Child c1(20, 30);
    Child c2 = c1;   
    p2.x = 100;
    c2.y = 200;
    p2.x = 300;
    
c2.display();
    return 0;
}
