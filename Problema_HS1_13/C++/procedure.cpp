#include "procedure.h"

using namespace std;

static treap_node* find_min(treap_node *root) {
    treap_node *curr = root;
    while (curr && curr->left != nullptr) {
        curr = curr->left;
    }
    return curr;
}

treap_node* create_node(int key) {
    treap_node *node = new treap_node;
    node->key = key;
    node->priority = rand();
    node->left = nullptr;
    node->right = nullptr;
    return node;
}

treap_node* rotate_right(treap_node *y) {
    treap_node *x = y->left;
    treap_node *temp = x->right;
    x->right = y;
    y->left = temp;
    return x;
}

treap_node* rotate_left(treap_node *x) {
    treap_node *y = x->right;
    treap_node *temp = y->left;
    y->left = x;
    x->right = temp;
    return y;
}

treap_node* insert_treap(treap_node *root, int key) {
    if (root == nullptr) {
        return create_node(key);
    }
    if (key < root->key) {
        root->left = insert_treap(root->left, key);
        if (root->left && root->left->priority > root->priority) {
            root = rotate_right(root);
        }
    } else if (key > root->key) {
        root->right = insert_treap(root->right, key);
        if (root->right && root->right->priority > root->priority) {
            root = rotate_left(root);
        }
    }
    return root;
}

treap_node* remove_treap(treap_node *root, int key) {
    if (root == nullptr) {
        return nullptr;
    }
    if (key < root->key) {
        root->left = remove_treap(root->left, key);
    } else if (key > root->key) {
        root->right = remove_treap(root->right, key);
    } else {
        if (root->left == nullptr) {
            treap_node *temp = root->right;
            delete root;
            root = temp;
        } else if (root->right == nullptr) {
            treap_node *temp = root->left;
            delete root;
            root = temp;
        } else {
            if (root->left->priority > root->right->priority) {
                root = rotate_right(root);
                root->right = remove_treap(root->right, key);
            } else {
                root = rotate_left(root);
                root->left = remove_treap(root->left, key);
            }
        }
    }
    return root;
}

bool search_treap(treap_node *root, int key) {
    if (root == nullptr) {
        return false;
    }
    if (root->key == key) {
        return true;
    } else if (key < root->key) {
        return search_treap(root->left, key);
    } else {
        return search_treap(root->right, key);
    }
}

void print_inorder(treap_node *root) {
    if (root == nullptr) return;
    print_inorder(root->left);
    cout << root->key << "(" << root->priority << ") ";
    print_inorder(root->right);
}

void print_preorder(treap_node *root) {
    if (root == nullptr) return;
    cout << root->key << "(" << root->priority << ") ";
    print_preorder(root->left);
    print_preorder(root->right);
}

void print_postorder(treap_node *root) {
    if (root == nullptr) return;
    print_postorder(root->left);
    print_postorder(root->right);
    cout << root->key << "(" << root->priority << ") ";
}
