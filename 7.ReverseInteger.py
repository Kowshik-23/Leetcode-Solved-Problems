class Solution:
    def reverse(self, x: int) -> int:
        r=1
        if x<0:
            r=-1
            x=x*-1
            p=int(str(x)[::-1])*r
            return 0 if p<-2147483648 else p
        else:
            p=int(str(x)[::-1])
            return 0 if p>2147483648 else p

         
        