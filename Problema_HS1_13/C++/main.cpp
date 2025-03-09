#include "procedure.h"

using namespace std;

int main() {
    srand(time(nullptr));
    treap_node *root = nullptr;
    int choice;
    do {
        cout << "\n--- MENU ---\n";
        cout << "1) Inserire un elemento\n";
        cout << "2) Rimuovere un elemento\n";
        cout << "3) Cercare un elemento\n";
        cout << "4) Stampare l'albero\n";
        cout << "5) Uscire\n";
        cout << "Scelta: ";
        cin >> choice;
        switch (choice) {
            case 1: {
                cout << "Inserisci la chiave: ";
                int key;
                cin >> key;
                root = insert_treap(root, key);
                break;
            }
            case 2: {
                cout << "Inserisci la chiave: ";
                int key;
                cin >> key;
                root = remove_treap(root, key);
                break;
            }
            case 3: {
                cout << "Inserisci la chiave: ";
                int key;
                cin >> key;
                bool found = search_treap(root, key);
                if (found) {
                    cout << "Chiave presente.\n";
                } else {
                    cout << "Chiave non presente.\n";
                }
                break;
            }
            case 4: {
                cout << "\nInorder:   ";
                print_inorder(root);
                cout << "\nPreorder:  ";
                print_preorder(root);
                cout << "\nPostorder: ";
                print_postorder(root);
                cout << "\n";
                break;
            }
            case 5: {
                cout << "Uscita.\n";
                break;
            }
            default: {
                cout << "Scelta non valida.\n";
                break;
            }
        }
    } while (choice != 5);
    return 0;
}
