a='1221'

def find(a):
    div=1

    while a<0 :
        return False
    
    if a>10*div:
        div*=10
    
    while a:
        left=a//div
        right=a%10
        if left==right:
            return True
        
    a=(a%div)//10
    div=div/100
    return True
        

#optimized

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        x=str(x)
        list=[d for d in x]
        rl=list[::-1]
        r="".join(rl)
        return r==x
    

        