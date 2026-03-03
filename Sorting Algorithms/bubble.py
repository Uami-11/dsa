def bubble_sort(nums):
    hasSwapped = True;
    end = len(nums);
    while (hasSwapped):
        hasSwapped = False;
        
        for i in range(1, end):
            if (nums[i - 1] > nums[i]):
                temp = nums[i - 1];
                nums[i - 1] = nums[i];
                nums[i] = temp;

                hasSwapped = True;
        end -= 1;

    return nums