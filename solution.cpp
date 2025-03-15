#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool canPlaceCows(vector<int>& stalls, int k, int minDist) {
    int count = 1; 
    int lastPlaced = stalls[0];

    for (int i = 1; i < stalls.size(); i++) {
        if (stalls[i] - lastPlaced >= minDist) {
            count++; 
            lastPlaced = stalls[i];

            if (count == k) return true; 
        }
    }
    return false; 
}
int aggressiveCows(vector<int>& stalls, int k) {
    sort(stalls.begin(), stalls.end()); 

    int low = 1; 
    int high = stalls.back() - stalls.front(); 
    int result = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (canPlaceCows(stalls, k, mid)) {
            result = mid; 
            low = mid + 1; 
        } else {
            high = mid - 1; 
        }
    }

    return result; 
}

int main() {
    int n, k;
    
    cin >> n >> k;
    
    vector<int> stalls(n);
    for (int i = 0; i < n; i++) {
        cin >> stalls[i];
    }

    int maxMinDist = aggressiveCows(stalls, k);
    cout  << maxMinDist << endl;

    return 0;
}
