import math
n = int(input())  # 첫 줄: 개수 입력
a = list(map(int, input().split()))  # 두 번째 줄: 공백으로 구분된 숫자 입력


avg = math.floor(sum(a) / n + 0.5)
min_val = float('inf')

for idx, x in enumerate(a):
    absTmp = abs(x - avg)
    if absTmp < min_val:
        min_val = absTmp
        score = x
        res = idx + 1
    elif absTmp == min_val:
        if x > score:
            score = x
            res = idx + 1


print(avg, res)
