test = int(input())
print("\n")
count = 1
while test >= 1:

    n, k, p = input().split()
    n = int(n)
    p = int(p)
    k = int(k)
    data = []
    int_count = 0

    temp = 0
    sum = []
    sum_data = 0
    while int_count != n:
        input_data = input().split()
        data.append(input_data)
        int_count += 1
    limit = k
    if n == 2:
        dub_p = n*k/2
    else:
        dub_p = 2
    p_copy = p
    while dub_p != 0:
        sum_data = 0
        i = 0
        j = 0
        while p != 0:

            sum_data += int(data[i][j])
            j += 1
            p -= 1
            # print(sum_data)
            if n == 3 and i == 0 and j == limit:
                j = 0
                i += 2
            if n == 2 and j == limit and i == 0:
                j = 0
                i += 1
        sum.append(sum_data)
        p = p_copy
        limit -= 1
        dub_p -= 1
    print("case #" + str(count) + ": " + str(max(sum)))
    count += 1
    test -= 1
