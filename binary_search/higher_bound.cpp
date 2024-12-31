#include<iostream>
#include<vector>
using namespace std; 

/*
Higher bound: smallest index such that arr[ind] > n
*/
const void input(vector<int>&ivec){
	for(auto &i: ivec){
		cin >> i; 
	}
}

const int f(vector<int>&ivec, int const target){
	int low = 0, high = ivec.size() - 1; 
	int ans = ivec.size(); 
	while(low <= high){
		int mid = (low + high) / 2; 
		if(ivec[mid] > target){
			ans = mid; 
			high = mid - 1;
		} else{ 
			low = mid + 1;
		}
	}
	return ans;

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
	int target; cin >> target;
	cout << f(ivec, target);
}
