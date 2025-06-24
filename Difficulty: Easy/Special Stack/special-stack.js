class SpecialStack {
    constructor(capacity = Infinity) {
        this.stack = [];
        this.minStack = [];
        this.capacity = capacity;
    }

    /**
     * @param {number} x
     * @return {void}
     */
    push(x) {
        if (this.stack.length < this.capacity) {
            this.stack.push(x);
            if (this.minStack.length === 0) {
                this.minStack.push(x);
            } else {
                this.minStack.push(Math.min(x, this.minStack[this.minStack.length - 1]));
            }
        }
    }

    /**
     * @return {number}
     */
    pop() {
        if (this.stack.length === 0) return -1;
        this.minStack.pop();
        return this.stack.pop();
    }

    /**
     * @return {boolean}
     */
    isFull() {
        return this.stack.length >= this.capacity;
    }

    /**
     * @return {boolean}
     */
    isEmpty() {
        return this.stack.length === 0;
    }

    /**
     * @return {number}
     */
    getMin() {
        if (this.minStack.length === 0) return -1;
        return this.minStack[this.minStack.length - 1];
    }
}