#include<iostream>
#include<vector>
using namespace std; 

const int f(const vector<int>&ivec, int const target){ 
	int low = 0, high = ivec.size() - 1; 
	while (low <= high){ 
		int mid = (low + high) / 2; 
		if (ivec[mid] == target){
			return mid; 
		} else if(target > ivec[mid]){
			low = mid + 1; 
		} else{ 
			high = mid - 1;
		}
	}
	return -1;
}

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
	int target; cin >> target;
	int res = f(ivec, target);
	if (res != -1){
		cout << "Found element at: " << res << " position";
	} else{
		cout << "Element not found" << endl;
	}
}
