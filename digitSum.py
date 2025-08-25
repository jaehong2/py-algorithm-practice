""" 
title: 자릿수의 합

content : N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요.

입력
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.

출력
자릿수의 합이 최대인 자연수를 출력한다.

입력예제 1
3
25 15232 97

출력예제 1
97
"""
n = int(input())
a = list(map(int, (input().split())))

def digit_sum(x):
    sum=0
    while x>0:
        sum += x%10
        x/=10
    return sum

max = -float('inf')

for idx, x in enumerate(a):
    tot = digit_sum(x)
    if (tot > max):
        max = tot
        res=x

print(res)