

k, p = input().split()
n = 2
p = int(p)
k = int(k)
data = []
int_count = 0
temp = 0
sum = []
sum_data = 0

# input data
while int_count != n:
    input_data = input().split()
    data.append(input_data)
    int_count += 1

dub_p = limit = k
p_copy = p
# sum of all combination
while dub_p != 0:
    sum_data = 0
    i = 0
    j = 0
    while p != 0:

        sum_data += int(data[i][j])
        j += 1
        p -= 1
        if j == limit and i == 0:
            j = 0
            i += 1
    sum.append(sum_data)
    p = p_copy
    limit -= 1
    dub_p -= 1
# picking out maximum one
print(sum)
ans = str(max(sum))
print("case #:" + ans)


'''
Input:
4 5
10 10 100 30
80 50 10 50
Output:
250

Input:
5 6
10 10 100 30 10
80 50 10 50 10
Output:
280
'''