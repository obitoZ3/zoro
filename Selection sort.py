def performSelectionSort(nums):
    n = len(nums)
    for fixThisIndex in range(n - 1, 0, -1):
        maxEle = nums[fixThisIndex]
        maxEleIndex = fixThisIndex 
 
        for index in range(fixThisIndex):
            if nums[index] > maxEle:
                maxEleIndex = index 
                maxEle = nums[index]
        if fixThisIndex != maxEleIndex:
            temp = nums[maxEleIndex]
            nums[maxEleIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp
 
        print(nums)
 
nums = [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
 
print("Before sorting:")
print(nums)
 
performSelectionSort(nums)
 
print("After sorting:")
print(nums)
 
 