# hw9pr2.py
# Andrew Marks
# Coding Bat Problems


# Medium python list problems
def count_evens(nums):
    count = 0
    for x in nums:
        if x % 2 == 0:
            count += 1
    return count


def big_diff(nums):
    x = min(nums)
    y = max(nums)
    dif = y - x
    return dif


def centered_average(nums):
    newlist = []
    for x in range(len(nums)):
        newlist.append(min(nums))
        nums.remove(newlist[x])
    newlist.remove(min(newlist))
    newlist.remove(max(newlist))
    c_avg = sum(newlist)/len(newlist)
    return c_avg


def sum13(nums):
    s = 0
    for i in range(len(nums)):
        if i == 0:
            if nums[i] == 13:
                s += 0
            else:
                s += nums[i]
        elif nums[i] == 13:
            s += 0
        else:
            if nums[i-1] == 13:
                s += 0
            else:
                s += nums[i]
    return s


def has22(nums):
    if len(nums) < 2:
        return False
    elif 2 not in nums:
        return False
    else:
        for i in range(len(nums)):
            if i == 0 and nums[i] == 2:
                if nums[i+1] == 2:
                    return True
            elif i == len(nums) and nums[i] == 2:
                if nums[i-1] == 2:
                    return True
            else:
                if nums[i] == 2:
                    if nums[i-1] == 2:
                        return True
                    elif nums[i+1] == 2:
                        return True
                    else:
                        return False
    return


def double_char(str):
  new_str = ''
  for x in str:
    new_str =  new_str + x*2
  return new_str
