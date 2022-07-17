import sys

n, m = map(int, sys.stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]
ans = []

for i in range(1, n + 1):
    matrix[i][1:] = map(int, sys.stdin.readline().split())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    ans.append(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])

for i in range(len(ans)):
    print(ans[i])
