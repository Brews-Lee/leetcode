# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        def find_common(s1: str, s2: str) -> str:
            common = ""
            count = 0
            if len(s1) > len(s2):
                count = len(s2)
            else:
                count = len(s1)

            for i, char in enumerate(s1):
                if i == count:
                    break
                if s1[i] == s2[i]:
                    common += char
                else:
                    break
            return common
        if not len(strs) == 1:
            prefix = find_common(strs[0], strs[1])
        else:
            prefix = strs[0]
            return prefix
        i = 2
        for s in strs:
            if i == len(strs):
                break
            prefix = find_common(prefix, strs[i])
            i += 1
        return prefix