def find_uniq(arr):
    # your code here
    print('govno')
    if (arr[0] == arr[1])+(arr[0] == arr[5]):
        repeated = arr[0]
    else:
        repeated = arr[1]
    # while repeated in arr:
    #     arr.remove(repeated)
    for i in range(0,len(arr)):
        if arr[i] != repeated:
            return arr[i]
    return 0   # n: unique number in the array
print(find_uniq([1, 2, 2]))