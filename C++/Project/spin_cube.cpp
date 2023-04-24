#include <cmath>
#include <cstdio>
#include <cstring>
#include <unistd.h>

float A, B, C;

float width = 10;

float calculate_X(int i, int j, int k) {

    return j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) *cos(C) + j * cos(A) * sin(C) + k * sin(A) * sin(C) + i * cos(B) * cos(C);

}

float calculate_Y(int i, int j, int k) {

    return j * cos(A) * cos(C) + k * sin(A) * cos(C) - j * sin(A) * sin(B) * sin(C) + k * cos(A) * sin(B) * sin(C) - i * cos(B) * sin(C);

}

float calculate_Z(int i, int j, int k) {

    return k * cos(A) * cos(B) - j * sin(A) * cos(B) + i * sin(B);

}

int main() {

    printf("\x1b[2J");

    while(true) {


    }

    return 0;
}