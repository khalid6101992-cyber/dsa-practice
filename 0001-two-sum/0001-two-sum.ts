function twoSum(nums: number[], target: number): number[] {
    const notebook = new Map<number, number>();
    let needed = 0;
    for (const [i, num] of nums.entries()) {
        needed = target - num;
        if (notebook.has(needed)) {
            return [notebook.get(needed), i]
        }
        notebook.set(num, i)
    }
    return [];
};