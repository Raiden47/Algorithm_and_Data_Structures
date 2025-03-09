#include <stdio.h>
#include <stdlib.h>

#define N_MAX 500000


int swap(int , int );
int bubble_sort(int[], int);
void merge_sort(int[], int, int);
void merge(int[], int, int, int);
int partition(int);
void arr_print(int[], int);

int main()
{
    printf("MAMMT 0 ---------------------------------\n");
    int n;
    int inv = 0;
    do
    {
        scanf("%d", &n);
        printf("MAMMT 1 ---------------------------------\n");
    } while (n >= N_MAX);

    int a[n];
    int b[n];
    for (int i = 0; i < n; i += 1)
    {
        scanf("%d", &a[i]);
        printf("MAMMT 2 ---------------------------------\n");
        b[i] = a[i];
    }

    inv = bubble_sort(a, n);
    arr_print(a, n);
    merge_sort(b, 0, n);
    arr_print(b, n);

    return 0;
}

int swap(int x, int y){
    int t = x;
    x = y;
    y = t;
    return 1;
}

int bubble_sort(int v[], int n){
    int inv = 0;
    for (int i = 0; i < n - 1; i += 1)
        for (int j = 0; j < n - 1; j += 1 )
            if (v[j] > v[j+1])
                inv += swap(v[j], v[j + 1]);
    return inv;
}

void merge_sort(int v[], int p, int n){
    if (p < n){
        int q = partition(n);
        merge_sort(v, p, q);
        merge_sort(v, q + 1, n);
        merge(v, p, q, n);
    }
}

void merge(int v[], int p, int q, int n){
    int i = 0;
    int j = 0;
    int n1 = q - p + 1;
    int n2 = n - q;
    int l[n1 + 1];
    int r[n2 + 1];
    for (i = 0; i < n1; i += 1)
        l[i] = v[p + i - 1];
    for (i = 0; i < n2; i += 1)
        r[i] = v[q + j];
    i = 1;
    j = 1;
    for (int k = p; k < n; k += 1){
        if (l[i] <= r[j]){
            v[k] = l[i];
            i += 1;
        } else {
            v[k] = r[j];
            j += 1;
        }
    }
}

int partition(int n) { return n / 2; }

void arr_print(int v[], int n){
    for (int i = 0; i < n ; i += 1)
        printf("%d ", v[i]);
    printf("\n");
}