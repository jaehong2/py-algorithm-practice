"""
문제: 두 리스트 합치기
카테고리: 정렬
풀이: 두 오름차순 리스트를 합쳐 오름차순으로 출력

이미 오름차순 정렬된 두 리스트를 합쳐 오름차순으로 출력한다.

입력: 첫 줄에 첫 번째 리스트 크기 N, 다음 줄에 N개의 정수
      다음 줄에 두 번째 리스트 크기 M, 다음 줄에 M개의 정수
출력: 합쳐진 오름차순 리스트를 한 줄에 출력

입력예제:
3
1 3 5
4
2 3 6 9

출력예제:
1 2 3 3 5 6 9
"""

n = int(input())
a=list(map(int, input().split()))
m = int(input())
b=list(map(int, input().split()))
p1=p2=0
c=[]

while p1 < n and p2 < m:
      if a[p1] <= b[p2]:
            c.append(a[p1])
            p1 += 1
      else:
            c.append(b[p2])
            p2 += 1

if p1 == n-1:
      c += b[p2:]

if p2 == m-1:
      c += a[p1:]

for i in range(c):
      print(i)