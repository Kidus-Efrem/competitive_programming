class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        output = [[0]*n  for i in range(m)]

        for i in range(m):
            for j in range(n):
                
                total, count= 0, 0
                for x in (i-1, i, i+1):
                    for y in (j-1, j, j+1):
                        if 0<= x < m and 0 <=y < n:
                            total += img[x][y]
                            count += 1
                output[i][j] = total//count

        print(output)
        return output