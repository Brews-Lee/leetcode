class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def find_substring(s: str) -> str:
            substr = ""
            for char in s:
                if char not in substr:
                    substr += char
                    continue
                break
            return (substr, len(substr))

        substrings = dict()
        if s == "":
            return 0

        while s != "":
            substr_len = find_substring(s)
            substrings.update({substr_len[0]: substr_len[1]})
            s = s.replace(s[0], "", 1)

        values = substrings.values()
        max_len = max(values)

        return max_len