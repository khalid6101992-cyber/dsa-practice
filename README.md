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

**Solved: 7** (Easy: 4 · Medium: 3)

## Patterns covered

- **Hashing** — sets for "seen before?", dictionaries for counting and lookups
- **Bucket sort** — placing items by count instead of sorting
- **Two pointers** — comparing from both ends, moving inward

## Structure

```
hashing/        Hash map and set problems
two-pointers/   Two pointer problems
```
