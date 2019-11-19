#
# @lc app=leetcode id=518 lang=python
#
# [518] Coin Change 2
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        memo = {}
        return self.changeHelper(amount, coins, memo)

    def changeHelper(self, amount, coins, memo):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        total_coins = 0
        for i in range(len(coins)):
            if amount - coins[i] >= 0:
                total_coins = self.changeHelper(amount - coins[i], coins, memo)
        memo[amount] = total_coins + 1
        return memo[amount]
        

        
# @lc code=end

