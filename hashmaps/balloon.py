#brute froce method
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count_a=count_b=count_l=count_o=count_n=0

        for c in text:
            if c=='a':
                count_a +=1
            elif c=='b':
                count_b +=1
            elif c=='l':
                count_l +=1
            elif c=='o':
                count_o +=1
            elif c=="n":
                count_n +=1
            else:
                pass
            
        result=min(count_a,count_b,count_l//2,count_o//2,count_n)
        return result
    

#hashmap solution

from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map=defaultdict(int)
        target='balloon'

        for c in text:
            if c in target:
                map[c]+=1
        
        if any(c not in text for c in target):
            return 0
        else:
            return min(map['a'],map['l']//2,map['o']//2,map['b'],map['n'])
        



        