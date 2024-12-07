from tqdm import tqdm


def parse(calibration):
    test, nums = calibration.split(":")
    return int(test), [int(x) for x in nums.split()]


def build_tree(test, nums):
    if len(nums) == 1:
        return nums[0] == test
    
    root, operand, *others = nums

    if root > test:
        return False

    added = root + operand
    multiplied = root * operand
    return {
        root: {
            added: build_tree(test, [added] + others),
            multiplied: build_tree(test, [multiplied] + others),
            }
        }


def build_tree_(test, nums):
    if len(nums) == 1:
        return nums[0] == test
    
    root, operand, *others = nums

    if root > test:
        return False
    
    added = root + operand
    multiplied = root * operand
    concat = int(f"{root}{operand}")
    return {
        root: {
            added: build_tree_(test, [added] + others),
            multiplied: build_tree_(test, [multiplied] + others),
            concat: build_tree_(test, [concat] + others)
            }
        }


def search(tree):
    if isinstance(tree, bool):
        return tree

    return any(search(n) for n in tree.values())


with open("day07/data") as f:
    calibrations = f.read().splitlines()


total = 0
for calibration in tqdm(calibrations):
    test, nums = parse(calibration)
    tree = build_tree(test, nums)
    if search(tree):
        total += test
print(total)


total = 0
for calibration in tqdm(calibrations):
    test, nums = parse(calibration)
    tree = build_tree_(test, nums)
    if search(tree):
        total += test
print(total)