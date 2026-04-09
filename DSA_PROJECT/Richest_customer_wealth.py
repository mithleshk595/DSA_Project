class solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0

        for account in accounts:
            ans = max(ans, sum(account))

        return ans
    