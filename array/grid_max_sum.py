"""
문제: 격자판 최대합
카테고리: 배열
풀이: 각 행, 열, 대각선의 합 중 최대값 구하기

N*N 격자판에서 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력한다.

입력: 첫 줄에 N(2<=N<=50)
      다음 N줄에 걸쳐 N개의 자연수 (각 자연수는 100 이하)
출력: 최대합을 출력

입력예제:
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

출력예제:
155
"""


n = int(input())
a = []

for i in range(n):
      a.append(list(map(int, input().split())))

max_val = 0

for i in range(n):
      sum = 0
      for j in range(n):
            sum += a[i][j]
      max_val = max(max_val, sum)
      
for i in range(n):
      sum = 0
      for j in range(n):
            sum += a[j][i]
      max_val = max(max_val, sum)
      

sum = 0
for i in range(n):
      sum += a[i][i]
max_val = max(max_val, sum)
      
sum = 0
for i in range(n):
      sum += a[i][n-1-i]
max_val = max(max_val, sum)      
      
print(max_val)