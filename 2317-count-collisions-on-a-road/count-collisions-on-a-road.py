class Solution:
    def countCollisions(self, directions: str) -> int:
        colision = False
        ans = 0
        right  =0
        n = len(directions)
        for i in range(n):
            if directions[i] == 'S':
                if right:
                    ans += right
                    right =0
                colision = True
                # colision=
            elif directions[i] == 'L':
                if right:
                    ans += 2
                    right -=1
                    if right:
                        ans +=right
                        right = 0
                    colision = True
                elif colision:
                    ans+=1
                else:
                    if colision:
                        ans +=1
                    else:
                        continue
            else:
                right +=1
        return(ans)
