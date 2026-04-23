class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anaGroups = collections.defaultdict(list)

        for s in strs:
            sortS = "".join(sorted(s))

            anaGroups[sortS].append(s)

        return list(anaGroups.values())