#include <iostream>
#include <cstdlib>
#include <time.h>

#define N_MAX 500000

using namespace std;

int gen_rdn();
void bubble_sort(int[], int);
void bubble_merge_sort(int[], int, int);
void merge_sort(int[], int, int);
void merge(int[], int, int, int);
int partition(int, int);
void arr_print(int[], int);
int inv_count(int [], int);

int main()
{
    int n;
    int inv = 0;
    do
    {
        cin >> n;
    } while (n >= N_MAX);

    int a[n];
    int b[n];

    srand(time(NULL));

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        //a[i] = gen_rdn();
        b[i] = a[i];
    }
    
    cout << endl << inv_count(a, n) << endl;
    bubble_sort(a, n);
    cout << inv_count(a, n) << endl;
    bubble_merge_sort(a, 0, n - 1);
    cout << inv_count(a, n) << endl;
    merge_sort(b, 0, n-1);
    cout << inv_count(b, n) << endl;

    

    return 0;
}

int gen_rdn() { return rand() % 51; }

void bubble_sort(int v[], int n){
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1; j++)
            if (v[j] > v[j+1]){
                int t = v[j];
                v[j] = v[j + 1];
                v[j + 1] = t;
            }
}

void bubble_merge_sort(int v[], int p, int n){
    
    if (p < n){
        int q = partition(p,n);
        bubble_merge_sort(v, p, q);
        bubble_merge_sort(v, q + 1, n);
        bool swapped;
        do {
            swapped = false;
            for (int i = p; i < n; i++) {
                if (v[i] > v[i+1]) {
                    swap(v[i], v[i+1]);
                     swapped = true;
                 }
             }
         } while (swapped);
    }
}

void merge_sort(int v[], int p, int n){
    if (p < n)
    {
        int q = partition(p,n);
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
    int l[n1];
    int r[n2];
    for (i = 0; i < n1; i++)
        l[i] = v[p + i];
    for (i = 0; i < n2; i++)
        r[i] = v[q + 1 + i];
    i = 0;
    j = 0;
    for (int k = p; k <= n; k++){
        if (l[i] <= r[j] && i < n1){
            v[k] = l[i];
            i++;
        } else if (r[j] < l[i] && j < n2){
            v[k] = r[j];
            j++;
        }
    }
}

int partition(int p, int n) { return (p + (n - p) / 2); }

void arr_print(int v[], int n){
    for (int i = 0; i < n ; i += 1)
        cout << v[i] << " ";
    cout << endl;
}

int inv_count(int v[], int n){
    int inv = 0;
    for (int i = 0; i < n-1; i++)
        if (v[i] > v[i+1])
            inv++;
    return inv;
}