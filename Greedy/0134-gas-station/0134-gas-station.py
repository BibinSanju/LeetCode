class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = start = total = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total+=diff
            tank+=diff
            
            if tank <0:
                tank = 0
                start = i + 1
        
        return -1 if total<0 else start
