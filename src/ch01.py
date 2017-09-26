def exp1(count):
    """Appending list"""
    nums = []
    for i in range(count):
        nums.append(i)
    return nums

def exp2(count):
    """Much slower than exp1"""
    nums = []
    for i in range(count):
        nums.insert(0, i)
    return nums
