def sol(n):
    # 100 이하는 무조건 n, 111 이하는 무조건 99
    sum = 99
    if n < 100: return n
    elif n < 111: return sum
    for i in range(111, n + 1):
        s = list(map(int, str(i)))
        d = s[0] - s[1]
        flag = True
        for j in range(1, len(s) - 1):
            if s[j] - s[j + 1] != d: flag = False
        if flag == True: sum += 1
    return sum

m=int(input())
print(sol(m))

