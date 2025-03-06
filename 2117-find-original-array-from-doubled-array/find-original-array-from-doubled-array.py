class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        print(changed)
        c = Counter(changed)
        ans = []
        for i in range(len(changed)):
            if c[changed[i]]>0 and changed[i]*2 in c and c[changed[i]*2]>0:
                if changed[i]==changed[i]*2 and c[changed[i]] <2:
                    continue
                c[changed[i]*2] -=1
                c[changed[i]]-=1
                ans.append(changed[i])
            else:
                continue
        return( ans if len(ans)==len(changed)/2 else [] )