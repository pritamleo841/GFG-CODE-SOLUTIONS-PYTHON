//{ Driver Code Starts
// Initial Template for javascript
// Position this line where user code will be pasted.
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split("\n").map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let str = readLine();
        let obj = new Solution();
        console.log(obj.maximumFrequency(str));
        console.log("~")
    }
}

// } Driver Code Ends


// User function Template for javascript
class Solution {
    maximumFrequency(s) {
       const mymap = new Map();
        let str = s.split(' ');
        for(let i=0;i<str.length;i++){
            if(mymap.has(str[i])){
                let val = mymap.get(str[i]);
                val = val+1;
                mymap.set(str[i], val)
            
            }
            else{
                mymap.set(str[i],1)
            }
        }
        let max = mymap.get(str[0]);
        let keyword = str[0];
        for(const[key,value] of mymap.entries()){
            if(value>max){
                keyword = key;
                max=value;
            }
        }
        let out = keyword + " " + max
        return out;
    }
}