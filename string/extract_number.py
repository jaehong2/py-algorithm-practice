"""
문제: 숫자만 추출
카테고리: 문자열
풀이: 문자열에서 숫자 추출 + 약수 개수 구하기

문자와 숫자가 섞인 문자열에서 숫자만 추출하여 자연수를 만들고,
그 자연수와 약수의 개수를 출력한다.
첫 자리 0은 자연수화할 때 무시한다.
추출하여 만들어지는 자연수는 1억을 넘지 않는다.

입력: 문자와 숫자가 섞인 문자열
출력: 첫 줄에 자연수, 다음 줄에 약수의 개수

입력예제:
t0e0a1c2h0er

출력예제:
120
16
"""

n = input()
result = ""
for c in n:
    if(c.isdecimal()):
        result += c
        
num = int(result)
print(num)
cnt = 0
for i in range(1, num+1):
    if num%i == 0:
        cnt+=1
print(cnt)