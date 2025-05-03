#################################################################################################################################

# Dato un insieme di stringhe, si implementi un algoritmo divide et impera per trovare il
# prefisso in comune più lungo.
# Si alleghi al PDF un file editabile riportante l’implementazione in un linguaggio a scelta,
# corredato da almeno tre casi di test oltre quello di esempio riportato di seguito. Si riporti
# anche l’analisi di complessità.
# INPUT
# L'input contiene diversi casi di test. Ogni test case inizia con una riga che contiene un singolo
# intero n, il numero di casi di test. Ciascuna delle seguenti n righe contiene una singola
# stringa.
# OUTPUT
# Per ogni sequenza di input, il programma stampa una singola riga contenente il prefisso
# comune più lungo.
# Sample Input
# 1
# apple
# ape
# april
# applied
# Sample Output
# ap

#################################################################################################################################

def input_manager() :
    in_seq = []
    x = " "
    while x != "" :
        x = input()
        if x != "" :
            in_seq.append(x)
    return in_seq

def max_common_prefix (arr) :
    if not arr :
        return ""
    if len(arr) <= 1 :
        return arr[0]
    
    mid_arr = len(arr) // 2
    left_arr = max_common_prefix(arr[:mid_arr])
    right_arr = max_common_prefix(arr[mid_arr:])
    
    return search_prefix(left_arr, right_arr)

def search_prefix(left_arr, right_arr) :
    min_len = min(len(left_arr), len(right_arr))
    i = 0
    while i < min_len and left_arr[i] == right_arr[i] :
        i += 1
    return left_arr[:i]

if __name__ == "__main__" :
    i = 0
    while True :
        in_seq = input_manager()
        print(in_seq)
        if i == 0 :
            n_test = int(in_seq[0])
            arr_test = in_seq[1:]
        else :
            arr_test = in_seq
        print(f"Max Common Prefix : {max_common_prefix(arr_test)}")
        i += 1
        if i >= n_test : 
            break
    