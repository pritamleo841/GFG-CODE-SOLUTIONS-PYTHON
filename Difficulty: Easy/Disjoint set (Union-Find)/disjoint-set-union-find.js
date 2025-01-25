//{ Driver Code Starts
// Initial Template for javascript

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split('\n').map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {

        let obj = new Solution();
        let [n, k] = readLine().trim().split(" ").map((x) => parseInt(x));
        let a = new Array(n + 1);
        for (let j = 0; j <= n; j++) a[j] = j;
        let input = readLine().trim().split(" ");
        let j = 0;
        let s = "";
        while (j < input.length) {

            if (input[j] === "UNION") {
                let x = parseInt(input[j + 1]);
                let z = parseInt(input[j + 2]);
                obj.unionSet(a, x, z);
                j += 3;
            } else {
                let x = parseInt(input[j + 1]);
                let parent = obj.find(a, x);
                s += parent;
                s += " ";
                j += 2;
            }
        }
        console.log(s);

        console.log("~");
    }
}
// } Driver Code Ends


// User function Template for javascript

class Solution {

    /*Complete the functions below*/
    find(par, x) {
        // add code here
        if(x===par[x]){
            return x
        }
        return this.find(par,par[x])
    }

    unionSet(par, x, z) {
        // add code here
        let parentX = this.find(par,x)
        let parentZ = this.find(par,z)
        if(parentX!=parentZ)
            par[parentX]=parentZ
    }
}
