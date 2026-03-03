def insertion_sort(nums):
    end = len(nums);
    for i in range(1, end):
        j = i;
        while (j > 0 and (nums[j - 1] > nums[j])):
            temp = nums[j];
            nums[j] = nums[j - 1]
            nums[j - 1] = temp;
            j -= 1;
        
    return nums;
        
