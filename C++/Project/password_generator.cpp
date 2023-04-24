#include <iostream>
#include <conio.h>
#include <direct.h>
#include <windows.h>
#include <ctime>
#include <iomanip>

using namespace std;

HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
COORD CursorPosition;

void goto_xy(int x, int y) {

    CursorPosition.X = x;
    CursorPosition.Y = y;

}

void setcursor(bool visible, DWORD size) {

    if(size == 0) {

        size = 20;

    }

    CONSOLE_CURSOR_INFO cursor;

    cursor.bVisible = visible;
    cursor.dwSize = size;

    SetConsoleCursorInfo(console, &cursor);

}

void draw_boarder(int x = 0, int y = 0) {

    char vertical = 186;
    char horizon = 205;
    char top_right = 187;
    char top_left = 188;
    char bottom_right = 201;
    char bottom_left = 200;

    int width = 24, height = 4;

    goto_xy(x + 4, y);
    cout << "Generated Password";

    for(int i = 1; i <= height; i++) {

        for(int j = 1; j <= width; j++) {

            goto_xy(j + x, i + y);

            if(i == 1 && j == 1) {

                cout << top_left;

            }

            else if(i == height && j == 1) {

                cout << bottom_left;

            }

            else if(i == 1 && j == width) {

                cout << top_right;

            }

            else if(i == height && j == width) {

                cout << bottom_right;

            }

            else if(i == 1 || i == height) {

                cout << horizon;

            }

            else if(j == 1 || j == width) {

                cout << vertical;

            }

        }

    }

}

int main() {

    srand((unsigned)time(NULL));

    setcursor(0, 0);

    system("cls");

    int complexity;
    int length;

    char operation;

    while(operation = 'y' || operation == 'Y') {

        while(complexity < 1 || complexity > 3) {
            cout << "1 - Weak" << setw(6) << "|" << setw(6) << "2 - Average" << setw(6) << "|" << setw(6) << "3 - Strong" << endl;
            cout << endl;
            cout << "select complexity (1 ~ 3): ";

            cin >> complexity;

            if(complexity < 1 || complexity > 3) {

                cout << "Invalid input" << endl;

            }

        }

    }

    switch(complexity) {

        case 1:

            length = 8;

        case 2:

            length = 16;

        case 3:

            length = 24;

    }

    char password[25] = "";

    for(int i = 0; i < length; i++) {

        if(complexity == 1) {

            password[i] = 33 + rand() % 94;

        }

        else if(complexity == 2) {

            password[i] = 33 + rand() % 94;

        }

        else if(complexity == 3) {

            password[i] = 33 + rand() % 94;

        }

        password[i] = '\0';

        cout << "Generating password..." << endl;

        for(int i = 0; i < 10; i++) {

            cout << (char)176;

            Sleep(200);

        }

        system("cls");

        draw_boarder(8, 5);

        goto_xy(11, 8);
        cout << password;

        goto_xy(10, 15);
        cout << "do you want to generate password again?: ";
        
        operation = getch();

    }

    return 0;
    
}