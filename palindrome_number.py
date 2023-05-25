class Solution:
    def isPalindrome(self, x: int) -> bool:
        set=str(x)
        l=len(set)-1
        for num in set:
            if num==set[l]:
                print(num)
            else:
                return False
            l=l-1
        return True

