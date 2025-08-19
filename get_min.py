arr=[5, 3, 7, 6, 10]
arrMin=float('inf')
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)