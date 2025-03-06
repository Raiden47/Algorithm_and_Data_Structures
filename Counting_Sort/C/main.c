#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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
    for (int i = 0; i < n; i += 1)
        a[i] = rand() % K;
}

void print_array(int a[], int n){
    for (int i = 0; i < n;i++)
        printf("%d ", a[i]);
    printf("\n\n");
}

void counting_sort(int a[], int b[], int n){
    int c[K];
    for (int i = 0; i < K; i+=1)
        c[i] = 0;

    for (int i = 1; i < n; i+=1)
        c[a[i]] += 1;

    for (int i = 1; i < K; i += 1)
        c[i] += c[i - 1];

    for (int i = n-1; i > 0; i-=1){
        b[c[a[i]]] = a[i];
        c[a[i]] -= 1;
    }
}