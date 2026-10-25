function twoSum(nums: number[], target: number): number[] {
    const notebook = new Map<number, number>();
    let data = [];
    nums.forEach((num, i) => {
        const needed = target - num;
        if (notebook.has(needed)) {
            data = [notebook.get(needed), i]
        }
        notebook.set(nums[i], i);
    })
    return data;
};