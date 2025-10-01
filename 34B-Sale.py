    n, m = map(int, input().split())
    ai = list(map(int, input().split()))
     
    ai.sort()  # Sort once, ascending (negative prices first)
    count = 0
    for i in range(m):
        if ai[i] < 0:
            count += ai[i]
        else:
            break
    print(-count)  # Negative sum ka positive value print karna hai
