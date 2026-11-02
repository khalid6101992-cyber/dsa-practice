class MinStack {
    minStack = []
    smallest = []
    constructor() {
        this.minStack = []
        this.smallest = []
    }

    push(value: number): void {
        this.minStack.push(value)
        let note;
        if (this.smallest.length == 0) {
            note = value
        } else {
            note = Math.min(value, this.smallest.at(-1))
        }
        this.smallest.push(note)
    }

    pop(): void {
        this.smallest.pop()
        this.minStack.pop()
        
    }

    top(): number {
        return this.minStack.at(-1)
        
    }

    getMin(): number {
        return this.smallest.at(-1)
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(value)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */