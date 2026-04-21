class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # list1 = []
        # pp = 1
        # ss = 1
        # prefix = []
        # sufix = []
        # n = len(nums)
        # for i in range(0,len(nums)-1):
        #     if i == 0 or i == len(nums)-1:
        #         prefix.append(1)
                
        #     else:
        #         pp *= nums[i-1]
        #         prefix.append(pp)
        #         ss *= nums[n-i-1]
        #         sufix.append(ss)
        # return sufix
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        for i in range(1,len(nums)):
            prefix[i]= prefix[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            suffix[i]= suffix[i+1]*nums[i+1]
        ans = [1]*n
        for i in range(0,n):
            ans[i] = prefix[i]*suffix[i]
        return ans


        