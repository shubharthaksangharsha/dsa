#include<iostream>
using namespace std; 

class Node{
    public:
        int data; 
        Node* next; 

        Node(int data){
            this -> data = data; 
            this -> next = NULL; 
        }
};

Node* reverse(Node* head){
    Node* prev = NULL;  
    Node* forward = NULL;
    Node* curr = head;  
    while(curr){
        forward = curr -> next;  
        curr ->  next = prev; 
        prev = curr; 
        curr = forward; 
    }
    return prev; 

}
void print(Node* head){
    Node* temp = head; 
    while (temp){
        cout << temp -> data << "->";
        temp = temp-> next;  
    }
    cout  << endl;
}

Node* populate(){
    Node* head = new Node(-1);
    Node* Main = head; 
    for(int i = 0; i < 10; i++){
        Node* temp = new Node(i); 
        head -> next = temp; 
        head = temp; 
    }
    return Main -> next; 
}
int main(){
    Node* head = populate();
    print(head);
    Node* reverse_head = reverse(head);
    print(reverse_head);
    return 0;
}