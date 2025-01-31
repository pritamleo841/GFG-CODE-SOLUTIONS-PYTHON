//{ Driver Code Starts
// Initial Template for javascript
// Position this line where user code will be pasted.
//  Initial Template for javascript

"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => { inputString += inputStdin; });

process.stdin.on("end", (_) => {
    inputString =
        inputString.trim().split("\n").map((string) => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

/* Function to print an array */
function printArray(arr, size) {
    let i;
    let s = "";
    for (i = 0; i < size; i++) {
        if (arr[i] === -0) arr[i] = 0;
        s += arr[i] + " ";
    }
    console.log(s);
}

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let dict = readLine().split(" ");
        let N = dict.length;
        let K = parseInt(readLine());
        let obj = new Solution();
        let res = obj.findOrder(dict, K);
        let order = "";
        for (let ch of res) order += ch;
        let temp = new Array(N);
        for (let j = 0; j < N; j++) temp[j] = dict[j];
        temp.sort(function(a, b) {
            let index1 = 0;
            let index2 = 0;
            for (let i = 0; i < Math.min(a.length, b.length) && index1 == index2; i++) {
                index1 = order.indexOf(a[i]);
                index2 = order.indexOf(b[i]);
            }

            if (index1 == index2 && a.length != b.length) {
                return a.length - b.length;
            }

            return index1 - index2;
        });
        let flag = true;
        for (let j = 0; j < N; j++) {
            if (dict[j] != temp[j]) {
                flag = false;
            }
        }
        if (flag)
            console.log("true");
        else
            console.log("false");
        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript
//  User function Template for javascript

/**
 * @param {string[]} dict
 * @param {number} k
 * @return {string}
 */
class Solution {
    findOrder(dict, k) {
       // Helper functions to convert characters to indices and vice versa
        function toNum(char) {
            return char.charCodeAt(0) - 'a'.charCodeAt(0);
        }
    
        function toChar(num) {
            return String.fromCharCode(num + 'a'.charCodeAt(0));
        }
    
        // Step 1: Create the adjacency list and indegree array
        let adj = Array.from({ length: k }, () => []);
        let indegree = Array(k).fill(0);
        let present = new Set();
    
        // Initialize the set of present characters
        for (let word of dict) {
            for (let char of word) {
                present.add(toNum(char));
            }
        }
    
        // Step 2: Build the graph from word comparisons
        for (let i = 0; i < dict.length - 1; i++) {
            let s1 = dict[i], s2 = dict[i + 1];
            let length = Math.min(s1.length, s2.length);
    
            // If s1 is longer than s2 and s1 is a prefix of s2, return ""
            if (s1.length > s2.length && s1.slice(0, length) === s2.slice(0, length)) {
                return "";
            }
    
            // Find the first differing character and add the directed edge
            for (let j = 0; j < length; j++) {
                if (s1[j] !== s2[j]) {
                    let u = toNum(s1[j]), v = toNum(s2[j]);
                    adj[u].push(v);
                    indegree[v]++;
                    break;
                }
            }
        }
    
        // Step 3: Perform topological sort using BFS (Kahn's algorithm)
        let queue = [];
        for (let i = 0; i < k; i++) {
            if (present.has(i) && indegree[i] === 0) {
                queue.push(i);
            }
        }
    
        let order = [];
    
        while (queue.length > 0) {
            let node = queue.shift();
            order.push(node);
    
            for (let neighbor of adj[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] === 0) {
                    queue.push(neighbor);
                }
            }
        }
    
        // If cycle detected (not all nodes included), return ""
        if (order.length !== present.size) {
            return "";
        }
    
        // Step 4: Convert the topological order back to characters
        return order.map(num => toChar(num)).join('');
    }
}