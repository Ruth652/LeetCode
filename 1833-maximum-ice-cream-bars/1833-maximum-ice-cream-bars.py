class Solution(object):
    def maxIceCream(self, costs, coins):
        count = 0
        total = 0
        
        sortedCost = sorted(costs)
        for i in range(len(sortedCost)):
            if total + sortedCost[i] > coins:
                break
            total += sortedCost[i]
            count += 1
            
        return count
