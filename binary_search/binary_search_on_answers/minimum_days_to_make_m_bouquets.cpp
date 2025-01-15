#include<iostream>
#include<vector>
#include<algorithm>
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
class Solution {
private:
	int isBloomed(const vector<int>&ivec, int const m, int const k, int const day){
		int counter = 0;
		int ans = 0;
		for(int i = 0; i < ivec.size(); i++){
			if (ivec[i] <= day){
				counter++;
			} else{
				ans += (counter / k);
				counter = 0; 
			}
		}
		ans += counter / k; 
		return ans >= m; 
	}
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
    	long long val = m * 1LL * k * 1LL; 
        if (val > bloomDay.size()){
    		return -1;
    	}
        int low = 1, high = *max_element(bloomDay.begin(), bloomDay.end());
        while (low <= high){
        	int mid = (low + high) / 2;
        	if  (isBloomed(bloomDay, m, k, mid)){
        		high = mid - 1; 
        	} else{
        		low = mid + 1;
        	}
        }
        return low;
    }
};
int main(){
	int n; 
	cin >> n; 
	vector<int>ivec(n); 
	input(ivec); 
	int m; cin >> m;
	int k; cin >> k;
	Solution sol;
	cout << sol.minDays(ivec, m, k) << endl;

}
