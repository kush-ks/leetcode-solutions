class Solution:
    def reverseWords(self, s: str) -> str:
        s = s + ' '
        word = ""
        firstVowel = -1
        currVowel = 0
        ans = ""
        
        for ch in s:
            if ch == ' ':
                if firstVowel == -1:
                    firstVowel = currVowel
                    currVowel = 0
                    ans += word + ' '
                else:
                    if currVowel == firstVowel:
                        ans += word[::-1] + ' '
                    else:
                        ans += word + ' '
                word = ""
                currVowel = 0

            else:
                if ch in ['a','e','i','o','u']: currVowel += 1
                word += ch


        return ans[:-1]