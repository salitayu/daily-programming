def find_max_sliding_window(nums, window, size):
    if len(nums) == 0:
        return 0
    result = []
    window = []
    for i in range(0, len(nums)):
        current = nums[i]
        window.append(current)
        if len(window) == size:
            result.append(max(window))
            window.pop(0)
    return result