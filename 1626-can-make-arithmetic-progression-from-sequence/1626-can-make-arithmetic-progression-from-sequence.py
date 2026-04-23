class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        fwd = sorted(arr)
        rev = sorted(arr, reverse=True)

        delta = None

        for i in range(1, len(arr)):
            if not delta:
                delta = abs(fwd[i]- fwd[i-1])

            if abs(fwd[i]- fwd[i-1]) != delta or abs(rev[i]-rev[i-1]) != delta:
                return False
        
        return True