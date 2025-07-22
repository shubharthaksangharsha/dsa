#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string getLargestNumber(string num) {
    int n = num.length();
    
    for (int i = 0; i < n; i++) {
        // Try to find the largest digit with same parity that can be brought to current position
        for (int j = i + 1; j < n; j++) {
            // Check if we can swap from j to i
            bool canSwap = ((num[j] - '0') % 2 == (num[i] - '0') % 2);
            
            // Check if all intermediate numbers have the same parity
            if (canSwap) {
                for (int k = j - 1; k >= i; k--) {
                    if ((num[k] - '0') % 2 != (num[j] - '0') % 2) {
                        canSwap = false;
                        break;
                    }
                }
            }
            
            // If we can swap and the digit at j is larger, perform the swaps
            if (canSwap && num[j] > num[i]) {
                // Bubble the larger digit up to position i
                for (int k = j; k > i; k--) {
                    swap(num[k], num[k-1]);
                }
                break;  // Found and placed the best digit for position i
            }
        }
    }
    
    return num;
}
int main() {
    string input = "1806579";
    cout << "Largest possible number: " << getLargestNumber(input) << endl;

    // Additional test cases
    cout << "Test Case 1: " << getLargestNumber("0082663") << endl; // Expected: "8606322"
    cout << "Test Case 2: " << getLargestNumber("7596801") << endl; // Expected: "9758601"
    return 0;
}
