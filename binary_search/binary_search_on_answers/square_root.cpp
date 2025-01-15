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

const int square_root(const int n){
	int ans = 1;
	int low = 1; 
	int high = n;
	while(low <= high){
		int mid = (low + high ) / 2;
		if (mid * mid <= n){
			ans = mid; 
			low = mid + 1;
		} else{
			high = mid - 1;
		}
	}
	return ans; 
}
int main(){
	int n; 
	cin >> n; 
	cout << square_root(n) << endl;
}
