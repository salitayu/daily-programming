def sortColors(nums):
    start = 0
    end = len(nums) - 1
    pivot = 1
    mid = 0
    while mid <= end:
        if nums[mid] < pivot:
            nums[mid], nums[start] = nums[start], nums[mid]
            start += 1
            mid += 1
        elif nums[mid] > pivot:
            nums[mid], nums[end] = nums[end], nums[mid]
            end -= 1
        else:
            mid += 1
    return nums
def sortColors1(colors):
    red, white, blue = 0, 0, len(colors) - 1
    while white <= blue:
        if colors[white] == 0:
            if colors[red] != 0:
                colors[red], colors[white] = colors[white], colors[red]
            white += 1
            red += 1
        elif colors[white] == 1:
            white += 1
        else:
            if colors[blue] != 2:
                colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1
    return colors