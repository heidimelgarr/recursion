"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Heidi Melgar, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: he3839

"""



def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    # Best case
    if target == 0:
        return True

    # If target not met
    if start == len(nums):
        return False

    # Including current num
    updated_target = target - nums[start]
    # Move to next index
    move_index = start + 1

    add_current = group_sum(move_index, nums, updated_target)
    if add_current:
        return True

    discard_current= group_sum(move_index, nums, target)
    return discard_current



def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    # Best case
    if target == 0:
        return True

    # If target not met
    if start == len(nums):
        return False

    updated_target = target - nums[start]
    # Move to next index
    move_index = start + 1

    # If current num is 6 then add to sum
    if nums[start] == 6:
        return group_sum_6(move_index, nums, updated_target)
    add_current = group_sum_6(move_index, nums, updated_target)
    if add_current:
        return True

    # Discard current num
    discard_current =  group_sum_6(move_index, nums, updated_target)
    return discard_current




def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    # Best case
    if target == 0:
        return True

    # If target not met
    if start == len(nums):
        return False

    # Move to next index
    move_index = start + 1
    # Skip adjacent num
    updated_target = target - nums[start]
    add_current = group_no_adj(move_index +1, nums, updated_target)

    if add_current:
        return True

    discard_current= group_no_adj(move_index, nums, target)
    return discard_current



def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    # Base Case
    if target == 0:
        return True

    # If target not met
    if start == len(nums):
        return False

    # Move to next index
    move_index = start + 1
    if nums[start] % 5 == 0:
        updated_target = target - nums[start]
        # If num if 1
        if nums[move_index:move_index+1] == [1]:
            move_index += 1

        return group_sum_5(move_index, nums, updated_target)

    updated_target = target - nums[start]
    add_current = group_sum_5(move_index, nums, updated_target)

    if add_current:
        return True

    discard_current = group_sum_5(move_index, nums, target)
    return discard_current




def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    # Best case
    if target == 0:
        return True

    if start >= len(nums):
        return False

    move_index = start
    group_of_sum = 0

    for i in range(start, len(nums)):
        if nums[i] == nums[start]:
            group_of_sum += nums[i]
            move_index += 1
    # Include all
    target -= group_of_sum
    if group_sum_clump(move_index, nums, target):
        return True
    target += group_of_sum

    # Excluding
    return group_sum_clump(move_index, nums, target)


#TO DO
def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def helper(start, subset1, subset2):
        # Base case
        if start == len(nums):
            return subset1 == subset2
        move_index = start + 1

        subset1 += nums[start]
        if helper(move_index, subset1, subset2):
            return True
        subset1 -= nums[start] # Backtrack

        subset2 += nums[start]
        if helper(move_index, subset1, subset2):
            return True
        subset2 -= nums[start] # Backtrack
        return False

    return helper(0, 0, 0)


#TO DO
def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def helper(index, subset1, subset2):
        # Base case
        if index == len(nums):
            if subset1 % 10 == 0 and subset2 % 2 == 1:
                return True
            if subset2 % 10 == 0 and subset1 % 2 == 1:
                return True
            return False

        move_index = index + 1
        # Recurse by adding to subset
        if helper(move_index, subset1 + nums[index], subset2):
            return True
        if helper(move_index, subset1, subset2 + nums[index]):
            return True
        return False

    return helper(0, 0, 0)


#TO DO
def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def helper(index, subset1, subset2):
        # Base case
        if index == len(nums):
            return subset1 == subset2

        move_index = index + 1

        # Recurse by adding num to group
        if nums[index] % 5 == 0:
            if helper(move_index, subset1 + nums[index], subset2):
                return True
        elif nums[index] % 3 == 0:
            if helper(move_index, subset1, subset2 + nums[index]):
                return True
        else:
            # Either subset
            if helper(move_index, subset1 + nums[index], subset2):
                return True
            if helper(move_index, subset1, subset2 + nums[index]):
                return True
        return False
    return helper(0, 0, 0)
