#include <iostream>
#include <conio.h>
#include <direct.h>
#include <windows.h>
#include <ctime>

#define width 70
#define tower1_position 15
#define tower2_position 30
#define tower3_position 45
#define number_of_disk 5

using namespace std;

HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
COORD CursorPosition;

int towers[3][number_of_disk];
int top[3] = {number_of_disk - 1, -1, -1};

int tries = 0;
int score = 0;

void goto_xy(int x, int y) {

    CursorPosition.X = x;
    CursorPosition.Y = y;
    
    SetConsoleCursorPosition(console, CursorPosition);

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

void update_score() {

    goto_xy(width + 7, 5);

    cout << "Tries: " << tries << endl;

}

void instructions() {

    system("cls");

    cout << "Instructions: " << endl;
    cout << "Shift disks from tower1 to tower3." << endl;
    cout << "You can not place large disk on small disk" << endl;
    cout << "Towers are numbered as 1, 2, and 3" << endl;
    cout << endl;
    cout << "Press any key to go back to menu";

    getch();

}

void draw_tile(int tower, int tile_number, int y) {

    int x;

    switch(tower) {

        case 1:

            x = tower1_position;

        case 2:

            x = tower2_position;

        case 3:

            x = tower3_position;

    }

    x = x- tile_number;

    for(int i = 0; i < (tile_number * 2) - 1; i++) {

        goto_xy(x, y);

        cout << "*";

        x++;

    }

}

void draw_tower(int tower) {

    int x;
    int y = 9;

    goto_xy(10, 10);
    cout << "===============";
    
    goto_xy(25, 10);
    cout << "===============";

    goto_xy(40, 10);
    cout << "===============";

    goto_xy(15, 11);
    cout << "1";

    goto_xy(30, 11);
    cout << "2";

    goto_xy(45, 11);
    cout << "3";

    for(int i = 0; i < number_of_disk; i++) {

        draw_tile(tower, towers[tower - 1][i], y);

        y--;

    }

}

int is_Empty(int tower_number) {

    for(int i = 0; i < number_of_disk; i++) {

        if(towers[tower_number][i] != 0) {

            return 0;

        }

    }

    return 1;

}

int validate(int from, int to) {

    if(!is_Empty((to))) {

        if(towers[from][top[from]] < towers[to][top[to]]) {

            return 1;

        }

        else {

            return 0;

        }

    }

}

int move(int from, int to) {

    if(is_Empty(from)) {

        return 0;

    }

    if(validate(from, to)) {

        if(towers[from][top[from]] != 0) {

            top[to]++;
            towers[to][top[to]] = towers[from][top[from]];
            towers[from][top[from]] = 0;
            top[from]--;

            return 1;

        }

    }

    return 0;

}

int win() {

    for(int i = 0; i < number_of_disk; i++) {

        if(towers[2][i] != number_of_disk - 1) {

            return 0;

        }
    }

    return 1;

}

void play() {

    int from, to;

    for(int i = 0; i < number_of_disk; i++) {

        towers[0][i] = number_of_disk - i;
        towers[1][i] = 0;
        towers[2][i] = 0;

    }

    while(true) {

        system("cls");

        cout << "==========================================" << endl;
        cout << "              Tower of Hanoi              " << endl;
        cout << "==========================================" << endl;

        draw_tower(1);
        draw_tower(2);
        draw_tower(3);

        if(win()) {

            system("cls");

            cout << "==========================================" << endl;
            cout << "                 You win                  " << endl;
            cout << "==========================================" << endl;

            cout << "\n\n\n";

            cout << "Press any key to go back to menu";

            getch();
            
            break;

        }

        goto_xy(10, 15);
        cout << "From: ";
        cin >> from;

        goto_xy(10, 16);
        cout << "To: ";
        cin >> to;

        if(to < 1 || to  > 3) {

            continue;

        }

        if(from < 1 || from > 3) {

            continue;

        }

        if(from == to) {

            continue;

        }

        from--;
        to--;

        move(from, to);

        if(kbhit()) {

            char ch = getch();

            if(ch == 'a' ||ch == 'A') {


            }

            if(ch == 'a' ||ch == 'A') {


            }

            if(ch == 27) {

                break;

            }

        }

    }

}

int main() {

    setcursor(0, 0);

    srand((unsigned)time(NULL));

    while(true) {

        system("cls");

        goto_xy(10, 5);
        cout << "===================================";

        goto_xy(10, 6);
        cout << "|         Tower of Hanoi          |";

        goto_xy(10, 7);
        cout << "===================================";

        goto_xy(10, 9);
        cout << "1. Start Game";

        goto_xy(10, 10);
        cout << "2, Instructions";

        goto_xy(10, 11);
        cout << "3, Quit";

        goto_xy(10, 13);
        cout << "Select option: ";

        char option = getche();

        switch(option) {

            case 1:

                play();

            case 2:

                instructions();

            case 3:

                exit(0);

        }    
        
    }

    return 0;

}