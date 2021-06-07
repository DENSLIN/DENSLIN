test = int(input())
print("\n")


def function(x, y):
    count = 0
    y = int(y)
    for data in x:
        data = int(data)
        if y >= data:
            y = y - data
            count += 1
    return count


while test >= 1:

    n, b = input().split()
    a = sorted(input().split())
    buy_house = function(a, b)
    print("case" + str(test-4) + ": " + str(buy_house))
    test -= 1





