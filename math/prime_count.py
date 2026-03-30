"""
문제: 소수의 개수
카테고리: 수학
풀이: 에라토스테네스의 체 (시간복잡도 O(N log log N))

자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
제한시간은 1초입니다.

입력: 첫 번째 줄에 개수 N(2<=N<=200000)
출력: 소수의 개수

입력예제: 20
출력예제: 8
"""
"""
처음 풀이 - 시간복잡도 O(N^2)라서 N=200000에선 1초 제한을 못넘음.
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
