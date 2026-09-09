class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp ={None:None}
        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next
        
        for curr in mp:
            if curr:
                newCr = mp.get(curr)
                currN = curr.next
                currR = curr.random

                newCr.next = mp[currN]
                newCr.random = mp[currR]

        return mp[head]
