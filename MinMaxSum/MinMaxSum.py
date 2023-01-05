def sum_four(arr):
    firstArr, restArr = arr[0], arr[1:]
    tempFirstArr = None
    sumAllArr = []

    for _ in range(len(arr)):
        tempFirstArr = firstArr
        firstArr= restArr[0]
        restArr.append(tempFirstArr)
        restArr = restArr[1:]
        sumAllArr.append(sum(restArr))

    sumAllArr = sorted(sumAllArr)

    print(sumAllArr)

sum_four([1,2,3,4,5])

	# sort.Slice(sumAllArr, func(i, j int) bool { return sumAllArr[i] < sumAllArr[j] })

	# fmt.Println(sumAllArr[0], sumAllArr[len(arr)-1])

	# return sumAllArr
