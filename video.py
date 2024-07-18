def min_frames(A):
    N = len(A)
    dp = [0]*N
    dp[0] = 1
    for i in range(1, N):
        if A[i] == A[i-1]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + 1
    return dp[-1]

A = list(int, input("Enter the elements: ").split())
print(min_frames(A))