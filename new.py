#User function Template for python3
from typing import List
class Solution:
    def playOfGlasses(self, c1:int, w1:int, c2:int, w2:int, c3:int, w3:int) -> List[int] :
        def playOfGlasses(c1, w1, c2, w2, c3, w3):
            for _ in range(10**5):
                poured = min(w1, c2 - w2)
                w1 -= poured
                w2 += poured
                poured = min(w2, c3 - w3)
                w2 -= poured
                w3 += poured
                poured = min(w3, c1 - w1)
                w3 -= poured
                w1 += poured

            return [w1, w2, w3]

# Example usage:
c1, w1 = 10, 3
c2, w2 = 11, 4
c3, w3 = 12, 5
print(playOfGlasses(c1, w1, c2, w2, c3, w3)) 

if __name__ == "__main__":
    for _ in range(int(input())):
        c1, w1, c2, w2, c3, w3 = map(int,input().split())
        obj = Solution()
        res = obj.playOfGlasses(c1, w1, c2, w2, c3, w3)
        print(" ".join(map(str,res)))