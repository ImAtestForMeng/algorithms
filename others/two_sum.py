class Solution:
    # time complexity: O(n)
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        
        for i in range(len(numbers)):
            res = target - numbers[i]
            if res in hash_table:
                index1 = hash_table[res]
                index2 = i + 1
                if index1 < index2:
                    return [index1, index2]
                else:
                    return [index2, index1]
            hash_table[numbers[i]] = i + 1
        return 0

# what if duplicate items appear?

numbers = [0,0,3,4] # be careful about this situation
target = 0
print(Solution().twoSum(numbers, target))