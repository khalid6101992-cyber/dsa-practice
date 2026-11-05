/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    let stack = []
    let wait = []
    for (let temp in temperatures) {
        wait[temp] = 0
    }
    for (let [i, temp] of temperatures.entries()) {
        let waiting_day = 0
        while (stack.length != 0 && temp > temperatures[stack.at(-1)]) {
            waiting_day = stack.pop()
            wait[waiting_day] = i - waiting_day
        }
        stack.push(i)
    }
    return wait
};