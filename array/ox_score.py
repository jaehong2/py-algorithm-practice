"""
문제: OX 퀴즈 점수 계산
카테고리: 배열
풀이: 연속 정답 카운트

OX 문제 시험에서 연속으로 맞히면 가산점을 준다.

규칙:
- 맞으면(1): 연속 정답 수만큼 점수 (1점, 2점, 3점, ...)
- 틀리면(0): 0점, 연속 카운트 초기화

예시:
1 0 1 1 1 0 0 1 1 0
→ 점수: 1 0 1 2 3 0 0 1 2 0
→ 총점: 10

입력: 첫 줄에 N, 다음 줄에 N개의 0 또는 1
출력: 총 점수
"""

n = int(input())
a = list(map(int, input().split()))

sum = 0
continueCount = 0
for i in a:
    if (i==1):
        continueCount += 1
        sum += continueCount
    else:
        continueCount = 0

print(sum)