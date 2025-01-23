//{ Driver Code Starts
//Initial Template for javascript

"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((string) => {
      return string.trim();
    });

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/* Function to print an array */
function printArray(arr, size) {
  let i;
  let s = "";
  for (i = 0; i < size; i++) {
    if(arr[i] == -0)
      arr[i] = 0;
    s += arr[i] + " ";
  }
  console.log(s);
}

function main() {
  let t = parseInt(readLine());
  let i = 0;
  for (; i < t; i++) {
    let n = parseInt(readLine());
    let dictionary = new Array(n);
    let input = readLine().split(" ");
    for(let j = 0;j<n;j++) dictionary[j] = input[j];
    let input2 = readLine().split(" ").map((x)=>parseInt(x));
    let R = input2[0];
    let C = input2[1];
    let board = [];
    for(let j = 0;j<R;j++){
      let row = readLine().split(" ");
      board.push(row);
    }

    let obj = new Solution();
    let res = obj.wordBoggle(board,dictionary);
    if(res.length===0){
      console.log("-1");
    }
    else{
      res.sort();
      printArray(res,res.length);
    }
  }
}
// } Driver Code Ends


//User function Template for javascript

/**
 * @param {string[][]} board
 * @param {string[]} dictionary
 * @return {string[]}
 */
class TrieNode {
    constructor() {
        this.children = {};
        this.isEndOfWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children[char]) {
                node.children[char] = new TrieNode();
            }
            node = node.children[char];
        }
        node.isEndOfWord = true;
    }
}
class Solution {
    wordBoggle(board,dictionary){
        //code here
        const trie = new Trie();
        for (const word of dictionary) {
            trie.insert(word);
        }

        const directions = [
            [-1, 0], [1, 0], [0, -1], [0, 1],
            [-1, -1], [1, 1], [-1, 1], [1, -1]
        ];
        const n = board.length, m = board[0].length;
        const result = new Set();

        const isInBoundary = (x, y) => x >= 0 && x < n && y >= 0 && y < m;

        const dfs = (x, y, node, path, visited) => {
            if (node.isEndOfWord) {
                result.add(path);
            }

            visited.add(`${x},${y}`); // Mark the current cell as visited

            for (const [dx, dy] of directions) {
                const nx = x + dx, ny = y + dy;
                if (
                    isInBoundary(nx, ny) &&
                    !visited.has(`${nx},${ny}`) &&
                    node.children[board[nx][ny]]
                ) {
                    dfs(nx, ny, node.children[board[nx][ny]], path + board[nx][ny], visited);
                }
            }

            visited.delete(`${x},${y}`); // Backtrack
        };

        // Start DFS from each cell
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                const char = board[i][j];
                if (trie.root.children[char]) {
                    dfs(i, j, trie.root.children[char], char, new Set());
                }
            }
        }

        return Array.from(result).sort(); // Return sorted list of found words
    }
}
