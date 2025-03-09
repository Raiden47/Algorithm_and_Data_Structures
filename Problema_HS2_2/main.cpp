#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

void backtrack(int row, int n, vector<bool> &col, vector<bool> &d1, vector<bool> &d2, int &count) {
    if (row == n) {
        count++;
        return;
    }
    for (int c = 0; c < n; c++) {
        if (!col[c] && !d1[row - c + (n - 1)] && !d2[row + c]) {
            col[c] = true;
            d1[row - c + (n - 1)] = true;
            d2[row + c] = true;

            backtrack(row + 1, n, col, d1, d2, count);

            col[c] = false;
            d1[row - c + (n - 1)] = false;
            d2[row + c] = false;
        }
    }
}

int countNQueens(int n) {
    if (n <= 0) return 0;
    vector<bool> col(n, false);
    vector<bool> d1(2*n - 1, false);
    vector<bool> d2(2*n - 1, false);
    int count = 0;
    backtrack(0, n, col, d1, d2, count);
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        string line;
        if (!getline(cin, line)) break;
        if (line.empty()) continue;

        int n;
        {
            // Converte la riga in intero
            stringstream ss(line);
            ss >> n;
            if (!ss) continue; // Se non è un intero valido, saltiamo
        }

        int ways = countNQueens(n);
        cout << ways << "\n";
    }
    return 0;
}
