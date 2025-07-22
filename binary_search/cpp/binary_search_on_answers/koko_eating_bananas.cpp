#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
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
double solve(vector<int>&ivec, int const hourly){
    double counter = 0; 
    for(int i = 0; i < ivec.size(); i++){
        counter += ceil(double(ivec[i]/double(hourly)));
    }
    return counter;
}
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1, high = *max_element(piles.begin(), piles.end());
        while(low <= high){
            int mid = (low + high) / 2; 
            double ans = solve(piles, mid);
            if(ans <=h){
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
	int h; cin >> h;
	Solution sol;
	cout << sol.minEatingSpeed(ivec, h) << endl;
}