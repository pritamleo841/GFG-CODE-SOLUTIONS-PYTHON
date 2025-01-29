//{ Driver Code Starts
//Initial Template for javascript

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let n = parseInt(readLine());
        let p = parseInt(readLine());
        
        let arr = [];
        let obj = new Solution();
        for(let i=0;i<p;i++)
        {
            let input_line = readLine().split(' ');
            arr.push(input_line);
        }
        let ans = obj.isPossible(arr,n,p);
        console.log(ans);
    }
}
// } Driver Code Ends


//User function Template for javascript

/**
 * @param {number[][]} prerequisites
 * @param {number} n
 * @param {number} p
 * @returns {boolean}
*/
class Solution {
    isPossible(prerequisites, N,p) {
        // Step 1: Initialize adjacency list and indegree array
        let adj = new Array(N).fill().map(() => []); // Create an empty adjacency list
        let indegree = new Array(N).fill(0); // Initialize indegree array with zeros
        
        // Step 2: Build the graph (adjacency list and indegree array)
        for (let [u, v] of prerequisites) {
            adj[v].push(u); // v → u (task u depends on task v)
            indegree[u] += 1; // task u has one more prerequisite
        }
        
        // Step 3: Initialize the queue with nodes that have no prerequisites (indegree 0)
        let queue = [];
        for (let i = 0; i < N; i++) {
            if (indegree[i] === 0) {
                queue.push(i);
            }
        }
        
        // Step 4: Process the queue using Kahn's Algorithm (Topological Sort)
        let topoCount = 0; // Number of tasks processed
        
        while (queue.length > 0) {
            let node = queue.shift(); // Dequeue the task
            topoCount += 1; // We are processing one task
            
            // Decrease in-degree of the neighbors
            for (let neighbor of adj[node]) {
                indegree[neighbor] -= 1;
                if (indegree[neighbor] === 0) {
                    queue.push(neighbor); // Add to the queue if no more prerequisites
                }
            }
        }
        
        // Step 5: If the number of tasks processed is equal to N, return "Yes", otherwise "No"
        return topoCount === N ? "Yes" : "No";
    }
}
