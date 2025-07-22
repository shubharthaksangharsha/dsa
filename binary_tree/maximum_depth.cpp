/*
maximum height can be evaluated by 
using 
1 + max(left, right)
where 1: current node 
left: left tree 
right: right tree 
*/
#include <iostream>
#include <vector>
#include<queue>
using namespace std;

class Node{
public:
	int data; 
	Node* left; 
	Node* right; 
	Node(){
		this->data = 0;
		this->left = nullptr;
		this->right = nullptr;
	}
	Node(int data){
		this -> data = data; 
		this->left = nullptr;
		this->right = nullptr;
	}
	Node(int data, Node *left, Node *right){
		this->data = data; 
		this->left = left; 
		this->right = right;
	}
};


int main() {
    Node* root = new Node(3);
    root ->left = new Node(9);
    root ->right = new Node(20, new Node(15), new Node(7));

    cout << root -> data << endl; 
    cout << root -> left -> data << " "; 
    cout << root -> right -> data << endl;
    cout << root -> right -> left -> data << " "; 
    cout << root -> right -> right -> data << " "; 
    

    return 0;
}
    