
#high complexity solution

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map={}
        for c in magazine:
            if c in hash_map:
                hash_map[c] +=1
            else:
                hash_map[c]=1
        for c in ransomNote:
            if c not in hash_map:
                return False
            elif hash_map[c]==1:
                del hash_map[c]
            else:
                hash_map[c]-=1
        return True


#using Counter from collections.  much more efficient than other one
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter =Counter(magazine)
        for c in ransomNote:
            if counter[c]==0:
                return False
            elif counter[c]==1:
                del counter[c]
            else:
                counter[c] -=1
        return True