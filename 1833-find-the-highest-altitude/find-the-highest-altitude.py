class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        listt = []
        sunn = 0
        for i in range(n):
            sunn+= gain[i]
            listt.append(sunn)
        if max(listt) > 0:
            return max(listt)
        else:
            return 0

        
        