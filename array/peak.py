"""
문제: 봉우리
카테고리: 배열
풀이: 상하좌우 이웃보다 큰 칸 개수 세기

N*N 격자판에서 상하좌우 4방향 이웃보다 모두 큰 칸을 봉우리라 한다.
봉우리의 개수를 출력한다.
격자판 밖은 0으로 간주한다.

입력: 첫 줄에 N(2<=N<=50)
      다음 N줄에 N개의 자연수 (각 자연수는 100 이하)
출력: 봉우리의 개수

입력예제:
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2

출력예제:
10
"""
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

peak_count = 0
for i in range(n):
    for j in range(n):
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < n and 0 <= nj < n:
                if a[i][j] <= a[ni][nj]:
                    break
        else:
            peak_count += 1
            
print(peak_count)
            