// User function Template for javascript

/*
class MyQueue {
    constructor(){
        this.front = 0;
        this.arr = [];
    }
    push(x){
        this.arr.push(x);
    }
    pop(){
        if(this.front == this.arr.length)
            return -1;
        return this.arr[this.front++];
    }
}
*/

class Solution {

    /**
     * @param {MyQueue} q
     * @param {number} x
     */

    enqueue(q, x) {
        // Enqueue element x to rear of the queue
        q.push(x);
    }

    /**
     * @param {MyQueue} q
     * @returns {number}
     */

    dequeue(q) {
        // Dequeue element from front of the queue
        return q.pop();
    }

    /**
     * @param {MyQueue} q
     * @returns {number}
     */
    front(q) {
        // Return the front element without removing it
        if (q.front < q.arr.length) {
            return q.arr[q.front];
        }
        return -1;
    }

    /**
     * @param {MyQueue} q
     * @param {number} x
     * @returns {string}
     */
    find(q, x) {
        for (let i = q.front; i < q.arr.length; i++) {
            if (q.arr[i] === x) {
                return "Yes";
            }
        }
        return "No";
    }
}
