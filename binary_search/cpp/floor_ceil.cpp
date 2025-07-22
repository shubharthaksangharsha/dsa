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

int get_ceil(int arr[], int n, int x){
	//arr[mid] >= target 
	int ans = n; 
	int low = 0, high = n - 1; 
	while(low <= high){
		int mid = (low + high)/2; 
		if (arr[mid] >= x){
			ans = arr[mid]; 
			high = mid -1 ; 
		} else{
			low = mid + 1; 
		}
	}
	return ans; 
}

int get_floor(int arr[], int n, int x){
	//arr[mid] >= target 
	int ans = n; 
	int low = 0, high = n - 1; 
	while(low <= high){
		int mid = (low + high)/2; 
		if (arr[mid] <= x){
			ans = arr[mid]; 
			low = mid + 1;
		} else{
			high = mid - 1; 
		}
	}
	return ans; 
}

pair<int, int> getFloorAndCeil(int arr[], int n, int x) {
	int ans1 = get_ceil(arr, n, x); 
	int ans2 = get_floor(arr, n, x);
    pair<int, int>myans = {ans1, ans2}; 
	return myans;
}


int main(){
	int n; 
	cin >> n; 
	vector<int>ivec(n); 
	input(ivec); 
	pair<int, int>myans = getFloorAndCeil(ivec);
	cout << myans.first << " " << myans.second << endl;
}
