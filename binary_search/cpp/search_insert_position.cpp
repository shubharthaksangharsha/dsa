#include<iostream>
#include<vector>
using namespace std; 

class Solution {
public:
    int searchInsert(vector<int>& ivec, int target) {
        	int low = 0, high = ivec.size() - 1; 
            int ans = ivec.size(); 
            while(low <= high){
                int mid = (low + high) / 2; 
                if(ivec[mid] >= target){
                    ans = mid; 
                    high = mid - 1;
                } else{ 
                    low = mid + 1;
                }
            }
            return ans;

    }
};

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
	Solution sol; 
	cout << sol.searchInsert(ivec, target) << endl;
}
