class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_tab = {}
        for num in nums:
            if str(num) in hash_tab:
                hash_tab[str(num)] += 1
            else:
                hash_tab[str(num)] = 1
        for num in hash_tab.values():
            if (num > 1):
                return True
        return False