#include <iostream>
#include <iomanip>

#define max_Row 100
#define max_Column 100

bool dead = 0;
bool alive = 1;

int map[max_Row][max_Column];
int new_map[max_Row][max_Column];
int Generation;

// initialization
void init() {

    int Row, Column;

    // initial map status
    for(Row = 0; Row < max_Row; Row++) {

        for(Column = 0; Column < max_Column; Column++) {

            map[Row][Column] = dead;

        }

    }

    std::cout << "Game of life" << std::endl;
    std::cout << "Enter (x, y), where (x, y) is a living cell" << std::endl;
    std::cout << "0 <= x <= " << max_Row - 1 << ", 0 <= y <= " << max_Column - 1 << std::endl;
    std::cout << "Terminate with (x, y) = (-1, -1)";

    while(Row != -1 || Column != -1) {

        std::cout << "\n" << "Please enter the coordinate: ";

        std::cin >> Row;
        std::cin >> Column;

        while(getchar() != '\n') {

            continue;

        }

        if(0 <= Row && Row < max_Row && 0 <= Column && Column < max_Column) {

            map[Row][Column] = alive;

        }

        else {

            std::cout << "(x, y) exceeds map range" << std::endl;

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

            count = count + 1;

    }

    // adjust the amount of neighbors
    if(map[row][column] == alive) {

        count = count - 1;

    }

    return count;
    
}

// show the status of cells
void output_map() {

    std::cout << "\n\n" << std::setw(0) << ' ' << "Game of life cell stutus" << std::endl;
    std::cout << std::setw(20) << ' ' << "------Generation " << ++Generation << "------" << std::endl;

    for(int i = 0; i < max_Row; i++) {

        std::cout << "\n" << std::setw(20) << ' ';

        for(int j = 0; j < max_Column; j++) {

            if(map[i][j] == alive) {

                putchar('@');
            }

            else {

                putchar('-');
            }

        }

    }

}

void copy_map() {

    for(int i = 0; i < max_Row; i++) {

        for(int j = 0; j < max_Column; j++) {

            map[i][j] = new_map[i][j];

        }
        
    }

}

int main() {

    int row, column;
    char answer;

    init();
    output_map();

    do {

        for(row = 0; row < max_Row; row++) {

            for(column = 0; column < max_Column; column++) {

                switch (neighbors(row, column)) {
                
                    case 0:
                    case 1:
                    case 4:
                    case 5:
                    case 6:
                    case 7:
                    case 8:

                        new_map[row][column] = dead;

                        break;

                    case 2:

                        new_map[row][column] = map[row][column];

                        break;

                    case 3:

                        new_map[row][column] = alive;

                        break;
                    
                }

            }

        }

        copy_map();

        do {

            std::cout << "\nContinue next Generation (Y/N)?";

            answer = toupper(getchar());

            while(getchar() != 'n' || getchar() != 'N') {

                continue;

            }

            if(answer == 'y' || answer == 'Y') {

                output_map();

            }

        }

        while(alive);

    }

    while(answer == 'y' || answer == 'Y');

    std::cout << std::endl;

    return 0;

}