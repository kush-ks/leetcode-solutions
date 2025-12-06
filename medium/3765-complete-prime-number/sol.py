from linecache import cache


class Solution:
    def completePrime(self, num: int) -> bool:
        
        @cache
        def isPrime(n):
            if n == 0: return True
            if n == 1: return False
            if n == 2: return True
            if n > 2 and not n&1:
                return False
            for i in range(2,int(pow(n,0.5))+1):
                if n % i == 0:
                    return False
            return True


        x = num
        ans = isPrime(num)

        # prefix
        while ans and x > 0:
            x //= 10
            ans &= isPrime(x)

        
        # suffix
        x = num % 10
        num //= 10
        a = 1
        
        while ans and num >= 0:
            ans &= isPrime(x)
            x = (num%10)*pow(10,a) + x
            num //= 10
            a += 1
            if num == 0: break
            
        
        return ans