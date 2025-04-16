//{ Driver Code Starts
// Initial Template for C++
//  CPP code to implement functions of priority_queue
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

/* Function to implement push operation in priority_queue
 * pq : priority_queue
 * x : element to be pushed
 */
void push(priority_queue<int, vector<int>, greater<int>> &pq, int x) {
    pq.push(x);
}

/* Function to implement pop operation in priority_queue
 * pq : priority_queue
 */
void pop(priority_queue<int, vector<int>, greater<int>> &pq) {

    if (!pq.empty()){
        pq.pop();
    }
    else return;
}

/* Function to implement top operation in priority_queue
 * pq : priority_queue
 */
int top(priority_queue<int, vector<int>, greater<int>> &pq) {

    if (!pq.empty()){
        return pq.top(); 
    }
    else return -1;
}


//{ Driver Code Starts.

// Driver code
int main() {

    int testcase;
    cin >> testcase;

    // Declaring priority queue
    priority_queue<int, vector<int>, greater<int>> pq;

    while (testcase--) {
        // Queries input
        int queries;
        cin >> queries;

        while (queries--) {

            string s;
            cin >> s;

            // If query is to push
            if (s == "p") {
                int x;
                cin >> x;
                push(pq, x);
                cout << pq.size() << endl;
            }

            // If query is to pop
            if (s == "pp") {
                pop(pq);

                cout << pq.size() << endl;
            }

            // If query is to return top
            if (s == "t") {
                cout << top(pq) << endl;
            }
        }

        // resetting priority queue
        pq = priority_queue<int, vector<int>, greater<int>>();

        cout << "~"
             << "\n";
    }

    return 0;
}
// } Driver Code Ends