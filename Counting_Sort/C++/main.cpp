#include <iostream>
#include <cstdlib>
#include <time.h>

using namespace std;

#define K 50
#define DIM 20

void init_array(int[], int);
void print_array(int[], int);
void counting_sort(int[], int[], int);

int main(){
    int a[DIM];
    int b[DIM];

    srand(time(NULL));

    init_array(a, DIM);
    print_array(a, DIM);

    counting_sort(a, b, DIM);
    print_array(b, DIM);
    
    return 0;
}

void init_array ( int a[], int n){
    for (int i = 0; i < n; i++)
        a[i] = rand() % K;
}

void print_array(int a[], int n){
    for (int i = 0; i < n;i++)
        cout << a[i] << " ";
    cout << endl << endl;
}

void counting_sort(int a[], int b[], int n){
    int c[K];
    for (int i = 0; i < K; i++)
        c[i] = 0;

    for (int i = 1; i < n; i++)
        c[a[i]] += 1;

    for (int i = 1; i < K; i++)
        c[i] += c[i - 1];

    for (int i = n-1; i > 0; i--){
        b[c[a[i]]] = a[i];
        c[a[i]] -= 1;
    }
}