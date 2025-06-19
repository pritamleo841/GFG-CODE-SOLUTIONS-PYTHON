/**
 * @param {Queue} q
 * @returns {Queue}
 */

/*
class Queue{
    constructor(){
        this.arr = [];
        this.front = 0;
    }

    push(a){
        this.arr.push(a);
    }

    pop(){
        if(this.arr.length != this.front){
            let x = this.arr[this.front];
            this.front++;
            return x;
        }
        else
            return -1;
    }

    front_ele(){
        return this.arr[this.front];
    }

    empty(){
        if(this.arr.length != this.front)
            return false;
        else
            return true;
    }
}
*/

class Solution {
    // Function to reverse the queue.
    reversedQueue(q) {
        let stack=[];
        //Dequeue all elements and push onto stack
        while(!q.empty()){
            stack.push(q.pop());
        }
        //Push all elements back to queue(in reversed order)
        for(let i=stack.length-1;i>=0;i--) {
            q.push(stack[i]);
        }
        return q;
            
    }
}