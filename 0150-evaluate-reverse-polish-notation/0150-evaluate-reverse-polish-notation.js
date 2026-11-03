/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    let result = []
    operatorSet = new Set(["+","-","*","/"])
    for (const token of tokens) {
        let data;
        if(operatorSet.has(token)) {
            right = +(result.pop())
            left = +(result.pop())
            if(token == "+") {
                data = left + right
            } else if(token == "-") {
                data = left - right
            } else if(token == "*") {
                data = left * right
            } else if(token == "/") {
                data = Math.trunc(left / right)
            }
            result.push(data)
        } else {
            result.push(+(token))
        }
    }
    return result.at(-1)
};