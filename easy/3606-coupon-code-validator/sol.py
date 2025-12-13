class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        def isValidCode(code):
            if code == "": 
                return False
            for ch in code:
                if not('0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or ch == '_'):
                    return False
            return True


        el,gr,ph,re = [],[],[],[]
        n = len(code)

        for i in range(n):
            c = code[i]
            btype = businessLine[i]
            if not isActive[i]:         continue
            if not isValidCode(c):      continue
            if btype == "electronics":  el.append(c)
            elif btype == "grocery":    gr.append(c)
            elif btype == "pharmacy":   ph.append(c)
            elif btype == "restaurant": re.append(c)

        ans = []
        if el: el.sort(); ans += el
        if gr: gr.sort(); ans += gr
        if ph: ph.sort(); ans += ph
        if re: re.sort(); ans += re

        return ans