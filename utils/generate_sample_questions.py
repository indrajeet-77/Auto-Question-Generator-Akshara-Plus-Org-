import pandas as pd
import os


def generate_sample_questions():
    """Generate a comprehensive CSV with 400+ data structure questions"""

    # Ensure the data directory exists
    os.makedirs("data", exist_ok=True)

    questions = []
    question_id = 1

    # Arrays - Level 1 (Beginner) 
    array_beginner = [
        {
            "question": "Given an array [VALUES], what is the element at index 2?",
            "answer": "The element at index 2 is [VALUE]. Remember that array indexing starts at 0 in most programming languages.",
        },
        {
            "question": "What is the length of the array [VALUES]?",
            "answer": "The length of the array is [LENGTH].",
        },
        {
            "question": "Find the sum of all elements in the array [VALUES].",
            "answer": "The sum of all elements is [SUM].",
        },
        {
            "question": "Find the largest element in the array [VALUES].",
            "answer": "The largest element in the array is [MAX].",
        },
        {
            "question": "Find the smallest element in the array [VALUES].",
            "answer": "The smallest element in the array is [MIN].",
        },
        {
            "question": "If we reverse the array [VALUES], what would be the result?",
            "answer": "The reversed array would be [REVERSED].",
        },
        {
            "question": "Given the array [VALUES], what would be the result after sorting in ascending order?",
            "answer": "The sorted array would be [SORTED].",
        },
        {
            "question": "Given the array [VALUES], calculate the average of all elements.",
            "answer": "The average of all elements is [AVERAGE].",
        },
        {
            "question": "In the array [VALUES], how many elements are greater than 50?",
            "answer": "Count each element greater than 50 to get the answer.",
        },
        {
            "question": "If we add 10 to each element in the array [VALUES], what would be the result?",
            "answer": "Add 10 to each element: the result would be a new array with each element increased by 10.",
        },
        {
            "question": "Find the first occurrence of the maximum element in array [VALUES].",
            "answer": "The first occurrence of the maximum element [MAX] is at index [MAX_INDEX].",
        },
        {
            "question": "Given array [VALUES], find all even numbers.",
            "answer": "The even numbers in the array are: [EVEN_NUMBERS].",
        },
        {
            "question": "What is the product of the first three elements in array [VALUES]?",
            "answer": "The product of the first three elements is [PRODUCT_FIRST_THREE].",
        },
        {
            "question": "Given array [VALUES], count how many elements are odd.",
            "answer": "Count each odd element to get the total number of odd elements.",
        },
        {
            "question": "Find the difference between the maximum and minimum elements in array [VALUES].",
            "answer": "The difference between max ([MAX]) and min ([MIN]) is [DIFFERENCE].",
        },
        {
            "question": "Given array [VALUES], what is the sum of the first five elements?",
            "answer": "Sum the first five elements of the array to get [SUM_FIRST_FIVE].",
        },
        {
            "question": "Given array [VALUES], what is the last element?",
            "answer": "The last element is [LAST_ELEMENT].",
        },
        {
            "question": "Given array [VALUES], what is the index of the minimum element?",
            "answer": "The index of the minimum element [MIN] is [MIN_INDEX].",
        },
        {
            "question": "Given array [VALUES], what is the result if you remove the first element?",
            "answer": "Remove the first element to get [WITHOUT_FIRST].",
        },
        {
            "question": "Given array [VALUES], what is the result if you remove the last element?",
            "answer": "Remove the last element to get [WITHOUT_LAST].",
        },
        {
            "question": "Given array [VALUES], what is the sum of all even elements?",
            "answer": "Sum all even elements in the array to get [SUM_EVEN].",
        },
        {
            "question": "Given array [VALUES], what is the sum of all odd elements?",
            "answer": "Sum all odd elements in the array to get [SUM_ODD].",
        },
        {
            "question": "Given array [VALUES], what is the average of the first three elements?",
            "answer": "The average of the first three elements is [AVG_FIRST_THREE].",
        },
        {
            "question": "Given array [VALUES], what is the median value?",
            "answer": "Sort the array and find the middle value(s): [MEDIAN].",
        },
        {
            "question": "Given array [VALUES], what is the mode (most frequent element)?",
            "answer": "The mode of the array is [MODE].",
        },
        {
            "question": "Given array [VALUES], what is the result after doubling each element?",
            "answer": "Double each element to get [DOUBLED].",
        },
        {
            "question": "Given array [VALUES], what is the result after squaring each element?",
            "answer": "Square each element to get [SQUARED].",
        },
        {
            "question": "Given array [VALUES], what is the sum of elements at even indices?",
            "answer": "Sum elements at indices 0, 2, 4, ... to get [SUM_EVEN_INDICES].",
        },
        {
            "question": "Given array [VALUES], what is the sum of elements at odd indices?",
            "answer": "Sum elements at indices 1, 3, 5, ... to get [SUM_ODD_INDICES].",
        },
        {
            "question": "Given array [VALUES], what is the maximum difference between any two elements?",
            "answer": "The maximum difference is [MAX_DIFF].",
        },
        {
            "question": "Given array [VALUES], what is the minimum positive element?",
            "answer": "The minimum positive element is [MIN_POSITIVE].",
        },
        {
            "question": "Given array [VALUES], what is the result after removing all negative numbers?",
            "answer": "Remove all negative numbers to get [NO_NEGATIVES].",
        },
        {
            "question": "Given array [VALUES], what is the result after removing all zeros?",
            "answer": "Remove all zeros to get [NO_ZEROS].",
        },
        {
            "question": "Given array [VALUES], what is the sum of the largest and smallest elements?",
            "answer": "Sum the largest ([MAX]) and smallest ([MIN]) elements to get [SUM_MAX_MIN].",
        },
        {
            "question": "Given array [VALUES], what is the result after inserting 100 at index 1?",
            "answer": "Insert 100 at index 1 to get [INSERTED_100].",
        },
        {
            "question": "Given array [VALUES], what is the result after removing the element at index 3?",
            "answer": "Remove the element at index 3 to get [REMOVED_INDEX_3].",
        },
        {
            "question": "Given array [VALUES], what is the sum of elements between indices 2 and 5 (inclusive)?",
            "answer": "Sum elements from index 2 to 5 to get [SUM_2_5].",
        },
        {
            "question": "Given array [VALUES], what is the result after sorting in descending order?",
            "answer": "Sort the array in descending order to get [SORTED_DESC].",
        },
        {
            "question": "Given array [VALUES], what is the result after rotating left by 1 position?",
            "answer": "Rotate left by 1 to get [ROTATED_LEFT_1].",
        },
        {
            "question": "Given array [VALUES], what is the result after rotating right by 1 position?",
            "answer": "Rotate right by 1 to get [ROTATED_RIGHT_1].",
        },
        {
            "question": "Given array [VALUES], what is the sum of the first and last elements?",
            "answer": "Sum the first ([FIRST_ELEMENT]) and last ([LAST_ELEMENT]) elements to get [SUM_FIRST_LAST].",
        },
        {
            "question": "Given array [VALUES], what is the result after removing all duplicate elements?",
            "answer": "Remove duplicates to get [NO_DUPLICATES].",
        },
        {
            "question": "Given array [VALUES], what is the result after reversing only the first three elements?",
            "answer": "Reverse the first three elements to get [REVERSED_FIRST_THREE].",
        },
        {
            "question": "Given array [VALUES], what is the result after swapping the first and last elements?",
            "answer": "Swap first and last elements to get [SWAPPED_FIRST_LAST].",
        },
        {
            "question": "Given array [VALUES], what is the result after multiplying each element by its index?",
            "answer": "Multiply each element by its index to get [MULTIPLIED_BY_INDEX].",
        },
        {
            "question": "Given array [VALUES], what is the result after removing all elements greater than 50?",
            "answer": "Remove all elements greater than 50 to get [NO_GREATER_50].",
        },
    ]

    # Arrays - Level 2 (Intermediate) - 
    array_intermediate = [
        {
            "question": "Given the array [VALUES], find the indices of all elements that are even numbers.",
            "answer": "Iterate through the array and collect indices where arr[i] % 2 == 0.",
        },
        {
            "question": "In the array [VALUES], find the second largest element.",
            "answer": "Sort the array or use two variables to track largest and second largest: [SECOND_MAX].",
        },
        {
            "question": "Given the array [VALUES], find the product of all elements.",
            "answer": "Multiply all elements together: [PRODUCT].",
        },
        {
            "question": "In the array [VALUES], calculate the running sum (cumulative sum).",
            "answer": "Create a new array where each element is the sum of all previous elements including current.",
        },
        {
            "question": "Given the array [VALUES], find the median value.",
            "answer": "Sort the array and find the middle element(s): [MEDIAN].",
        },
        {
            "question": "In the array [VALUES], find all pairs of elements that sum to 100.",
            "answer": "Use nested loops or hash map to find pairs (i,j) where arr[i] + arr[j] = 100.",
        },
        {
            "question": "Given the array [VALUES], rotate it to the right by 2 positions.",
            "answer": "Move elements: last 2 elements move to front, others shift right.",
        },
        {
            "question": "In the array [VALUES], find the majority element (appears more than n/2 times).",
            "answer": "Use Boyer-Moore algorithm or count frequencies to find element appearing > n/2 times.",
        },
        {
            "question": "Given the array [VALUES], remove all duplicates and return the new array.",
            "answer": "Use a set or hash map to track seen elements and build new array.",
        },
        {
            "question": "In the array [VALUES], find the longest sequence of consecutive increasing numbers.",
            "answer": "Iterate and track current sequence length, update maximum when sequence breaks.",
        },
        {
            "question": "Given array [VALUES], find the subarray with maximum sum using Kadane's algorithm.",
            "answer": "Use dynamic programming: track current_sum and max_sum, reset current_sum when negative.",
        },
        {
            "question": "In array [VALUES], find the missing number if it contains n-1 distinct numbers from 1 to n.",
            "answer": "Use sum formula: expected_sum - actual_sum = missing number.",
        },
        {
            "question": "Given array [VALUES], implement binary search to find target element 50.",
            "answer": "Sort array first, then use divide and conquer: compare middle with target.",
        },
        {
            "question": "In array [VALUES], find the peak element (greater than its neighbors).",
            "answer": "Check each element with its neighbors, or use binary search approach.",
        },
        {
            "question": "Given array [VALUES], merge it with another sorted array efficiently.",
            "answer": "Use two pointers technique to merge in O(n+m) time.",
        },
        {
            "question": "Given the array [VALUES], find the minimum difference between any two elements.",
            "answer": "Sort the array and find the minimum difference between consecutive elements: [MIN_DIFF].",
        },
        {
            "question": "Given the array [VALUES], find the longest subarray with all unique elements.",
            "answer": "Use a sliding window to track the longest subarray with unique elements: [LONGEST_UNIQUE].",
        },
        {
            "question": "Given the array [VALUES], find the number of inversions (i < j and arr[i] > arr[j]).",
            "answer": "Count all pairs (i, j) where i < j and arr[i] > arr[j]: [INVERSION_COUNT].",
        },
        {
            "question": "Given the array [VALUES], find the kth smallest element.",
            "answer": "Sort the array or use a min-heap to find the kth smallest element: [KTH_SMALLEST].",
        },
        {
            "question": "Given the array [VALUES], find the maximum product of any two elements.",
            "answer": "Find the two largest and two smallest elements, return the maximum product: [MAX_PRODUCT].",
        },
    ]

    # Arrays - Level 3 (Advanced) -
    array_advanced = [
        {
            "question": "Given the array [VALUES], implement the Kadane's algorithm to find the maximum subarray sum.",
            "answer": "```python\ndef kadane(arr):\n    max_sum = current_sum = arr[0]\n    for i in range(1, len(arr)):\n        current_sum = max(arr[i], current_sum + arr[i])\n        max_sum = max(max_sum, current_sum)\n    return max_sum```",
        },
        {
            "question": "Given the array [VALUES], find all triplets that sum to zero using 3Sum algorithm.",
            "answer": "```python\ndef three_sum(arr):\n    arr.sort()\n    result = []\n    for i in range(len(arr)-2):\n        if i > 0 and arr[i] == arr[i-1]: continue\n        left, right = i+1, len(arr)-1\n        while left < right:\n            total = arr[i] + arr[left] + arr[right]\n            if total == 0:\n                result.append([arr[i], arr[left], arr[right]])\n                left += 1\n                right -= 1\n            elif total < 0: left += 1\n            else: right -= 1\n    return result```",
        },
        {
            "question": "In the array [VALUES], find the longest bitonic subarray (increases then decreases).",
            "answer": "```python\ndef longest_bitonic(arr):\n    n = len(arr)\n    inc = [1] * n  # increasing lengths\n    dec = [1] * n  # decreasing lengths\n    \n    for i in range(1, n):\n        if arr[i] > arr[i-1]:\n            inc[i] = inc[i-1] + 1\n    \n    for i in range(n-2, -1, -1):\n        if arr[i] > arr[i+1]:\n            dec[i] = dec[i+1] + 1\n    \n    return max(inc[i] + dec[i] - 1 for i in range(n))```",
        },
        {
            "question": "Given the array [VALUES], find the equilibrium index where left sum equals right sum.",
            "answer": "```python\ndef equilibrium_index(arr):\n    total_sum = sum(arr)\n    left_sum = 0\n    for i in range(len(arr)):\n        if left_sum == total_sum - left_sum - arr[i]:\n            return i\n        left_sum += arr[i]\n    return -1```",
        },
        {
            "question": "In the array [VALUES], find minimum jumps to reach end where each element is max jump length.",
            "answer": "```python\ndef min_jumps(arr):\n    if len(arr) <= 1: return 0\n    if arr[0] == 0: return -1\n    \n    jumps = 1\n    max_reach = arr[0]\n    steps = arr[0]\n    \n    for i in range(1, len(arr)):\n        if i == len(arr) - 1: return jumps\n        max_reach = max(max_reach, i + arr[i])\n        steps -= 1\n        if steps == 0:\n            jumps += 1\n            if i >= max_reach: return -1\n            steps = max_reach - i\n    return -1```",
        },
        {
            "question": "Given the array [VALUES], rearrange it so that arr[i] becomes arr[arr[i]] with O(1) space.",
            "answer": "```python\ndef rearrange(arr):\n    n = len(arr)\n    for i in range(n):\n        arr[i] += (arr[arr[i]] % n) * n\n    for i in range(n):\n        arr[i] //= n```",
        },
        {
            "question": "In array [VALUES], find maximum difference between elements where larger comes after smaller.",
            "answer": "```python\ndef max_difference(arr):\n    min_element = arr[0]\n    max_diff = arr[1] - arr[0]\n    for i in range(1, len(arr)):\n        max_diff = max(max_diff, arr[i] - min_element)\n        min_element = min(min_element, arr[i])\n    return max_diff```",
        },
        {
            "question": "Given array [VALUES], implement Dutch National Flag algorithm for 0s, 1s, 2s.",
            "answer": "```python\ndef dutch_flag(arr):\n    low = mid = 0\n    high = len(arr) - 1\n    while mid <= high:\n        if arr[mid] == 0:\n            arr[low], arr[mid] = arr[mid], arr[low]\n            low += 1\n            mid += 1\n        elif arr[mid] == 1:\n            mid += 1\n        else:\n            arr[mid], arr[high] = arr[high], arr[mid]\n            high -= 1```",
        },
        {
            "question": "In array [VALUES], find the smallest positive missing number.",
            "answer": "```python\ndef first_missing_positive(arr):\n    n = len(arr)\n    for i in range(n):\n        while 1 <= arr[i] <= n and arr[arr[i]-1] != arr[i]:\n            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]\n    \n    for i in range(n):\n        if arr[i] != i + 1:\n            return i + 1\n    return n + 1```",
        },
        {
            "question": "Given array [VALUES], find maximum product subarray.",
            "answer": "```python\ndef max_product_subarray(arr):\n    max_prod = min_prod = result = arr[0]\n    for i in range(1, len(arr)):\n        if arr[i] < 0:\n            max_prod, min_prod = min_prod, max_prod\n        max_prod = max(arr[i], max_prod * arr[i])\n        min_prod = min(arr[i], min_prod * arr[i])\n        result = max(result, max_prod)\n    return result```",
        },
        {
            "question": "Implement sliding window maximum for array [VALUES] with window size 3.",
            "answer": "```python\nfrom collections import deque\ndef sliding_window_max(arr, k):\n    dq = deque()\n    result = []\n    for i in range(len(arr)):\n        while dq and dq[0] <= i - k:\n            dq.popleft()\n        while dq and arr[dq[-1]] <= arr[i]:\n            dq.pop()\n        dq.append(i)\n        if i >= k - 1:\n            result.append(arr[dq[0]])\n    return result```",
        },
        {
            "question": "Given array [VALUES], find longest increasing subsequence length.",
            "answer": "```python\ndef lis_length(arr):\n    from bisect import bisect_left\n    tails = []\n    for num in arr:\n        pos = bisect_left(tails, num)\n        if pos == len(tails):\n            tails.append(num)\n        else:\n            tails[pos] = num\n    return len(tails)```",
        },
        {
            "question": "Implement merge sort for array [VALUES] and return sorted array.",
            "answer": "```python\ndef merge_sort(arr):\n    if len(arr) <= 1: return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    return merge(left, right)\n\ndef merge(left, right):\n    result = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i] <= right[j]:\n            result.append(left[i])\n            i += 1\n        else:\n            result.append(right[j])\n            j += 1\n    result.extend(left[i:])\n    result.extend(right[j:])\n    return result```",
        },
        {
            "question": "Given array [VALUES], implement quick sort with random pivot.",
            "answer": "```python\nimport random\ndef quick_sort(arr, low=0, high=None):\n    if high is None: high = len(arr) - 1\n    if low < high:\n        pi = partition(arr, low, high)\n        quick_sort(arr, low, pi - 1)\n        quick_sort(arr, pi + 1, high)\n\ndef partition(arr, low, high):\n    random_index = random.randint(low, high)\n    arr[random_index], arr[high] = arr[high], arr[random_index]\n    pivot = arr[high]\n    i = low - 1\n    for j in range(low, high):\n        if arr[j] <= pivot:\n            i += 1\n            arr[i], arr[j] = arr[j], arr[i]\n    arr[i + 1], arr[high] = arr[high], arr[i + 1]\n    return i + 1```",
        },
        {
            "question": "Find all subarrays in [VALUES] with sum equal to target value 100.",
            "answer": "```python\ndef subarrays_with_sum(arr, target):\n    result = []\n    for i in range(len(arr)):\n        current_sum = 0\n        for j in range(i, len(arr)):\n            current_sum += arr[j]\n            if current_sum == target:\n                result.append(arr[i:j+1])\n    return result```",
        },
        {
            "question": "Given the array [VALUES], find the smallest subarray with a sum greater than [TARGET_SUM].",
            "answer": "Use a sliding window to find the smallest subarray with sum > [TARGET_SUM]: [SMALLEST_SUBARRAY].",
        },
        {
            "question": "Given the array [VALUES], find the maximum sum of a circular subarray.",
            "answer": "Use Kadane's algorithm for both normal and circular cases: [MAX_CIRCULAR_SUM].",
        },
        {
            "question": "Given the array [VALUES], find the minimum number of swaps required to sort the array.",
            "answer": "Count cycles in the array to determine minimum swaps: [MIN_SWAPS].",
        },
        {
            "question": "Given the array [VALUES], find the maximum sum of non-adjacent elements.",
            "answer": "Use dynamic programming to find the maximum sum of non-adjacent elements: [MAX_NON_ADJ_SUM].",
        },
        {
            "question": "Given the array [VALUES], find the equilibrium index (sum of left elements equals sum of right elements).",
            "answer": "Find the index where the sum of elements to the left equals the sum to the right: [EQUILIBRIUM_INDEX].",
        },
    ]

    # Singly Linked Lists - Level 1 (Beginner) - 
    singly_linked_list_beginner = [
        {
            "question": "Given a singly linked list with head pointing to node with value [HEAD] and values [VALUES], what is the value of the head node?",
            "answer": "The value of the head node is [HEAD].",
        },
        {
            "question": "Given a singly linked list with head node [HEAD] and values [VALUES], what is the value of the tail node?",
            "answer": "The value of the tail node is [TAIL]. The tail is the last node whose next pointer is NULL.",
        },
        {
            "question": "Find the length of the singly linked list with head [HEAD] and values [VALUES].",
            "answer": "Traverse from head to tail counting nodes. The length is [LENGTH].",
        },
        {
            "question": "Given a singly linked list with head [HEAD] and values [VALUES], what is the value at the 3rd node?",
            "answer": "Starting from head [HEAD], traverse 2 more nodes to reach the 3rd node with value [VALUE].",
        },
        {
            "question": "Find the sum of all values in the singly linked list with head [HEAD] and values [VALUES].",
            "answer": "Traverse all nodes and sum their values. The sum is [SUM].",
        },
        {
            "question": "Given a singly linked list with head [HEAD] and values [VALUES], insert a new node with value 42 at the beginning.",
            "answer": "Create new node with value 42, set its next to current head [HEAD], update head to point to new node.",
        },
        {
            "question": "Given a singly linked list with head [HEAD] and values [VALUES], insert a new node with value 42 at the end.",
            "answer": "Traverse to tail node [TAIL], create new node with value 42, set tail's next to new node.",
        },
        {
            "question": "Find the largest value in the singly linked list with head [HEAD] and values [VALUES].",
            "answer": "Traverse all nodes comparing values. The largest value is [MAX].",
        },
        {
            "question": "Find the smallest value in the singly linked list with head [HEAD] and values [VALUES].",
            "answer": "Traverse all nodes comparing values. The smallest value is [MIN].",
        },
        {
            "question": "Given a singly linked list with head [HEAD] and values [VALUES], delete the first node.",
            "answer": "Update head to point to head.next. The new head becomes the second node.",
        },
        {
            "question": "In singly linked list with head [HEAD] and values [VALUES], search for value 50.",
            "answer": "Traverse from head comparing each node's value with 50 until found or reach end.",
        },
        {
            "question": "Given singly linked list with head [HEAD] and values [VALUES], print all values.",
            "answer": "Start from head [HEAD], print current value, move to next until NULL.",
        },
        {
            "question": "Count even numbers in singly linked list with head [HEAD] and values [VALUES].",
            "answer": "Traverse all nodes, count those with value % 2 == 0.",
        },
        {
            "question": "Find second node value in singly linked list with head [HEAD] and values [VALUES].",
            "answer": "From head [HEAD], move to head.next to get second node value.",
        },
        {
            "question": "Check if singly linked list with head [HEAD] and values [VALUES] is empty.",
            "answer": "List is empty if head is NULL, otherwise it contains nodes.",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the value at the head node?",
            "answer": "The value at the head node is [HEAD].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the value at the tail node?",
            "answer": "The value at the tail node is [TAIL].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the length of the list?",
            "answer": "The length of the list is [LENGTH].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the value at index 2?",
            "answer": "The value at index 2 is [VALUE_AT_2].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the sum of all node values?",
            "answer": "The sum of all node values is [SUM].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the maximum value in the list?",
            "answer": "The maximum value is [MAX].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the minimum value in the list?",
            "answer": "The minimum value is [MIN].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the value of the node after the head?",
            "answer": "The value after the head is [SECOND].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after reversing the list?",
            "answer": "The reversed list is [REVERSED].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the value at the middle node?",
            "answer": "The value at the middle node is [MIDDLE].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after removing the head node?",
            "answer": "The list after removing the head is [WITHOUT_HEAD].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after removing the tail node?",
            "answer": "The list after removing the tail is [WITHOUT_TAIL].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after inserting 100 at the head?",
            "answer": "The list after inserting 100 at the head is [INSERTED_HEAD].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after inserting 100 at the tail?",
            "answer": "The list after inserting 100 at the tail is [INSERTED_TAIL].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after deleting the node at index 2?",
            "answer": "The list after deleting index 2 is [DELETED_INDEX_2].",
        },
    ]

    # Singly Linked Lists - Level 2 (Intermediate) -
    singly_linked_list_intermediate = [
        {
            "question": "Given a singly linked list with head [HEAD] and values [VALUES], reverse it.",
            "answer": "```python\ndef reverse_list(head):\n    prev = None\n    current = head\n    while current:\n        next_temp = current.next\n        current.next = prev\n        prev = current\n        current = next_temp\n    return prev```",
        },
        {
            "question": "Find the middle node of singly linked list with head [HEAD] and values [VALUES] using slow-fast pointer.",
            "answer": "```python\ndef find_middle(head):\n    slow = fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n    return slow```",
        },
        {
            "question": "Given singly linked list with head [HEAD] and values [VALUES], detect if it has a cycle.",
            "answer": "```python\ndef has_cycle(head):\n    slow = fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n        if slow == fast:\n            return True\n    return False```",
        },
        {
            "question": "Remove all nodes with even values from singly linked list with head [HEAD] and values [VALUES].",
            "answer": "```python\ndef remove_even(head):\n    dummy = ListNode(0)\n    dummy.next = head\n    prev = dummy\n    current = head\n    while current:\n        if current.val % 2 == 0:\n            prev.next = current.next\n        else:\n            prev = current\n        current = current.next\n    return dummy.next```",
        },
        {
            "question": "Delete node at position 3 in singly linked list with head [HEAD] and values [VALUES].",
            "answer": "```python\ndef delete_at_position(head, pos):\n    if pos == 0: return head.next\n    current = head\n    for i in range(pos - 1):\n        current = current.next\n    current.next = current.next.next\n    return head```",
        },
        {
            "question": "Merge two sorted singly linked lists with heads [HEAD1] and [HEAD2].",
            "answer": "```python\ndef merge_sorted(l1, l2):\n    dummy = ListNode(0)\n    current = dummy\n    while l1 and l2:\n        if l1.val <= l2.val:\n            current.next = l1\n            l1 = l1.next\n        else:\n            current.next = l2\n            l2 = l2.next\n        current = current.next\n    current.next = l1 or l2\n    return dummy.next```",
        },
        {
            "question": "Find nth node from end in singly linked list with head [HEAD] and values [VALUES].",
            "answer": "```python\ndef nth_from_end(head, n):\n    first = second = head\n    for i in range(n):\n        first = first.next\n    while first:\n        first = first.next\n        second = second.next\n    return second```",
        },
        {
            "question": "Remove duplicates from sorted singly linked list with head [HEAD] and values [VALUES].",
            "answer": "```python\ndef remove_duplicates(head):\n    current = head\n    while current and current.next:\n        if current.val == current.next.val:\n            current.next = current.next.next\n        else:\n            current = current.next\n    return head```",
        },
        {
            "question": "Rotate singly linked list with head [HEAD] and values [VALUES] to the right by k places.",
            "answer": "```python\ndef rotate_right(head, k):\n    if not head or k == 0: return head\n    length = 1\n    tail = head\n    while tail.next:\n        tail = tail.next\n        length += 1\n    k = k % length\n    if k == 0: return head\n    \n    new_tail = head\n    for i in range(length - k - 1):\n        new_tail = new_tail.next\n    new_head = new_tail.next\n    new_tail.next = None\n    tail.next = head\n    return new_head```",
        },
        {
            "question": "Check if singly linked list with head [HEAD] and values [VALUES] is palindrome.",
            "answer": "```python\ndef is_palindrome(head):\n    # Find middle and reverse second half\n    slow = fast = head\n    while fast and fast.next:\n        slow = slow.next\n        fast = fast.next.next\n    \n    # Reverse second half\n    prev = None\n    while slow:\n        next_temp = slow.next\n        slow.next = prev\n        prev = slow\n        slow = next_temp\n    \n    # Compare\n    while prev:\n        if head.val != prev.val:\n            return False\n        head = head.next\n        prev = prev.next\n    return True```",
        },
        {
            "question": "Add two numbers represented as singly linked lists with heads [HEAD1] and [HEAD2].",
            "answer": "```python\ndef add_two_numbers(l1, l2):\n    dummy = ListNode(0)\n    current = dummy\n    carry = 0\n    while l1 or l2 or carry:\n        val1 = l1.val if l1 else 0\n        val2 = l2.val if l2 else 0\n        total = val1 + val2 + carry\n        carry = total // 10\n        current.next = ListNode(total % 10)\n        current = current.next\n        if l1: l1 = l1.next\n        if l2: l2 = l2.next\n    return dummy.next```",
        },
        {
            "question": "Swap nodes in pairs in singly linked list with head [HEAD] and values [VALUES].",
            "answer": "```python\ndef swap_pairs(head):\n    dummy = ListNode(0)\n    dummy.next = head\n    prev = dummy\n    while prev.next and prev.next.next:\n        first = prev.next\n        second = prev.next.next\n        prev.next = second\n        first.next = second.next\n        second.next = first\n        prev = first\n    return dummy.next```",
        },
        {
            "question": "Find intersection point of two singly linked lists with heads [HEAD1] and [HEAD2].",
            "answer": "```python\ndef get_intersection(headA, headB):\n    if not headA or not headB: return None\n    pA, pB = headA, headB\n    while pA != pB:\n        pA = pA.next if pA else headB\n        pB = pB.next if pB else headA\n    return pA```",
        },
        {
            "question": "Sort singly linked list with head [HEAD] and values [VALUES] using merge sort.",
            "answer": "```python\ndef sort_list(head):\n    if not head or not head.next: return head\n    \n    # Find middle\n    slow = fast = head\n    prev = None\n    while fast and fast.next:\n        prev = slow\n        slow = slow.next\n        fast = fast.next.next\n    prev.next = None\n    \n    # Recursively sort both halves\n    left = sort_list(head)\n    right = sort_list(slow)\n    \n    # Merge sorted halves\n    return merge_sorted(left, right)```",
        },
        {
            "question": "Remove nth node from end of singly linked list with head [HEAD] and values [VALUES].",
            "answer": "```python\ndef remove_nth_from_end(head, n):\n    dummy = ListNode(0)\n    dummy.next = head\n    first = second = dummy\n    for i in range(n + 1):\n        first = first.next\n    while first:\n        first = first.next\n        second = second.next\n    second.next = second.next.next\n    return dummy.next```",
        },
        {
            "question": "Given a singly linked list [VALUES], find the index of the maximum value.",
            "answer": "The index of the maximum value [MAX] is [MAX_INDEX].",
        },
        {
            "question": "Given a singly linked list [VALUES], find the index of the minimum value.",
            "answer": "The index of the minimum value [MIN] is [MIN_INDEX].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after removing all even values?",
            "answer": "The list after removing even values is [NO_EVEN].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after removing all odd values?",
            "answer": "The list after removing odd values is [NO_ODD].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after doubling each value?",
            "answer": "The list after doubling each value is [DOUBLED].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after squaring each value?",
            "answer": "The list after squaring each value is [SQUARED].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after removing all duplicate values?",
            "answer": "The list after removing duplicates is [NO_DUPLICATES].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after rotating right by 2 positions?",
            "answer": "The list after rotating right by 2 is [ROTATED_RIGHT_2].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the sum of values at even indices?",
            "answer": "Sum values at indices 0, 2, 4, ... to get [SUM_EVEN_INDICES].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the sum of values at odd indices?",
            "answer": "Sum values at indices 1, 3, 5, ... to get [SUM_ODD_INDICES].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after reversing the first three nodes?",
            "answer": "Reverse the first three nodes to get [REVERSED_FIRST_THREE].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after swapping the first and last nodes?",
            "answer": "Swap first and last nodes to get [SWAPPED_FIRST_LAST].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after inserting 100 at index 2?",
            "answer": "Insert 100 at index 2 to get [INSERTED_100_INDEX_2].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after deleting all nodes with value 0?",
            "answer": "Delete all nodes with value 0 to get [NO_ZERO].",
        },
        {
            "question": "Given a singly linked list [VALUES], what is the result after removing all nodes greater than 50?",
            "answer": "Remove all nodes greater than 50 to get [NO_GREATER_50].",
        },
    ]
    # Sigly Lined Lists -Level 3(advanced)
    singly_linked_list_advanced = [
        {
            "question": "Given a singly linked list [VALUES], detect if there is a cycle.",
            "answer": "Use Floyd's cycle detection algorithm. Cycle exists: [CYCLE_EXISTS].",
        },
        {
            "question": "Given a singly linked list [VALUES], find the starting node of the cycle if it exists.",
            "answer": "The starting node of the cycle is [CYCLE_START].",
        },
        {
            "question": "Given a singly linked list [VALUES], reverse nodes in groups of k.",
            "answer": "Reverse every k nodes in the list: [REVERSED_GROUPS].",
        },
        {
            "question": "Given a singly linked list [VALUES], check if it is a palindrome.",
            "answer": "The list is [PALINDROME/NOT_PALINDROME].",
        },
        {
            "question": "Given a singly linked list [VALUES], sort the list using merge sort.",
            "answer": "The sorted list is [SORTED_LIST].",
        },
        {
            "question": "Given a singly linked list [VALUES], remove all nodes with duplicate values.",
            "answer": "Traverse and remove duplicate nodes: [NO_DUPLICATES].",
        },
        {
            "question": "Given a singly linked list [VALUES], rotate the list to the left by k positions.",
            "answer": "Rotate left by k positions: [ROTATED_LEFT_K].",
        },
        {
            "question": "Given a singly linked list [VALUES], rotate the list to the right by k positions.",
            "answer": "Rotate right by k positions: [ROTATED_RIGHT_K].",
        },
        {
            "question": "Given a singly linked list [VALUES], remove the Nth node from the end.",
            "answer": "Remove the Nth node from the end: [REMOVED_NTH_FROM_END].",
        },
        {
            "question": "Given a singly linked list [VALUES], partition the list around value X.",
            "answer": "Partition the list so that all nodes less than X come before nodes greater than or equal to X: [PARTITIONED].",
        },
        {
            "question": "Given a singly linked list [VALUES], find the intersection node with another list [VALUES2].",
            "answer": "The intersection node is [INTERSECTION_NODE].",
        },
        {
            "question": "Given a singly linked list [VALUES], remove all nodes with value X.",
            "answer": "Remove all nodes with value X: [NO_X].",
        },
        {
            "question": "Given a singly linked list [VALUES], swap every two adjacent nodes.",
            "answer": "Swap every two adjacent nodes: [SWAPPED_PAIRS].",
        },
        {
            "question": "Given a singly linked list [VALUES], find the length of the longest palindrome sublist.",
            "answer": "The length of the longest palindrome sublist is [LONGEST_PALINDROME].",
        },
        {
            "question": "Given a singly linked list [VALUES], flatten a multilevel linked list.",
            "answer": "Flatten the multilevel list into a single-level list: [FLATTENED].",
        },
        {
            "question": "Given a singly linked list [VALUES], add two numbers represented by two lists.",
            "answer": "Sum the two numbers and return as a linked list: [SUM_LIST].",
        },
        {
            "question": "Given a singly linked list [VALUES], reverse alternate k nodes.",
            "answer": "Reverse every alternate group of k nodes: [REVERSED_ALTERNATE_K].",
        },
        {
            "question": "Given a singly linked list [VALUES], clone the list with random pointers.",
            "answer": "Clone the list including random pointers: [CLONED_LIST].",
        },
        {
            "question": "Given a singly linked list [VALUES], find the node where the cycle begins.",
            "answer": "The node where the cycle begins is [CYCLE_START_NODE].",
        },
        {
            "question": "Given a singly linked list [VALUES], reverse the list recursively.",
            "answer": "Reverse the list using recursion: [REVERSED_RECURSIVE].",
        },
        {
            "question": "Given a singly linked list [VALUES], remove all nodes with value X.",
            "answer": "Remove all nodes with value X: [NO_X].",
        },
        {
            "question": "Given a singly linked list [VALUES], swap every two adjacent nodes.",
            "answer": "Swap every two adjacent nodes: [SWAPPED_PAIRS].",
        },
        {
            "question": "Given a singly linked list [VALUES], rotate the list to the left by k positions.",
            "answer": "Rotate left by k positions: [ROTATED_LEFT_K].",
        },
        {
            "question": "Given a singly linked list [VALUES], rotate the list to the right by k positions.",
            "answer": "Rotate right by k positions: [ROTATED_RIGHT_K].",
        },
        {
            "question": "Given a singly linked list [VALUES], remove the Nth node from the end.",
            "answer": "Remove the Nth node from the end: [REMOVED_NTH_FROM_END].",
        },
        {
            "question": "Given a singly linked list [VALUES], partition the list around value X.",
            "answer": "Partition the list so that all nodes less than X come before nodes greater than or equal to X: [PARTITIONED].",
        },
        {
            "question": "Given a singly linked list [VALUES], find the intersection node with another list [VALUES2].",
            "answer": "The intersection node is [INTERSECTION_NODE].",
        },
        {
            "question": "Given a singly linked list [VALUES], remove all nodes with value X.",
            "answer": "Remove all nodes with value X: [NO_X].",
        },
        {
            "question": "Given a singly linked list [VALUES], swap every two adjacent nodes.",
            "answer": "Swap every two adjacent nodes: [SWAPPED_PAIRS].",
        },
        {
            "question": "Given a singly linked list [VALUES], find the length of the longest palindrome sublist.",
            "answer": "The length of the longest palindrome sublist is [LONGEST_PALINDROME].",
        },
        {
            "question": "Given a singly linked list [VALUES], flatten a multilevel linked list.",
            "answer": "Flatten the multilevel list into a single-level list: [FLATTENED].",
        },
        {
            "question": "Given a singly linked list [VALUES], add two numbers represented by two lists.",
            "answer": "Sum the two numbers and return as a linked list: [SUM_LIST].",
        },
        {
            "question": "Given a singly linked list [VALUES], reverse alternate k nodes.",
            "answer": "Reverse every alternate group of k nodes: [REVERSED_ALTERNATE_K].",
        },
        {
            "question": "Given a singly linked list [VALUES], clone the list with random pointers.",
            "answer": "Clone the list including random pointers: [CLONED_LIST].",
        },
        {
            "question": "Given a singly linked list [VALUES], find the node where the cycle begins.",
            "answer": "The node where the cycle begins is [CYCLE_START_NODE].",
        },
    ]

    # Doubly Linked Lists - Level 1 (Beginner) - 
    doubly_linked_list_beginner = [
        {
            "question": "Given a doubly linked list with head [HEAD] and values [VALUES], what is the value of the head node?",
            "answer": "The value of the head node is [HEAD]. In doubly linked list, head.prev is NULL.",
        },
        {
            "question": "In doubly linked list with head [HEAD] and values [VALUES], what is the tail node value?",
            "answer": "The tail node value is [TAIL]. In doubly linked list, tail.next is NULL.",
        },
        {
            "question": "Find length of doubly linked list with head [HEAD] and values [VALUES].",
            "answer": "Traverse from head to tail counting nodes. Length is [LENGTH].",
        },
        {
            "question": "Given doubly linked list with head [HEAD] and values [VALUES], traverse backwards from tail.",
            "answer": "Start from tail [TAIL], use prev pointers to traverse: [REVERSED].",
        },
        {
            "question": "Insert node with value 42 at beginning of doubly linked list with head [HEAD].",
            "answer": "Create new node, set new.next = head, head.prev = new, update head = new.",
        },
        {
            "question": "Insert node with value 42 at end of doubly linked list with head [HEAD] and values [VALUES].",
            "answer": "Find tail [TAIL], create new node, set tail.next = new, new.prev = tail.",
        },
        {
            "question": "Delete first node from doubly linked list with head [HEAD] and values [VALUES].",
            "answer": "Update head = head.next, set new head.prev = NULL.",
        },
        {
            "question": "Delete last node from doubly linked list with head [HEAD] and values [VALUES].",
            "answer": "Find tail [TAIL], update tail.prev.next = NULL.",
        },
        {
            "question": "Search for value 50 in doubly linked list with head [HEAD] and values [VALUES].",
            "answer": "Traverse from head comparing each node's value with 50.",
        },
        {
            "question": "Find sum of all values in doubly linked list with head [HEAD] and values [VALUES].",
            "answer": "Traverse all nodes and sum their values. Sum is [SUM].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at the head node?",
            "answer": "The value at the head node is [HEAD].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at the tail node?",
            "answer": "The value at the tail node is [TAIL].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the length of the list?",
            "answer": "The length of the list is [LENGTH].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at index 2?",
            "answer": "The value at index 2 is [VALUE_AT_2].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after reversing the list?",
            "answer": "The reversed list is [REVERSED].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after removing the head node?",
            "answer": "The list after removing the head is [WITHOUT_HEAD].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after removing the tail node?",
            "answer": "The list after removing the tail is [WITHOUT_TAIL].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after inserting 100 at the head?",
            "answer": "The list after inserting 100 at the head is [INSERTED_HEAD].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after inserting 100 at the tail?",
            "answer": "The list after inserting 100 at the tail is [INSERTED_TAIL].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after deleting the node at index 2?",
            "answer": "The list after deleting index 2 is [DELETED_INDEX_2].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the sum of all node values?",
            "answer": "The sum of all node values is [SUM].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the maximum value in the list?",
            "answer": "The maximum value is [MAX].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the minimum value in the list?",
            "answer": "The minimum value is [MIN].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at the previous node of index 2?",
            "answer": "The value at the previous node of index 2 is [PREV_2].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at the next node of index 2?",
            "answer": "The value at the next node of index 2 is [NEXT_2].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at the head node?",
            "answer": "The value at the head node is [HEAD].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at the tail node?",
            "answer": "The value at the tail node is [TAIL].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the length of the list?",
            "answer": "The length of the list is [LENGTH].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at index 2?",
            "answer": "The value at index 2 is [VALUE_AT_2].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after reversing the list?",
            "answer": "The reversed list is [REVERSED].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after removing the head node?",
            "answer": "The list after removing the head is [WITHOUT_HEAD].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after removing the tail node?",
            "answer": "The list after removing the tail is [WITHOUT_TAIL].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after inserting 100 at the head?",
            "answer": "The list after inserting 100 at the head is [INSERTED_HEAD].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after inserting 100 at the tail?",
            "answer": "The list after inserting 100 at the tail is [INSERTED_TAIL].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the result after deleting the node at index 2?",
            "answer": "The list after deleting index 2 is [DELETED_INDEX_2].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the sum of all node values?",
            "answer": "The sum of all node values is [SUM].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the maximum value in the list?",
            "answer": "The maximum value is [MAX].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the minimum value in the list?",
            "answer": "The minimum value is [MIN].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at the previous node of index 2?",
            "answer": "The value at the previous node of index 2 is [PREV_2].",
        },
        {
            "question": "Given a doubly linked list [VALUES], what is the value at the next node of index 2?",
            "answer": "The value at the next node of index 2 is [NEXT_2].",
        },
    ]
    # Doubly linked list intermediate level 2 
    doubly_linked_list_intermediate = [
    {
        "question": "Given a doubly linked list [VALUES], reverse the list recursively.",
        "answer": "Reverse the list using recursion: [REVERSED_RECURSIVE]."
    },
    {
        "question": "Given a doubly linked list [VALUES], remove all nodes with value X.",
        "answer": "Remove all nodes with value X: [NO_X]."
    },
    {
        "question": "Given a doubly linked list [VALUES], swap every two adjacent nodes.",
        "answer": "Swap every two adjacent nodes: [SWAPPED_PAIRS]."
    },
    {
        "question": "Given a doubly linked list [VALUES], rotate the list to the left by k positions.",
        "answer": "Rotate left by k positions: [ROTATED_LEFT_K]."
    },
    {
        "question": "Given a doubly linked list [VALUES], rotate the list to the right by k positions.",
        "answer": "Rotate right by k positions: [ROTATED_RIGHT_K]."
    },
    {
        "question": "Given a doubly linked list [VALUES], remove the Nth node from the end.",
        "answer": "Remove the Nth node from the end: [REMOVED_NTH_FROM_END]."
    },
    {
        "question": "Given a doubly linked list [VALUES], partition the list around value X.",
        "answer": "Partition the list so that all nodes less than X come before nodes greater than or equal to X: [PARTITIONED]."
    },
    {
        "question": "Given a doubly linked list [VALUES], find the intersection node with another list [VALUES2].",
        "answer": "The intersection node is [INTERSECTION_NODE]."
    },
    {
        "question": "Given a doubly linked list [VALUES], remove all nodes with duplicate values from a sorted list.",
        "answer": "Remove all duplicates so only unique values remain: [ONLY_UNIQUE]."
    },
    {
        "question": "Given a doubly linked list [VALUES], split the list into two halves.",
        "answer": "Split the list into two halves: [FIRST_HALF], [SECOND_HALF]."
    }
]

    # Doublt Lined lists- Level 3 (advanced )
    doubly_linked_list_advance = [
        {
            "question": "Given a doubly linked list [VALUES], reverse the list in place.",
            "answer": "Reverse the next and prev pointers for all nodes: [REVERSED].",
        },
        {
            "question": "Given a doubly linked list [VALUES], remove all nodes with duplicate values.",
            "answer": "Traverse and remove duplicate nodes: [NO_DUPLICATES].",
        },
        {
            "question": "Given a doubly linked list [VALUES], insert a node with value X before node with value Y.",
            "answer": "Find node Y, insert new node before it: [INSERTED_BEFORE_Y].",
        },
        {
            "question": "Given a doubly linked list [VALUES], delete the node at position k.",
            "answer": "Traverse to position k and remove the node: [DELETED_K].",
        },
        {
            "question": "Given a doubly linked list [VALUES], check if the list is a palindrome.",
            "answer": "Compare values from head and tail moving inward: [PALINDROME/NOT_PALINDROME].",
        },
    ]

    # Circular Linked Lists - Level 1 (Beginner) - 
    circular_linked_list_beginner = [
        {
            "question": "Given a circular linked list with head [HEAD] and values [VALUES], what makes it circular?",
            "answer": "The last node's next pointer points back to the head [HEAD] instead of NULL.",
        },
        {
            "question": "In circular linked list with head [HEAD] and values [VALUES], how do you detect the end?",
            "answer": "Traverse until you reach the head again. No NULL pointers exist.",
        },
        {
            "question": "Find length of circular linked list with head [HEAD] and values [VALUES].",
            "answer": "Start from head, count nodes until you return to head. Length is [LENGTH].",
        },
        {
            "question": "Insert node with value 42 at beginning of circular linked list with head [HEAD].",
            "answer": "Find tail (node pointing to head), create new node, update connections.",
        },
        {
            "question": "Delete node with value X from circular linked list with head [HEAD] and values [VALUES].",
            "answer": "Find node and its previous, update prev.next = node.next.",
        },
        {
            "question": "Convert singly linked list with head [HEAD] to circular linked list.",
            "answer": "Find tail node, set tail.next = head to make it circular.",
        },
        {
            "question": "Check if linked list with head [HEAD] is circular.",
            "answer": "Use Floyd's algorithm or traverse and check if you return to head.",
        },
        {
            "question": "Split circular linked list with head [HEAD] and values [VALUES] into two halves.",
            "answer": "Find middle using slow-fast pointers, break and create two circular lists.",
        },
        {
            "question": "Find maximum value in circular linked list with head [HEAD] and values [VALUES].",
            "answer": "Traverse once starting from head until back to head. Max is [MAX].",
        },
        {
            "question": "Reverse circular linked list with head [HEAD] and values [VALUES].",
            "answer": "Similar to singly linked list reversal but maintain circular property.",
        },
    ]

    # Circular lined list intermediate
    circular_linked_list_intermediate = [
        {
            "question": "Given a circular linked list [VALUES], detect if there is a cycle.",
            "answer": "Traverse the list and check if you return to the head: [CYCLE_EXISTS].",
        },
        {
            "question": "Given a circular linked list [VALUES], remove all nodes with value X.",
            "answer": "Remove all nodes with value X: [NO_X].",
        },
        {
            "question": "Given a circular linked list [VALUES], split the list into two halves.",
            "answer": "Use slow and fast pointers to split the list: [SPLIT_HALVES].",
        },
        {
            "question": "Given a circular linked list [VALUES], insert a node with value Y after node with value X.",
            "answer": "Find node X and insert new node after it: [INSERTED_AFTER_X].",
        },
        {
            "question": "Given a circular linked list [VALUES], reverse the list.",
            "answer": "Reverse the next pointers while maintaining circularity: [REVERSED].",
        },
    ]
    # Circular lined list advanced
    circular_linked_list_advanced = [
        {
            "question": "Given a circular linked list [VALUES], remove every kth node until only one node remains.",
            "answer": "This is the Josephus problem. The last remaining node is [LAST_NODE].",
        },
        {
            "question": "Given a circular linked list [VALUES], check if the list is a palindrome.",
            "answer": "Compare values from head moving forward and backward: [PALINDROME/NOT_PALINDROME].",
        },
        {
            "question": "Given a circular linked list [VALUES], merge two sorted circular linked lists.",
            "answer": "Merge both lists and maintain circular property: [MERGED_LIST].",
        },
        {
            "question": "Given a circular linked list [VALUES], find the length of the longest sequence of identical values.",
            "answer": "Traverse and track the longest sequence: [LONGEST_SEQUENCE].",
        },
        {
            "question": "Given a circular linked list [VALUES], delete alternate nodes.",
            "answer": "Delete every second node in the list: [ALTERNATE_DELETED].",
        },
    ]

    # Trees - Level 1 (Beginner) - 
    tree_beginner = [
        {
            "question": "Given a binary tree with root [ROOT] and values [VALUES], what is the root node value?",
            "answer": "The root node value is [ROOT]. This is the topmost node of the tree.",
        },
        {
            "question": "Find the height of binary tree with root [ROOT] and values [VALUES].",
            "answer": "Height is the longest path from root to leaf. Use recursive approach: height = 1 + max(left_height, right_height).",
        },
        {
            "question": "Count total nodes in binary tree with root [ROOT] and values [VALUES].",
            "answer": "Recursively count: total = 1 + count(left) + count(right). Total nodes: [COUNT].",
        },
        {
            "question": "Find all leaf nodes in binary tree with root [ROOT] and values [VALUES].",
            "answer": "Leaf nodes have no children (left == NULL && right == NULL). Leaves: [LEAVES].",
        },
        {
            "question": "Perform inorder traversal of binary tree with root [ROOT] and values [VALUES].",
            "answer": "Inorder: Left -> Root -> Right. Result: [INORDER].",
        },
        {
            "question": "Perform preorder traversal of binary tree with root [ROOT] and values [VALUES].",
            "answer": "Preorder: Root -> Left -> Right. Result: [PREORDER].",
        },
        {
            "question": "Perform postorder traversal of binary tree with root [ROOT] and values [VALUES].",
            "answer": "Postorder: Left -> Right -> Root. Result: [POSTORDER].",
        },
        {
            "question": "Find sum of all node values in binary tree with root [ROOT] and values [VALUES].",
            "answer": "Recursively sum all nodes: sum = root.val + sum(left) + sum(right). Sum: [SUM].",
        },
        {
            "question": "What is the left child of root in binary tree with root [ROOT] and values [VALUES]?",
            "answer": "The left child of root [ROOT] has value [LEFT_CHILD].",
        },
        {
            "question": "What is the right child of root in binary tree with root [ROOT] and values [VALUES]?",
            "answer": "The right child of root [ROOT] has value [RIGHT_CHILD].",
        },
        {
            "question": "Find maximum value in binary tree with root [ROOT] and values [VALUES].",
            "answer": "Traverse all nodes and track maximum. Maximum value: [MAX].",
        },
        {
            "question": "Find minimum value in binary tree with root [ROOT] and values [VALUES].",
            "answer": "Traverse all nodes and track minimum. Minimum value: [MIN].",
        },
        {
            "question": "Check if binary tree with root [ROOT] is empty.",
            "answer": "Tree is empty if root is NULL, otherwise it contains nodes.",
        },
        {
            "question": "Find depth of a specific node with value X in binary tree with root [ROOT].",
            "answer": "Depth is distance from root. Use BFS or DFS to find node and track depth.",
        },
        {
            "question": "Count internal nodes in binary tree with root [ROOT] and values [VALUES].",
            "answer": "Internal nodes have at least one child. Count = Total nodes - Leaf nodes.",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the value at the root?",
            "answer": "The value at the root is [ROOT].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the height of the tree?",
            "answer": "The height of the tree is [HEIGHT].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the number of leaf nodes?",
            "answer": "The number of leaf nodes is [LEAF_COUNT].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the sum of all node values?",
            "answer": "The sum of all node values is [SUM].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the maximum value in the tree?",
            "answer": "The maximum value is [MAX].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the minimum value in the tree?",
            "answer": "The minimum value is [MIN].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the result of an inorder traversal?",
            "answer": "The inorder traversal is [INORDER].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the result of a preorder traversal?",
            "answer": "The preorder traversal is [PREORDER].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the result of a postorder traversal?",
            "answer": "The postorder traversal is [POSTORDER].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the result of a level order traversal?",
            "answer": "The level order traversal is [LEVELORDER].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the value at the leftmost node?",
            "answer": "The value at the leftmost node is [LEFTMOST].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the value at the rightmost node?",
            "answer": "The value at the rightmost node is [RIGHTMOST].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the number of nodes at level 2?",
            "answer": "The number of nodes at level 2 is [LEVEL2_COUNT].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the sum of all leaf node values?",
            "answer": "The sum of all leaf node values is [LEAF_SUM].",
        },
        {
            "question": "Given a binary tree with values [VALUES], what is the maximum depth of the tree?",
            "answer": "The maximum depth is [MAX_DEPTH].",
        },
    ]

    # Trees - Level 2 (Intermediate) - 
    tree_intermediate = [
        {
            "question": "Check if binary tree with root [ROOT] and values [VALUES] is a Binary Search Tree.",
            "answer": "```python\ndef is_bst(root, min_val=float('-inf'), max_val=float('inf')):\n    if not root: return True\n    if root.val <= min_val or root.val >= max_val: return False\n    return is_bst(root.left, min_val, root.val) and is_bst(root.right, root.val, max_val)```",
        },
        {
            "question": "Find diameter of binary tree with root [ROOT] and values [VALUES].",
            "answer": "```python\ndef diameter(root):\n    def height(node):\n        if not node: return 0\n        left = height(node.left)\n        right = height(node.right)\n        self.diameter = max(self.diameter, left + right)\n        return 1 + max(left, right)\n    \n    self.diameter = 0\n    height(root)\n    return self.diameter```",
        },
        {
            "question": "Perform level order traversal of binary tree with root [ROOT] and values [VALUES].",
            "answer": "```python\nfrom collections import deque\ndef level_order(root):\n    if not root: return []\n    result = []\n    queue = deque([root])\n    while queue:\n        level_size = len(queue)\n        level = []\n        for _ in range(level_size):\n            node = queue.popleft()\n            level.append(node.val)\n            if node.left: queue.append(node.left)\n            if node.right: queue.append(node.right)\n        result.append(level)\n    return result```",
        },
        {
            "question": "Find lowest common ancestor of nodes X and Y in binary tree with root [ROOT].",
            "answer": "```python\ndef lca(root, p, q):\n    if not root or root == p or root == q:\n        return root\n    left = lca(root.left, p, q)\n    right = lca(root.right, p, q)\n    if left and right: return root\n    return left or right```",
        },
        {
            "question": "Convert binary tree with root [ROOT] to its mirror image.",
            "answer": "```python\ndef mirror_tree(root):\n    if not root: return None\n    root.left, root.right = root.right, root.left\n    mirror_tree(root.left)\n    mirror_tree(root.right)\n    return root```",
        },
        {
            "question": "Check if binary tree with root [ROOT] and values [VALUES] is balanced.",
            "answer": "```python\ndef is_balanced(root):\n    def height(node):\n        if not node: return 0\n        left = height(node.left)\n        right = height(node.right)\n        if left == -1 or right == -1 or abs(left - right) > 1:\n            return -1\n        return 1 + max(left, right)\n    return height(root) != -1```",
        },
        {
            "question": "Find all root-to-leaf paths in binary tree with root [ROOT] and values [VALUES].",
            "answer": "```python\ndef root_to_leaf_paths(root):\n    def dfs(node, path, result):\n        if not node: return\n        path.append(node.val)\n        if not node.left and not node.right:\n            result.append(path[:])\n        else:\n            dfs(node.left, path, result)\n            dfs(node.right, path, result)\n        path.pop()\n    \n    result = []\n    dfs(root, [], result)\n    return result```",
        },
        {
            "question": "Find maximum width of binary tree with root [ROOT] and values [VALUES].",
            "answer": "```python\nfrom collections import deque\ndef max_width(root):\n    if not root: return 0\n    max_w = 0\n    queue = deque([(root, 0)])\n    while queue:\n        level_size = len(queue)\n        _, first_index = queue[0]\n        for i in range(level_size):\n            node, index = queue.popleft()\n            if node.left: queue.append((node.left, 2 * index))\n            if node.right: queue.append((node.right, 2 * index + 1))\n        max_w = max(max_w, index - first_index + 1)\n    return max_w```",
        },
        {
            "question": "Check if binary tree with root [ROOT] and values [VALUES] is symmetric.",
            "answer": "```python\ndef is_symmetric(root):\n    def is_mirror(left, right):\n        if not left and not right: return True\n        if not left or not right: return False\n        return (left.val == right.val and \n                is_mirror(left.left, right.right) and                is_mirror(left.right, right.left))\n    return is_mirror(root.left, root.right) if root else True```",
        },
        {
            "question": "Find kth smallest element in BST with root [ROOT] and values [VALUES].",
            "answer": "```python\ndef kth_smallest(root, k):\n    def inorder(node):\n        if not node: return\n        inorder(node.left)\n        self.count += 1\n        if self.count == k:\n            self.result = node.val\n            return\n        inorder(node.right)\n    \n    self.count = 0\n    self.result = 0\n    inorder(root)\n    return self.result```",
        },
        {
            "question": "Construct binary tree from inorder and preorder traversals.",
            "answer": "```python\ndef build_tree(preorder, inorder):\n    if not preorder or not inorder: return None\n    root = TreeNode(preorder[0])\n    mid = inorder.index(preorder[0])\n    root.left = build_tree(preorder[1:mid+1], inorder[:mid])\n    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])\n    return root```",
        },
        {
            "question": "Find vertical order traversal of binary tree with root [ROOT].",
            "answer": "```python\nfrom collections import defaultdict, deque\ndef vertical_order(root):\n    if not root: return []\n    column_table = defaultdict(list)\n    queue = deque([(root, 0)])\n    while queue:\n        node, column = queue.popleft()\n        column_table[column].append(node.val)\n        if node.left: queue.append((node.left, column - 1))\n        if node.right: queue.append((node.right, column + 1))\n    return [column_table[x] for x in sorted(column_table.keys())]```",
        },
        {
            "question": "Find boundary traversal of binary tree with root [ROOT].",
            "answer": "```python\ndef boundary_traversal(root):\n    if not root: return []\n    result = [root.val]\n    \n    def left_boundary(node):\n        if not node or (not node.left and not node.right): return\n        result.append(node.val)\n        if node.left: left_boundary(node.left)\n        else: left_boundary(node.right)\n    \n    def leaves(node):\n        if not node: return\n        if not node.left and not node.right:\n            result.append(node.val)\n        leaves(node.left)\n        leaves(node.right)\n    \n    def right_boundary(node):\n        if not node or (not node.left and not node.right): return\n        if node.right: right_boundary(node.right)\n        else: right_boundary(node.left)\n        result.append(node.val)\n    \n    left_boundary(root.left)\n    leaves(root)\n    right_boundary(root.right)\n    return result```",
        },
        {
            "question": "Convert binary tree with root [ROOT] to doubly linked list in-place.",
            "answer": "```python\ndef tree_to_dll(root):\n    def convert(node):\n        if not node: return None, None\n        \n        left_head, left_tail = convert(node.left)\n        right_head, right_tail = convert(node.right)\n        \n        if left_tail:\n            left_tail.right = node\n            node.left = left_tail\n        \n        if right_head:\n            node.right = right_head\n            right_head.left = node\n        \n        head = left_head if left_head else node\n        tail = right_tail if right_tail else node\n        \n        return head, tail\n    \n    head, _ = convert(root)\n    return head```",
        },
        {
            "question": "Find sum of nodes at maximum depth in binary tree with root [ROOT].",
            "answer": "```python\ndef sum_at_max_depth(root):\n    if not root: return 0\n    \n    def dfs(node, depth):\n        if not node: return 0, -1\n        if not node.left and not node.right:\n            return node.val, depth\n        \n        left_sum, left_depth = dfs(node.left, depth + 1)\n        right_sum, right_depth = dfs(node.right, depth + 1)\n        \n        if left_depth > right_depth:\n            return left_sum, left_depth\n        elif right_depth > left_depth:\n            return right_sum, right_depth\n        else:\n            return left_sum + right_sum, left_depth\n    \n    result, _ = dfs(root, 0)\n    return result```",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the path from root to node with value [TARGET].",
            "answer": "The path from root to [TARGET] is [PATH].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the lowest common ancestor of nodes [A] and [B].",
            "answer": "The lowest common ancestor of [A] and [B] is [LCA].",
        },
        {
            "question": "Given a binary tree with values [VALUES], check if the tree is balanced.",
            "answer": "The tree is [BALANCED/NOT_BALANCED].",
        },
        {
            "question": "Given a binary tree with values [VALUES], check if the tree is a binary search tree.",
            "answer": "The tree is [BST/NOT_BST].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the diameter of the tree.",
            "answer": "The diameter of the tree is [DIAMETER].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the maximum width of the tree.",
            "answer": "The maximum width is [MAX_WIDTH].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the sum of all nodes at the deepest level.",
            "answer": "The sum at the deepest level is [DEEP_SUM].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the vertical order traversal.",
            "answer": "The vertical order traversal is [VERTICAL_ORDER].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the boundary traversal.",
            "answer": "The boundary traversal is [BOUNDARY].",
        },
        {
            "question": "Given a binary tree with values [VALUES], convert it to its mirror image.",
            "answer": "The mirror image of the tree is [MIRROR].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find all root-to-leaf paths.",
            "answer": "All root-to-leaf paths are [ROOT_TO_LEAF_PATHS].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the kth smallest element.",
            "answer": "The kth smallest element is [KTH_SMALLEST].",
        },
        {
            "question": "Given a binary tree with values [VALUES], construct the tree from inorder and preorder traversals.",
            "answer": "The constructed tree is [CONSTRUCTED_TREE].",
        },
        {
            "question": "Given a binary tree with values [VALUES], check if the tree is symmetric.",
            "answer": "The tree is [SYMMETRIC/NOT_SYMMETRIC].",
        },
        {
            "question": "Given a binary tree with values [VALUES], convert it to a doubly linked list in-place.",
            "answer": "The doubly linked list is [DOUBLY_LINKED_LIST].",
        },
    ]
    tree_advanced = [
        {
            "question": "Given a binary tree with values [VALUES], find the maximum path sum.",
            "answer": "The maximum path sum is [MAX_PATH_SUM].",
        },
        {
            "question": "Given a binary tree with values [VALUES], print the tree in spiral (zigzag) order.",
            "answer": "The spiral order traversal is [SPIRAL_ORDER].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the distance between two nodes [A] and [B].",
            "answer": "The distance between [A] and [B] is [DISTANCE].",
        },
        {
            "question": "Given a binary tree with values [VALUES], find the largest BST subtree.",
            "answer": "The largest BST subtree has size [LARGEST_BST_SIZE].",
        },
        {
            "question": "Given a binary tree with values [VALUES], flatten the tree to a linked list in-place.",
            "answer": "The flattened list is [FLATTENED_LIST].",
        },
    ]

    # Add all questions to the main list
    topics_and_levels = [
        ("Array", 1, array_beginner),
        ("Array", 2, array_intermediate),
        ("Array", 3, array_advanced),
        ("Singly Linked List", 1, singly_linked_list_beginner),
        ("Singly Linked List", 2, singly_linked_list_intermediate),
        ("Singly Linked List", 3, singly_linked_list_advanced),
        ("Doubly Linked List", 1, doubly_linked_list_beginner),
        ("Doubly Linked List", 2, doubly_linked_list_intermediate),  
        ("Doubly Linked List", 3, doubly_linked_list_advance),
        ("Circular Linked List", 1, circular_linked_list_beginner),
        ("Circular Linked List", 2, circular_linked_list_intermediate),  
        ("Circular Linked List", 3, circular_linked_list_advanced),
        ("Tree", 1, tree_beginner),
        ("Tree", 2, tree_intermediate),
        ("Tree", 3, tree_advanced),  
    ]

    for topic, level, questions_list in topics_and_levels:
        for q in questions_list:
            questions.append(
                {
                    "id": question_id,
                    "topic": topic,
                    "difficulty": level,
                    "question": q["question"],
                    "answer": q["answer"],
                }
            )
            question_id += 1

    # Create DataFrame and save to CSV
    df = pd.DataFrame(questions)
    df.to_csv("data/questions.csv", index=False)
    print(f"Generated {len(questions)} comprehensive questions in data/questions.csv")


if __name__ == "__main__":
    generate_sample_questions()
