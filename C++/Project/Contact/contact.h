class Contact {

    private:

        Node* head; 

    protected:

        void Add() {


        }

        void Delete() {


        }

        void Print() {


        }

    public:

        Contact()

        void Menu(char function) {

            switch(function) {

                case 'L':

                    Load();

                case 'A':

                    Add();

                case 'P':

                    Print();

                case 'E':

                    Edit();

                case 'D':

                    Delete();

                case 'R':

                    Remove():

                case 'C':

                    Clear();

            }

        }

        ~Contact()
};