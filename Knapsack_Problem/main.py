###################################################################################################################################

# Due ladri mettono a segno un colpo alla banca d’Italia. Recuperano un bottino composto da
# monete d’oro di diverso valore. Devono dividerselo il più equamente possibile, ossia devono
# minimizzare la differenza tra il valore che ciascuno di loro ottiene. Scrivere un algoritmo per
# determinare la suddivisione, stampando in output la differenza (positiva) tra il valore che i
# due ladri ottengono dividendosi il bottino.
# Il bottino contiene al massimo 50 monete, il valore di ciascuna moneta varia da 1 a 1000. Il
# valore di una moneta può occorrere più di una volta.
# INPUT
# La prima riga contiene il numero di casi di test, N. Dopo la prima linea, ogni caso di test è
# composto da 2 linee: la prima riporta un numero intero non negativo M compreso tra 1 e 50,
# che indica il numero di monete; la seconda riporta M numeri interi non negativi compresi tra
# 1 e 1000, separati da uno spazio, che indicano il valore di ciascuna delle M monete.
# OUTPUT
# Per ogni caso di test, l'output deve stampare la differenza (positiva) tra il valore che i due
# ladri ottengono dividendosi il bottino.
# Sample Input
# 3
# 5
# 1 4 7 4 8
# 4
# 5 4 9 1
# 1
# 50
# Sample Output
# 0
# 1
# 50

###################################################################################################################################

def init_val (n_test) :
    if n_test == 0 :
        return 5, [1, 4, 7, 4, 8]
    if n_test == 1 :
        return 4, [5, 4, 9, 1]
    if n_test == 2 :
        return 1, [50]
    return

def merge_sort (arr) :
    if len(arr) <= 1 :
        return arr
    
    mid_arr = int(len(arr) // 2)
    left_arr = merge_sort(arr[:mid_arr])
    right_arr = merge_sort(arr[mid_arr:])
    
    return merge(left_arr, right_arr)

def merge(left_arr, right_arr) :
    result = []
    i = j = 0
    
    while i < len(left_arr) and j < len(right_arr) :
        if left_arr[i] < right_arr[j] :
            result.append(left_arr[i])
            i += 1
        else :
            result.append(right_arr[j])
            j += 1
        
    while i < len(left_arr) :
        result.append(left_arr[i])
        i += 1
        
    while j < len(right_arr) :
        result.append(right_arr[j])
        j += 1
        
    return result

def knapsack_multiple (sack_1, sack_2, arr, index) :
    if index <= 0 :
        return sack_1, sack_2
    
    elem = arr.pop()
    if sum(sack_1) <= sum(sack_2) :
        sack_1.append(elem)
    else : 
        sack_2.append(elem)
    
    return knapsack_multiple(sack_1, sack_2, arr, index - 1)

if __name__ == '__main__' :
    arr = []
    sack_1 = []
    sack_2 = []
    for i in range(3) :
        dim, arr = init_val(i)
        print(arr)
        arr = merge_sort(arr)
        print(arr)
        sack_1, sack_2 = knapsack_multiple(sack_1, sack_2, arr, len(arr))
        print(f"Sack_1 : {sack_1}\nValue_1 : {sum(sack_1)}\n\nSack_2 : {sack_2}\nValue_2 : {sum(sack_2)}\n\nDifferences in value : {abs(sum(sack_1) - sum(sack_2))}\n\n")
        while sack_1 :
            sack_1.pop()
        while sack_2 : 
            sack_2.pop()