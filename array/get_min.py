"""
문제: 배열 최솟값 구하기
카테고리: 배열
풀이: 배열을 순회하며 최솟값을 갱신
"""
arr=[5, 3, 7, 6, 10]
arrMin=float('inf')
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)
