#A=O(1) Accessing the first element of a list takes constant time because no looping or scanning is required#
#B=O(n) The function checks every element once, so its runtime grows linearly with the size of the list.#
#C=O(n^2) It uses two nested loops over the list, generating n × n pairs.#
#D=O(log n) The loop repeatedly halves n, so the number of iterations grows logarithmically.#
#E=O(n log n) The sorting step dominates the runtime because sum is O(n) and indexing is O(1), but sorted is O(n log n).#

def count_pairs_quadratic(nums, target):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j]==target:
                count +=1
                return count

def count_pairs_linear(nums, target):
    seen={}
    count= 0
    for num in nums:
        complement=target-num
        if complement in seen:
            count+= seen[complement]
            seen[num] = seen.get(num, 0) + 1
            return count


import time
import random

def benchmark(func, nums, target):
    start = time.time()
    result = func(nums, target)
    end = time.time()
    return end - start

sizes = [1000, 5000, 10000]
target = 100

for size in sizes:
    nums = [random.randint(0, 100) for _ in range(size)]
    random.shuffle(nums)

    t1 = benchmark(count_pairs_quadratic, nums, target)
    t2 = benchmark(count_pairs_linear, nums, target)

    print(f"n={size:>6}  |  O(n^2): {t1:.4f}s  |  O(n): {t2:.4f}s")       






