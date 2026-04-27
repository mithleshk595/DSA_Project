class solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = x 

        while l <= r:
            mid = l + (r + l)//2
            midSquare = mid*mid

            if midSquare>x:
                r = mid -1
            
            else:
                ans = mid
                l = mid + 1
        return ans
    