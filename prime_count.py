""" 
title: 소수의 갯수

content : 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
만약 20이 입력되면, 1부터 20까지의 소수는 2,3,5,7,11,13,17,19로 총 8개 입니다.
제한시간은 1초입니다.

입력
첫 번째 줄에는 개수 N(2<=N<=200000)이 주어집니다.

출력
첫 줄에 소수의 개수를 출력합니다.

입력예제 1
20

출력예제 1
8
"""
"""
내가 낸 푼 문제방식
- 시간복잡도 O(N^2) 라서 N=200000에선 1초 제한을 못넘음.
a = int(input())
cnt = 0

for x in range(2, a+1):
    for y in range(2, a+1):
        if (x == y):
            cnt += 1
        if(x % y == 0):
            break
                

print(cnt)
"""
# 소수 여부를 저장하는 리스트 (True: 소수로 가정)
# 0과 1은 소수가 아님
def count_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return sum(is_prime)


N = int(input())
print(count_primes(N))