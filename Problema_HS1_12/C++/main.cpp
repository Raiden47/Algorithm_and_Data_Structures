#include <iostream>
#include <vector>
#include <string>

using namespace std;

string commonPrefix(const string &, const string &);
string LCP_divideEtImpera(const vector<string> &, int , int );
string longestCommonPrefix(const vector<string> &);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; // Numero di test case
    cin >> t;

    while (t--) {
        int n; // Numero di stringhe per il test case corrente
        cin >> n;

        // Lettura delle stringhe
        vector<string> strs(n);
        for (int i = 0; i < n; i++) {
            cin >> strs[i];
        }

        // Calcolo del LCP
        string result = longestCommonPrefix(strs);

        // Stampa del risultato
        cout << result << "\n";
    }

    return 0;
}

/**
 * Restituisce il prefisso comune tra due stringhe.
 * Esempio: commonPrefix("flower", "flow") = "flow"
 */
string commonPrefix(const string& s1, const string& s2) {
    int minLen = min(s1.size(), s2.size());
    int i = 0;
    while (i < minLen && s1[i] == s2[i]) {
        i++;
    }
    // Ritorna il sottostringa [0, i)
    return s1.substr(0, i);
}

/**
 * Funzione ricorsiva "divide et impera" per calcolare
 * il LCP di un sottoinsieme di stringhe compreso tra gli
 * indici left e right (inclusi).
 */
string LCP_divideEtImpera(const vector<string>& strs, int left, int right) {
    // Caso base: una sola stringa
    if (left == right) {
        return strs[left];
    }
    // Se left < right, dividiamo il vettore in due metà
    int mid = left + (right - left) / 2;
    
    // Calcola ricorsivamente il LCP della parte sinistra
    string lcpLeft = LCP_divideEtImpera(strs, left, mid);
    // Calcola ricorsivamente il LCP della parte destra
    string lcpRight = LCP_divideEtImpera(strs, mid + 1, right);
    
    // "Fonde" (merge) i due risultati trovando il prefisso comune
    return commonPrefix(lcpLeft, lcpRight);
}

/**
 * Calcola il LCP di un intero vettore di stringhe usando il
 * metodo "divide et impera". Se il vettore è vuoto, ritorna stringa vuota.
 */
string longestCommonPrefix(const vector<string>& strs) {
    if (strs.empty()) {
        return "";
    }
    return LCP_divideEtImpera(strs, 0, strs.size() - 1);
}