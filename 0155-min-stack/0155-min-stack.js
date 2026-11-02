
var MinStack = function() {
    this.minStack = []
    this.smallest = []
};

/** 
 * @param {number} value
 * @return {void}
 */
MinStack.prototype.push = function(value) {
    let note;
    this.minStack.push(value)
    if(this.smallest.length == 0) {
        note = value
    } else {
        note = Math.min(value, this.smallest.at(-1))
    }
    this.smallest.push(note)
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.minStack.pop()
    this.smallest.pop()
    
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.minStack.at(-1)
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.smallest.at(-1)
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(value)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */