"""
https://www.codewars.com/kata/5467e4d82edf8bbf40000155/ - Task's Link


Simple one before I study for an exam. 

Well, instead of sorting we can also try to get maximum char value out of our list using something like max() and remove that from list afterwards.

Complexity: If conversions doesn't take "n" time(which I believe it doesnt), this should be a O(nlogn) time 

"""

def descending_order(num):
    # Bust a move right here
    numStr = str(num)
    nums = sorted(numStr, reverse=True)
    res = int(''.join(nums))
    return res
