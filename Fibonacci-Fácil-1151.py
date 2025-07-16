N = int(input())
fib = []
for i in range(N):
    fib.append(i)
    if i == 2:
        fib[i] = fib[0] + fib[1]
    if i > 2:
        fib[i] = fib[i-1] + fib[i-2]
print(*fib)