#include<iostream>
#include<vector>
using namespace std; 

const void input(vector<int>&ivec){
	for(auto &i: ivec){
		cin >> i; 
	}
}

const void print(const vector<int>&ivec){
	for(auto const i: ivec){
		cout << i << " ";
	}
	cout << endl; 
}

int main(){
	int n; 
	cin >> n; 
	vector<int>ivec(n); 
	input(ivec); 
	print(ivec); 
}
