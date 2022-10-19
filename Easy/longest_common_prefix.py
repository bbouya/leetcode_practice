"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
"""



from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for i in range(len(strs[0])):
            for s in strs :
                if i==len(s)or s[i]!=strs[0][i]:
                    return result
            result += strs[0][i]
        return result

if __name__ == "__main__":
    print('auu')
    strs = ["flower","flow","flight"]
    resul = Solution()
    print(resul.longestCommonPrefix(strs))