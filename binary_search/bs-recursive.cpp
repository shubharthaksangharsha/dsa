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

int f(const vector<int>&ivec, int low, int high, const int target){
	if (low > high){
		return -1;
	}
	int mid = (low + high) / 2; 

	if (ivec[mid] == target){
		return mid;
	} else if(target > ivec[mid]){
		return f(ivec, mid + 1, high, target);
	} else{
		return f(ivec, low, mid - 1, target);
	}
}

int main(){
	int n; 
	cin >> n; 
	vector<int>ivec(n); 
	input(ivec); 
	int target; cin >> target; 
	int res = f(ivec, 0, ivec.size() - 1, target); 
	if (res != -1){
		cout << "Element found at: " << res << " position";
	} else{
		cout << "Element not found";
	}
}
