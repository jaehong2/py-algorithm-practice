"""
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력

ex )
32를 뒤집으면 23, 23은 소수 23은 출력
910를 뒤집으면 19로 숫자화
첫 자리부터 연속된 0은 무시
def reverse 
def isPrime 를 반드시 작성 

입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 100,000을 넘지 않는다.

출력설명
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.
"""


n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0: 
        res = res * 10 + x % 10 
        x //= 10
    return res
    
def isPrime(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i ==0:
            return False
    return True

for x in a:
    r = reverse(x)
    if isPrime(r):
        print(r, end=" ")