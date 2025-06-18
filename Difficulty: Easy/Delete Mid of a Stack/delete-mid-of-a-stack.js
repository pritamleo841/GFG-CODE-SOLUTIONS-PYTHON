// User function Template for JavaScript

class Solution {
    deleteMid(stack) {
        const size=stack.length;
        function recur(count) {
            if (count===Math.floor(size/2)) {
                stack.pop(); // Delete middle element
                return;
            }
            const temp=stack.pop(); // Pop top
            recur(count+1);         // Go deeper
            stack.push(temp);         // Push back after middle is removed
        }
        recur(0);
    }
}
