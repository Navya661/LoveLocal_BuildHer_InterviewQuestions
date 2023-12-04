def majorityElement(nums):
    """
    Finds all elements that appear more than ⌊ n/3 ⌋ times in an integer array.

    Args:
    - nums: The input integer array.

    Returns:
    - List[int]: A list of elements that satisfy the condition.
    """
    if not nums:
        return []

    # Initialize candidates and counters
    candidate1, count1 = None, 0
    candidate2, count2 = None, 0

    # Voting process
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Count occurrences of the candidates
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    # Check if candidates appear more than ⌊ n/3 ⌋ times
    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result

# Example usage:
nums1 = [3, 2, 3]
print(majorityElement(nums1))  # Output: [3]

nums2 = [1]
print(majorityElement(nums2))  # Output: [1]

nums3 = [1, 2]
print(majorityElement(nums3))  # Output: [1, 2]
