"""
문제: 스도쿠 검사
카테고리: 배열
풀이: 행, 열, 3×3 박스 각각 1~9 포함 여부 확인

9×9 스도쿠 판이 올바르게 채워졌는지 확인한다.
각 행, 각 열, 각 3×3 박스에 1~9가 정확히 한 번씩 있으면 YES, 아니면 NO.

입력: 9줄에 걸쳐 9개의 숫자 (1~9)
출력: YES 또는 NO

입력예제:
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
2 3 4 5 6 7 8 9 1
5 6 7 8 9 1 2 3 4
8 9 1 2 3 4 5 6 7
3 4 5 6 7 8 9 1 2
6 7 8 9 1 2 3 4 5
9 1 2 3 4 5 6 7 8

출력예제:
YES
"""

a = [list(map(int, input().split())) for _ in range(9)]


ch3 = [0] * 10
result = ''

for i in range(9):
    ch1 = [0] * 10
    ch2 = [0] * 10
    for j in range(9):
        ch1[a[i][j]] = 1
        ch2[a[j][i]] = 1
    if sum(ch1) != 9 or sum(ch2) != 9:
        result = 'NO'

for i in range(3):
    for j in range(3):
        ch3 = [0] * 10
        for x in range(3):
            for y in range(3):
                ch3[a[i*3 + x][j*3 + y]] = 1
        if sum(ch3) != 9:
            result = 'NO'

if result == '':
    result = 'YES'
print(result)
    
    
    
    

