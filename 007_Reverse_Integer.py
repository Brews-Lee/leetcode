class Solution:
    def reverse(self, x: int) -> int:
        reversed = str(x)[::-1]
        if reversed[len(reversed) - 1] == "-":
            reversed = reversed.replace("-", "")
            reversed = - int(reversed)
        if int(reversed) > pow(2, 31) - 1 or int(reversed) < - pow(2, 31):
            return 0
        else:
            return int(reversed)