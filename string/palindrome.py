"""
문제: 회문 문자열 검사
카테고리: 문자열
풀이: 앞뒤 비교 (대소문자 무시)

N개의 문자열을 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같으면 YES,
아니면 NO를 출력한다. 대소문자는 구분하지 않는다.

입력: 첫 줄에 N(1<=N<=20), 다음 N줄에 단어 (길이 100 이하)
출력: 각 단어에 대해 YES 또는 NO

입력예제:
5
level
moon
abcba
soon
gooG

출력예제:
YES
NO
YES
NO
YES
"""
n = int(input())
results = []
for _ in range(n):           
    s = input().lower()        
    is_palin = True            
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            is_palin = False
            break              # 하나라도 다르면 즉시 종료
    if is_palin:
        results.append("YES")
    else:
        results.append("NO")

for r in results:
    print(r)

# results = []
# for i in range(n):
#     s = input().lower()
#     if s == s[::-1]:
#         results.append("YES")
#     else:
#         results.append("NO")

# for r in results:
#     print(r)
    
    