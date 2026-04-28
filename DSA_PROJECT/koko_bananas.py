class solution:
    def getHours(self, piles, mid):
        hours = 0
        for pile in piles:
            hours += pile+mid-1//mid

        return hours
    
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)

        l = 1
        r = max(piles)
        k = r

        while l<=r:
            mid = l+(r-l)//2

            if self.getHours(piles, mid) > h:
                l = mid + 1
            else:
                r = mid - 1
                k = mid
        
        return k
    

