class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                mapping[stack.pop()] = i
            stack.append(i)
        result = []
        for j in nums1:
            result.append(mapping.get(j,-1))
        return result