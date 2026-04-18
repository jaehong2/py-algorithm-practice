"""
문제: 수들의 합
카테고리: 투포인터
풀이: 두 포인터로 연속된 구간의 합을 조절

N개의 수로 이루어진 수열에서 연속된 수들의 합이 S가 되는 경우의 수를 구한다.

투포인터:
- 합이 S보다 작으면 오른쪽 포인터를 늘려 범위 확장
- 합이 S보다 크면 왼쪽 포인터를 늘려 범위 축소
- 합이 S와 같으면 카운트 증가

입력: 첫 줄에 N(1<=N<=10,000)과 S(1<=S<=100,000,000)
      둘째 줄에 N개의 자연수 (각 자연수는 10,000 이하)
출력: 합이 S가 되는 연속 부분 수열의 개수

입력예제:
5 5
1 2 3 4 2

출력예제:
1
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0 

while True:
      if tot < m:
            if rt < n:
                  tot+=a[rt]
                  rt+=1
            else:
                  break
            
      elif tot == m:
            cnt+=1
            tot-=a[lt]
            lt+=1
            
      else:
            tot-=a[lt]
            lt+=1

print(cnt)