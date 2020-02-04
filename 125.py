import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = re.compile('[\W_]+')
        s = new_string.sub('', s)
        s = s.lower()
        count = 0
        for i in range(len(s)//2):
            if((s[i] == s[-(i+1)])):
                count+=1
        if count == (len(s)//2):
            return 1
        else:
            return 0