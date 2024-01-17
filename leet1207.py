"""
Leet code 1207. Unique Number of Occurrences

Complexity: O(n) i think?

Basically I abuse dictionaries for counting, then make them into a list into a set(which destroys non-unique occurences then list again.
Sets destroy duplicates, so if the length of the set is the same as the length of the original list, then all the occurences are unique.
Probably train myself into using some kind of counter instead of dictionary abusing but hey, it works.

"""

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurs = {}
        for a in arr:
            if occurs.get(a):
                occurs[a] = occurs.get(a) + 1
            else:
                occurs[a] = 1

        uniques = list(set(list(occurs.values())))
        return len(uniques) == len(occurs.values())