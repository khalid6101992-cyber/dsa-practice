function threeSum(nums: number[]): number[][] {
    
    let sortedValues = nums.sort((a,b) => a - b);
    let result = [];
    let fixed;
    let left;
    let right = sortedValues.length - 1;
    let target;
    for (const [i,num] of sortedValues.entries()) {
        if (i > 0 && sortedValues[i] == sortedValues[i - 1]) {
            continue
        }
        target = -(sortedValues[i]);
        fixed = sortedValues[i];
        right = sortedValues.length - 1;
        left = i + 1

        while (left < right) {
            if (target > sortedValues[left] + sortedValues[right]) {
                left ++;
            } else if(target < sortedValues[left] + sortedValues[right]) {
                right --;
            } else {
                result.push([sortedValues[i], sortedValues[left], sortedValues[right]])
                left ++;
                right --;
                while (left < right && (sortedValues[left] == sortedValues[left-1])) {
                    left ++;
                }
            }
        }
        
    }
    console.log(sortedValues)

    return result;

};