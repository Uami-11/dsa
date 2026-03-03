def merge_sort(nums):
    if (len(nums) < 2):
        return nums;
    middle = len(nums) // 2;
    left = nums[:middle]
    right = nums[middle:]
    
    sorted_left_side = merge_sort(left);
    sorted_right_side = merge_sort(right);
    
    return merge(sorted_left_side, sorted_right_side);


def merge(first, second):
    final = [];
    i = 0;
    j = 0;
    maxi = len(first);
    maxj = len(second);
    while (i < maxi and j < maxj):
        if (first[i] <= second[j]):
            final.append(first[i]);
            i += 1;
        elif (second[j] < first[i]):
            final.append(second[j]);
            j += 1;
            

    while (i < maxi):
        final.append(first[i]);
        i += 1;

    while (j < maxj):
        final.append(second[j]);
        j += 1;
    
    return final;