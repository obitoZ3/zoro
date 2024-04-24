def findPivotIndex(nums, left, right): 
    pivot = nums[right]
    position = left 
    for index in range(left, right):
        if nums[index] < pivot:
            temp = nums[position]
            nums[position] = nums[index]
            nums[index] = temp 
            position += 1 
 
    temp = nums[right]
    nums[right] = nums[position]
    nums[position] = temp 
    return position
 
 
def performQuickSort(nums, left, right):
    if left >= right:
        return 
    pivotIndex = findPivotIndex(nums, left, right)
    print(nums)
 
    performQuickSort(nums, left, pivotIndex - 1)
    performQuickSort(nums, pivotIndex + 1, right)
 
nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(nums)
print("Before sorting", nums)
 
performQuickSort(nums, 0, n - 1)
 
print("After sorting", nums)
