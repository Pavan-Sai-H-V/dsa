#solution using hashmap
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map=defaultdict(int)

        for c in s:
            map[c]+=1

        for i,n in enumerate(s):
            if map[n]==1:
                return i
        return -1

# solution using linear logic
