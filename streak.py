class Solution:
    def score(self, N, k):
        count = 0
        m = 1
        while N > 0:
            N -= m ** k
            m += 1
            count += 1
        
        return count

# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        N, k = map(int, input().split())
        ob = Solution()
        ans = ob.score(N, k)
        print(ans)
        tc -= 1
