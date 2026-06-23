class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """initially i made a code with extra elif people[right]<= limit,
            which is useless, constraint says, people[i] <= limit, so elif condition
            is always true
        """

        people.sort()
        left, right = 0, len(people)-1
        count = 0

        while left <= right:
            s = people[left] + people[right]
            if s <= limit:
                left+=1

            right-=1
            count+=1

        return count