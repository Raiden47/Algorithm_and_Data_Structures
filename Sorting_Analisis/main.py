#################################################################################################################################

# Si richiede di analizzare un particolare algoritmo di ordinamento. L'algoritmo elabora una
# sequenza di n interi distinti scambiando due elementi adiacenti finché la sequenza non viene
# ordinata in ordine crescente. La lunghezza massima della sequenza di input è n < 500.000.
# Per la sequenza di input: 91054, l’algoritmo produce l'output 01459.
# Bisogna determinare quante operazioni di scambio sono necessarie a quest’algoritmo per
# ordinare una determinata sequenza di input.
# Un modo alternativo di vedere è il problema è in termini di “inversioni”: in una sequenza A,
# la coppia (i, j) è un’inversione se i < j e Ai > Aj. Il problema consiste nel trovare il conteggio
# delle inversioni.
# Attenzione: data la lunghezza massima della sequenza (500.000, eseguire l’algoritmo al fine
# di contare le operazioni di scambio richiederebbe troppo tempo: si richiede pertanto di
# implementare una soluzione divide et impera per questo problema).
# Si alleghi al PDF un file editabile riportante l’implementazione in un linguaggio a scelta,
# corredato da almeno tre casi di test oltre quelli di esempio riportati di seguito. Si riporti anche
# l’analisi di complessità.
# INPUT
# L'input contiene diversi casi di test. Ogni test case inizia con una riga che contiene un singolo
# intero n < 500.000 — la lunghezza della sequenza di input. Ciascuna delle seguenti n righe
# contiene un singolo intero 0 ≤ a[i] ≤ 999.999.999. L'immissione termina con una sequenza
# di lunghezza n = 0, che chiaramente non deve essere elaborata.
# OUTPUT
# Per ogni sequenza di input, il programma stampa una singola riga contenente il numero
# minimo di operazioni di scambio necessarie per ordinare la sequenza di input data.
# Sample Input
# 5
# 9
# 1
# 0
# 5
# 4
# 3
# 1
# 2
# 3
# 0
# Sample Output
# 6
# 0

#################################################################################################################################

import random as rnd

def bubble_sort(arr) :
    cont_inv = 0
    for i in range(len(arr) - 1) :
        for j in range(len(arr) - 1 - i) :
            if arr[j] > arr[j+1] :
                cont_inv += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, cont_inv

def init_arr() :
    i = 0
    val = None
    arr=[]
    
    n = int(input())
    #n = rnd.randint(1,500000)
    while i < n :
        val = int(input())
        #val = rnd.randint(0,999999999)
        arr.append(val)
        i += 1
    return arr

def bubble_sort_modified (arr, index, temp_arr) :
    if index >= len(arr):
        temp_arr, inv = bubble_sort(temp_arr)
        print (inv, temp_arr)
        return
    if arr[index] == 0 :
        temp_arr, inv = bubble_sort(temp_arr)
        print (inv, temp_arr)
        return bubble_sort_modified(arr, index + 1, [])
    else :
        temp_arr.append(arr[index])
        return bubble_sort_modified(arr, index + 1, temp_arr)
    

if __name__ == "__main__" :
    temp_arr = []
    arr = init_arr()
    bubble_sort_modified(arr, 0, temp_arr)