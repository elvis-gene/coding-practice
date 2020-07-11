class Solution:
    """
    Algorithm:

    When nums[j] equals to the given value, skip this element by incrementing j.
    As long as nums[j] != val, we copy nums[j] to nums[i] and increment both indexes at the same time.
    Repeat the process until jj reaches the end of the array and the new length is i.
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        newLength = 0
        length = len(nums)

        for i in range(length):
            if nums[i] != val:
                nums[newLength] = nums[i]
                newLength = newLength + 1

        return newLength
