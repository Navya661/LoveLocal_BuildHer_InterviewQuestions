from collections import deque

def maxSlidingWindow(nums, k):
    """
    Finds the maximum elements in a sliding window of size k in an array.

    Args:
    - nums: The input array of integers.
    - k: The size of the sliding window.

    Returns:
    - List[int]: A list containing the maximum elements in each sliding window.
    """
    if not nums or k == 0:
        return []

    result = []  # to store the maximum elements in each sliding window
    window = deque()  # deque to store indices of elements in the current window

    for i in range(len(nums)):
        # Remove elements outside the current window from the front of the deque
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove elements smaller than the current element from the back of the deque
        while window and nums[i] > nums[window[-1]]:
            window.pop()

        # Add the current index to the deque
        window.append(i)

        # Add the maximum element in the current window to the result
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Example usage:
nums1 = [1]
k1 = 1
print(maxSlidingWindow(nums1, k1))  # Output: [1]

nums2 = [1, 3, -1, -3, 5, 3, 6, 7]
k2 = 3
print(maxSlidingWindow(nums2, k2))  # Output: [3, 3, 5, 5, 6, 7]
