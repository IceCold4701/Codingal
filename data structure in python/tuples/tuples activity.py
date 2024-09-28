def multiple_tuple(nums):
    temp=list(nums)
    product=1
    for x in temp:
        product *= x
    return product
nums=(4, 3, 2, 2, -1, 18)
print("Original Tuple:")
print(nums)
print(" Product - multiplying all the said numbers of the tuple:",multiple_tuple(nums))
nums=(2, 4, 8, 8, 3, 2, 9)
print("\nOriginal Tuple:")
print(nums)
print("Product - multiplying all the said numbers of the tuple:",multiple_tuple(nums))