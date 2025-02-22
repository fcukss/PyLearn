"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

strs = ["Stas"]

# name= "Stanislav"
# print(name[:2:])

def longestCommonPrefix(strs):
    res = ""
    strs.sort()
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return res
        res += first[i]
    return res

print(longestCommonPrefix(strs))