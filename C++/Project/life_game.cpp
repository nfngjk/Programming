#include <iostream>
#include <iomanip>

#define max_Row 10
#define max_Column 25

using namespace std;

bool dead = 0;
bool alive = 1;

int map[max_Row][max_Column];
int new_map[max_Row][max_Column];

void init() {

    int Row, Column;

    // initial map status
    for(Row = 0; Row < max_Row; Row++) {

        for(Column = 0; Column < max_Column; Column++) {

            map[Row][Column] = dead;

        }

    }

    cout << "Game of life" << endl;
    cout << "Enter (x, y), where (x, y) is a living cell" << endl;
    cout << "0 <= x <= " << max_Row - 1 << ", 0 <= y <= " << max_Column - 1 << endl;
    cout << "Terminate with (x, y) = (-1, -1)";

    while(Row != -1 || Column != -1) {

        cout << "Please enter the coordinate: ";

        cin >> Row;
        cin >> Column;

        while(getchar() != "\n") {

            continue;

        }

        if(0 <= Row && Row < max_Row && 0 <= Column && Column < max_Column) {

            map[Row][Column] = alive;

        }

        else {

            cout << "(x, y) exceeds map range" << endl;

        }

    }

}

int neighbors(int Row, int Column) {

    int count = 0;
    int row;
    int column;
        
    for(row = Row - 1; row <= Row + 1; row++) {

        for(column = Column - 1; column <= Column + 1; column++) {

            if(row < 0 || row >= max_Row || column < 0 || column >= max_Column) {

                continue;

            }

        }

    }

    if(map[row][column] == alive) {

            count++;

    }

    return count;
    
}
