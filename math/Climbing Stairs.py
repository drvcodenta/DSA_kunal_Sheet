n = 4
dp = [-1 for i in range(n+1)]
def count(n, dp):
    if n <= 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = count(n-1, dp) + count(n-2, dp)
    return dp[n]

print(count(n, dp))