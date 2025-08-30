import sys

while True:
    try:
        alph = list(input())
        N = int(input())
        for i in range(N):
            L = int(input())
            i = L
            print(''.join(alph[i-1]), end=' ')
    except EOFError:
        break