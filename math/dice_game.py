"""
문제: 주사위 게임
카테고리: 수학
풀이: 조건 분기

1~6 눈을 가진 주사위 3개를 던져 상금을 계산한다.

규칙1) 같은 눈 3개 → 10,000 + (같은 눈) * 1,000원
규칙2) 같은 눈 2개 → 1,000 + (같은 눈) * 100원
규칙3) 모두 다른 눈 → (가장 큰 눈) * 100원

N명이 참여할 때, 가장 많은 상금을 받은 사람의 상금을 출력

입력: 첫 줄에 N(2<=N<=1,000), 다음 N줄에 주사위 3개의 눈
출력: 가장 많은 상금

입력예제:
3
3 3 6
2 2 2
6 2 5

출력예제:
12000
"""
maxResult = 0
n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        money = 10000 + 1000 * a
    elif a == b or a == c:
        money = 1000 + 100 * a
    elif b == c:
        money = 1000 + 100 * b
    else:
        money = 100 * max(a, b, c)
    if money > maxResult:
        maxResult = money

print(maxResult)
        
    

