class Solution:
    def check(self,mid: int, weights: List[int], days: int) -> bool:
        count = 1
        sumval = 0
        for i in weights:
            sumval += i
            if (sumval > mid):
                print(sumval)
                count += 1
                sumval = i

        print("count", count)
        print(count <= days)
        return count <= days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = max(weights)
        e = sum(weights)
        ans = 0
        while s<=e:
            mid = s + (e-s)//2
            print("midterm",mid)
            if self.check(mid,weights,days):

                ans = mid
                e = mid -1
            else:
                s = mid +1
        return ans


        