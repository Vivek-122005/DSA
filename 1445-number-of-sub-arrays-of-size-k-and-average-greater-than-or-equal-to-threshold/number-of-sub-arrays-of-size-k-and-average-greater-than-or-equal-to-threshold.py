class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start, end = 0,k 
        sum1 = 0
        count = 0
        for i in range(0,k):
            sum1 += arr[i]

        if sum1/k >= threshold:
            count +=1
        while(end<len(arr)):
            sum1 -= arr[start]
            sum1 += arr[end]
            if (sum1/k) >= threshold:
                count+= 1
            start += 1
            end += 1
        return count
        