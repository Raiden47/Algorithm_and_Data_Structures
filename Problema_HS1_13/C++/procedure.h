#ifndef _PROCEDURE_H_
#define _PROCEDURE_H_

#include <iostream>
#include <cstdlib>
#include <ctime>

struct treap_node {
    int key;
    int priority;
    treap_node *left;
    treap_node *right;
};

treap_node* create_node(int key);
treap_node* rotate_right(treap_node *y);
treap_node* rotate_left(treap_node *x);
treap_node* insert_treap(treap_node *root, int key);
treap_node* remove_treap(treap_node *root, int key);
bool search_treap(treap_node *root, int key);
void print_inorder(treap_node *root);
void print_preorder(treap_node *root);
void print_postorder(treap_node *root);

#endif //_PROCEDURE_H_