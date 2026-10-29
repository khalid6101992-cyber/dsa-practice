function isValid(s: string): boolean {
    
    let stack = []
    let pairs = new Map([
        [')', '('],
        [']', '['],
        ['}', '{'],
    ])

    console.log(pairs)
    for(let ch of s) {
        console.log(ch)
        if (pairs.has(ch)) {
            if (stack.length == 0 || stack.at(-1) != pairs.get(ch)) {
                return false
            }
        stack.pop()
        }
        else {
            stack.push(ch)
        }
    }
    return stack.length == 0
};