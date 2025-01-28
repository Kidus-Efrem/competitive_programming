class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        output = [[0]*n  for i in range(m)]

        for i in range(m):
            for j in range(n):
                
                total, count= img[i][j], 1
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0<= ni < m and 0 <=nj < n:
                        total += img[ni][nj]
                        count += 1
                output[i][j] = total//count

        print(output)
        return output