class solution:
    def countDigits(self, num: int) -> int:
        temp = num
        result = 0
        while temp > 0:
            r = temp % 10
            if num % r == 0:
                result += 1
                temp//=10
        return result
    