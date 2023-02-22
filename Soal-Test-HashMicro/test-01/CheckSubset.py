n = int(input())

for _ in range(n):
    a = input()
    xa = set(input().split())
    b = int(input())
    yb = set(input().split())
    print(xa.issubset(yb))