"""
문제: 사과나무 다이아몬드
카테고리: 배열
풀이: 다이아몬드 모양 범위 계산

N*N 격자판에서 다이아몬드 모양에 해당하는 사과만 수확한다.
N은 항상 홀수.

다이아몬드 조건:
- 중심에서 각 칸까지의 거리(행+열 절댓값)가 N//2 이하인 칸

입력: 첫 줄에 N(홀수), 다음 N줄에 N개의 정수
출력: 다이아몬드 범위 안의 사과 합계

입력예제:
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

출력예제:
379
"""

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

total_sum = 0
center = n // 2
for i in range(n):
    for j in range(abs(i - center), n - abs(i - center)):
        total_sum += a[i][j]
print(total_sum)

