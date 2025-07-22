#include<iostream>
#include<queue>
#include<vector>
using namespace std; 

class Node{
public:
	int data; 
	Node* left; 
	Node* right;

	Node(int data){
		this ->data = data; 
		this -> left = nullptr;
		this -> right = nullptr;
	}
};

vector<vector<int>> levelorder(Node* root){
	vector<vector<int>>ans; 
	queue<Node*>q; 
	q.push(root);
	while(!q.empty()){
		int size = q.size();
		vector<int>level;
		for(int i = 0; i < size; i++){
			Node* node = q.front();
			q.pop();
			if(node -> left != NULL){
				q.push(node->left);
			}
			if(node -> right != NULL){
				q.push(node->right);
			}
			level.push_back(node->data);
		}
		ans.push_back(level);
	}
	return ans;
}
void preorder(Node* root){
	if (root == nullptr){
		return;
	}

	cout << root -> data << " "; 
	preorder(root -> left); 
	preorder(root -> right);
}

void inorder(Node* root){
	if (root == nullptr){
		return;
	}

	inorder(root -> left); 
	cout << root -> data << " "; 
	inorder(root -> right);
}

void postorder(Node* root){
	if (root == nullptr){
		return;
	}
	

	postorder(root -> left); 
	postorder(root -> right);
	cout << root-> data << " "; 
}
void print(const vector<vector<int>>ivec){
	cout << endl;
	for(auto i: ivec){
		for(auto j: i){
			cout << j << " ";
		}
		cout << endl;
	}
}
int main(){
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    
    cout << "Preorder Traversal: ";
    preorder(root);
    cout << endl;

    cout << "Inorder Traversal: ";
    inorder(root);
    cout << endl;

    cout << "Postorder Traversal: ";
    postorder(root);
    cout << endl;
    vector<vector<int>>levelOrder = levelorder(root);
    cout << "Level Order:"; 
    print(levelOrder);

}
