
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        j = 0
        profit = 0
        for i in range(1 ,len(prices)):
            if prices[ i -1] > prices[i]:
                j = i
            if prices[i] > prices[ i -1] and (( i +1) == len(prices) or prices[i] > prices[ i +1]):
                profit += (prices[i] - prices[j] - fee)

        return profit

if __name__ == '__main__':
    print(Solution().maxProfit([1,3,2,8,4,9],2))