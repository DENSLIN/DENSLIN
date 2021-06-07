t = int(input())
while t != 0:
    n, k = input().split()
    n = int(n)
    k = int(k)
    m = input().split()
    diff = []
    i = 0
    j = 1
    while n != 1:
        data = -(int(m[i]) - int(m[j]))/2
        diff.append(data)
        i += 1
        j += 1
        n -= 1
    print("\n")
    print(diff)
    print(int(max(diff)))
    t -= 1

