###################################################################################################################################################

# Se inseriamo un insieme di n elementi in un albero di ricerca binario (binary search tree,
# BST) utilizzando TREE-INSERT, l'albero risultante potrebbe essere molto sbilanciato.

# Tuttavia, ci si aspetta che i BST costruiti casualmente siano bilanciati (ossia ha un'altezza
# attesa O(lg n)). Pertanto, se vogliamo costruire un BST con altezza attesa O(lg n) per un
# insieme fisso di elementi, potremmo permutare casualmente gli elementi e quindi inserirli in
# quell'ordine nell'albero.

# Cosa succede se non abbiamo tutti gli elementi a disposizione in una sola volta? Se
# riceviamo gli elementi uno alla volta, possiamo ancora costruire casualmente un albero di
# ricerca binario da essi? Nel seguito è proposta una struttura dati che risponde
# affermativamente a questa domanda. Un treap è un albero binario di ricerca che usa una
# strategia diversa per ordinare i nodi. Ogni elemento x nell'albero ha una chiave key[x].
# Inoltre, assegniamo priority[x], che è un numero casuale scelto indipendentemente per ogni
# x. Assumiamo che tutte le priorità siano distinte e anche che tutte le chiavi siano distinte. I
# nodi del treap sono ordinati in modo che (1) le chiavi obbediscano alla proprietà del binary
# search tree e (2) le priorità obbediscano alla proprietà min-heap order dell’heap. In altre
# parole:

# • se v è un figlio sinistro di u, allora key[v] < key[u];
# • se v è un figlio destro di u, allora key[v] > key[u]; e
# • se v è un figlio di u, allora priority(v) > priority(u).
# (Questa combinazione di proprietà è il motivo per cui l'albero è chiamato "treap": ha
# caratteristiche sia di un albero di ricerca binario che di un heap)

# È utile pensare ai treaps in questo modo: supponiamo di inserire i nodi x1, x2, …xn, ciascuno
# con una chiave associata, in un treap in ordine arbitrario. Quindi il treap risultante è l'albero
# che si sarebbe formato se i nodi fossero stati inseriti in un normale albero binario di ricerca
# nell'ordine dato dalle loro priorità (scelte casualmente). In altre parole, priority[xi] < priority[xj]
# significa che xi è effettivamente inserito prima di xj.

# Per inserire un nuovo nodo x in un treap esistente, si assegna dapprima ad x una priorità
# casuale priority[x]. Quindi si chiama l'algoritmo di inserimento, che chiameremo TREAPINSERT,
# il cui funzionamento è illustrato nella Figura 1.

# Quesito. Fornire il codice della procedura TREAP-INSERT in un linguaggio a scelta,
# allegando un file editabile. Suggerimento: effettuare il consueto inserimento del BST, ed
# eseguire le rotazioni per ripristinare la proprietà del min-heap (min-heap order)). 

###################################################################################################################################################

import random as rnd

class treap_node :
    def __init__ (self, key, priority = None):
        self.key = key
        self.priority = priority if priority is not None else rnd.randint(1, 100)
        self.left = None
        self.right = None
        
    def __repr__(self):
        return f"key : {self.key} , priority : {self.priority}"
    
def rotate_left (x) :
    y = x.right
    x.right = y.left
    y.right = x
    return y
    
def rotate_right (y) :
    x = y.left
    y.left = x.right
    x.right = y
    return x
        
        
    
class treap :
    def __init__ (self) :
        self.root = None
        
    def _insert(self, node, key, priority=None) :
        if node is None :
            return treap_node(key, priority)
        
        if key < node.key :
            node.left = self._insert(node.left, key, priority)
            if node.left and node.left.priority > node.priority :
                node = rotate_right(node)
        elif key > node.key :
            node.right = self._insert(node.right, key, priority)
            if node.right and node.right.priority > node.priority :
                node = rotate_left(node)
        return node
    
    def insert(self, key, priority=None) :
        self.root = self._insert(self.root, key, priority)
        
    def _search(self, node, key) :
        if node is None or node.key == key :
            return node
        if key < node.key :
            return self._search(node.left, key)
        else :
            return self._search(node.right, key)
        
    def search(self, key) :
        return self._search(self.root, key)
        
    def _delete(self, node, key) :
        if node is None :
            return None
        if key < node.key :
            node.left = self._delete(node.left, key)
        elif key > node.key :
            node.right = self._delete(node.right, key)
        else :
            if node.left is None :
                return node.right
            elif node.right is None :
                return node.left
            else :
                if node.left.priority > node.right.priority :
                    node = rotate_right(node)
                    node.right = self._delete(node.right, key)
                else :
                    node = rotate_left(node)
                    node.left = self._delete(node.left, key)
        return node
    
    def delete(self, key) :
        self.root = self._delete(self.root, key)
        
    def _inorder(self, node) :
        if node :
            yield from self._inorder(node.left)
            yield node
            yield from self._inorder(node.right)
            
    def inorder(self) :
        return list(self._inorder(self.root))
    
    
if __name__ == "__main__":
    tr = treap()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        tr.insert(v)

    print("Inorder traversal (chiavi ordinate):")
    print(tr.inorder())

    key_to_search = 40
    found = tr.search(key_to_search)
    print(f"\nRisultato ricerca per chiave {key_to_search}: {found}")