#include<iostream>
#include<vector>
#include<math.h>
using namespace std; 


const int nth_root(int const n, int const m){
	int low = 1, high = m; 
	while(low <= high){
		int mid = (low + high) / 2;
		if (pow(mid, n) == m){
			return mid;
		} else if (pow(mid, n) < m){
			low = mid + 1;
		} else{
			high = mid - 1;
		}
	}
	return -1;
}
int main(){
	int n; 
	cin >> n; 
	int m; 
	cin >> m;
	cout << nth_root(n, m)<< endl;
	
}
