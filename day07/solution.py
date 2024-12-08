from operator import add, mul


def parse(calibration):
    test, nums = calibration.split(":")
    return int(test), [int(x) for x in nums.split()]


def search(test, nums, ops):
    if len(nums) == 1:
        return nums[0] == test
    
    x, y, *others = nums

    if x > test:
        return False

    res = [op(x, y) for op in ops]
    return any(search(test, [r] + others, ops) for r in res)


def concat(x, y):
    return int(f"{x}{y}")


with open("day07/data") as f:
    calibrations = [parse(l) for l in f.read().splitlines()]


# ==== PART 1 ====
print(sum(test for test, nums in calibrations if search(test, nums, (add, mul))))

# ==== PART 2 ====
print(sum(test for test, nums in calibrations if search(test, nums, (add, mul, concat))))
