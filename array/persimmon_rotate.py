"""
문제: 곳감 (행 회전 + 모래시계 합)
카테고리: 배열
풀이: 행 회전 후 모래시계 합 구하기

N*N 격자판에서 M개의 회전 명령을 수행한 후,
모래시계 모양의 합을 출력한다.

회전 명령: [행번호 방향 회전수]
- 방향 0: 왼쪽 회전
- 방향 1: 오른쪽 회전

모래시계 모양 (3칸 기준):
* * *
  *
* * *

입력: 첫 줄에 N(홀수, 3<=N<=50)
      다음 N줄에 N개의 정수 (1~9)
      다음 줄에 명령 수 M
      다음 M줄에 회전 명령 [행번호 방향 회전수]
출력: 모래시계 합
"""

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

m = int(input())
commands = []
for i in range(m):
    commands.append(list(map(int, input().split())))

for cmd in commands:
    row, direction, cnt = cmd
    row -= 1
    cnt %= n

    if direction == 0:
        a[row] = a[row][cnt:] + a[row][:cnt]
    else:
        a[row] = a[row][-cnt:] + a[row][:-cnt]

center = n // 2
total = 0
for i in range(n):
    dist = abs(i - center)
    total += sum(a[i][center - dist:center + dist + 1])

print(total)
