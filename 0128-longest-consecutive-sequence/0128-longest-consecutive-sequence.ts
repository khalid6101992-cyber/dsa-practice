function longestConsecutive(nums: number[]): number {
    const numSet = new Set(nums);
    console.log(numSet)
    let longest = 0;
    for (const num of numSet) {                 
        if (!numSet.has(num - 1)) {                          
            let length = 1;
            while (numSet.has(num + length)) {                   
                length++;
            }
            longest = Math.max(longest, length);
        }
    }
    return longest;
}