class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for v in nums:
            if v in hash_set:
                return True
            else:
                hash_set.add(v)
        return False
        