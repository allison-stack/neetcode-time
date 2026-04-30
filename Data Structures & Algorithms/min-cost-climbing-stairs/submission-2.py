class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def min_cost_to_get_to_step(step):
            if step < 2:
                return 0
            if step in memo:
                return memo[step]
            memo[step] = min(min_cost_to_get_to_step(step-1)+cost[step-1], min_cost_to_get_to_step(step-2)+cost[step-2])
            return memo[step]
        return min_cost_to_get_to_step(len(cost))
        