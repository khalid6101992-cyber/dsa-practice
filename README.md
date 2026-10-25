# DSA Practice

My daily Data Structures & Algorithms practice in **Python**, organized by pattern.
Each solution includes the approach, time/space complexity, and notes on mistakes I learned from.

**Goal:** consistent daily practice for software engineering interviews.

## Progress

| # | Problem | Pattern | Difficulty | Time | Space | Solution |
|---|---------|---------|------------|------|-------|----------|
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Hashing | Easy | O(n) | O(n) | [Python](hashing/0217-contains-duplicate.py) |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Hashing | Easy | O(n) | O(n) | [Python](hashing/0001-two-sum.py) |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Hashing | Easy | O(n) | O(1) | [Python](hashing/0242-valid-anagram.py) |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Hashing | Medium | O(n·k log k) | O(n·k) | [Python](hashing/0049-group-anagrams.py) |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Hashing, Bucket Sort | Medium | O(n) | O(n) | [Python](hashing/0347-top-k-frequent-elements.py) |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Hashing | Medium | O(n) | O(n) | [Python](hashing/0128-longest-consecutive-sequence.py) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Two Pointers | Easy | O(n) | O(1) | [Python](two-pointers/0125-valid-palindrome.py) |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Pointers | Medium | O(n) | O(1) | [Python](two-pointers/0167-two-sum-ii.py) |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Two Pointers | Medium | O(n²) | O(n) | [Python](two-pointers/0015-3sum.py) |

**Solved: 9** (Easy: 4 · Medium: 5)

## Patterns covered

- **Hashing** — sets for "seen before?", dictionaries for counting and lookups
- **Bucket sort** — placing items by count instead of sorting
- **Two pointers** — comparing from both ends, moving inward; fix one + Two Sum II for 3Sum

## Structure

```
hashing/        Hash map and set problems
two-pointers/   Two pointer problems
```

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0001-two-sum) |
| [0011-container-with-most-water](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0011-container-with-most-water) |
| [0015-3sum](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0015-3sum) |
| [0049-group-anagrams](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0049-group-anagrams) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0121-best-time-to-buy-and-sell-stock) |
## Two Pointers
|  |
| ------- |
| [0011-container-with-most-water](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0011-container-with-most-water) |
| [0015-3sum](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0015-3sum) |
| [0567-permutation-in-string](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0567-permutation-in-string) |
## Sorting
|  |
| ------- |
| [0015-3sum](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0015-3sum) |
| [0049-group-anagrams](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0049-group-anagrams) |
## Greedy
|  |
| ------- |
| [0011-container-with-most-water](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0011-container-with-most-water) |
## Dynamic Programming
|  |
| ------- |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0121-best-time-to-buy-and-sell-stock) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0001-two-sum) |
| [0003-longest-substring-without-repeating-characters](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0003-longest-substring-without-repeating-characters) |
| [0049-group-anagrams](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0049-group-anagrams) |
| [0424-longest-repeating-character-replacement](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0424-longest-repeating-character-replacement) |
| [0567-permutation-in-string](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0567-permutation-in-string) |
## String
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0003-longest-substring-without-repeating-characters) |
| [0049-group-anagrams](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0049-group-anagrams) |
| [0424-longest-repeating-character-replacement](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0424-longest-repeating-character-replacement) |
| [0567-permutation-in-string](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0567-permutation-in-string) |
## Sliding Window
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0003-longest-substring-without-repeating-characters) |
| [0424-longest-repeating-character-replacement](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0424-longest-repeating-character-replacement) |
| [0567-permutation-in-string](https://github.com/khalid6101992-cyber/dsa-practice/tree/master/0567-permutation-in-string) |
<!---LeetCode Topics End-->