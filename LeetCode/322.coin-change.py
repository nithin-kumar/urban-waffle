#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        memo = {}
        out = self.coinChangeHelper(coins, amount, memo, 0)
        if out == 100000:
            return -1
        else:
            return out
    def coinChangeHelper(self, coins, amount, memo, j):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        min_coins = 99999
        for i in range(len(coins)):
            if amount - coins[i] >= 0:
                min_coins = min(min_coins,
                self.coinChangeHelper(coins, amount - coins[i], memo, i))
        memo[amount] = min_coins + 1
        return min_coins + 1
        
# @lc code=end

