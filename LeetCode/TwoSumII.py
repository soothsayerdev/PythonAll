class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return 0

        i = 0
        j = len(numbers) - 1

        while i < j:
            _sum = numbers[i] + numbers[j]
            if _sum == target:
                return [i + 1, j + 1]

            if _sum > target:
                j -= 1
            
            else:
                i += 1

        return []