function groupAnagrams(strs: string[]): string[][] {
    let sortedValue;
    let result = new Map();
    for (const data of strs) {
        sortedValue = data.split("").sort().join("")
        
        if (!result.has(sortedValue)){
            result.set(sortedValue, [])
        }
        result.get(sortedValue).push(data);
        
    }
    return [...result.values()];
};