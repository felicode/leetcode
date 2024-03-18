# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.


#---- 1st approach


class Solution(object):
    def removeElement(self, nums, val):
        k = len(nums)

        while val in nums:
            nums.remove(val)
        return k


#-----2n approach


def removeElement(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i

#---test cases

nums = [1, 2, 3, 4, 5]
val = int(5)

result = removeElement(nums, val)

# solution_instance = Solution()
# result = solution_instance.removeElement(nums, val)

print(result)


