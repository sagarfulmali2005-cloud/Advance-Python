# 0/1 Knapsack using Bottom-Up and Top-Down DP

memo = {}

def top_down(wt, val, n, W):
    if n == 0 or W == 0:
        return 0
    if (n, W) in memo:
        return memo[(n, W)]

    if wt[n-1] <= W:
        memo[(n, W)] = max(
            val[n-1] + top_down(wt, val, n-1, W-wt[n-1]),
            top_down(wt, val, n-1, W))
    else:
        memo[(n, W)] = top_down(wt, val, n-1, W)

    return memo[(n, W)]


def bottom_up(wt, val, n, W):
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(
                    val[i-1] + dp[i-1][w-wt[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]


n = int(input("Items: "))
wt = list(map(int, input("Weights: ").split()))
val = list(map(int, input("Values: ").split()))
W = int(input("Capacity: "))

while True:
    print("\n1.Bottom-Up  2.Top-Down  3.Both  4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        print("Maximum value:", bottom_up(wt, val, n, W))

    elif ch == 2:
        memo.clear()
        print("Maximum value:", top_down(wt, val, n, W))

    elif ch == 3:
        memo.clear()
        print("Bottom-Up:", bottom_up(wt, val, n, W))
        print("Top-Down:", top_down(wt, val, n, W))

    elif ch == 4:
        break

    else:
        print("Invalid choice")