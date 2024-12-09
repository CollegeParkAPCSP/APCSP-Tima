def filter_even_numbers(nums):
    res = []
    for i in nums:
        if i % 2 == 0:
            res.append(i)
    return res
            
def triangle_sum(nums):
    res = []
    for i in range(len(nums)):
        res.append(sum(nums[:i+1]))
    return res

def remove_duplicates(nums):
    res = []
    for i in nums:
        if i not in res:
            res.append(i)
    return res