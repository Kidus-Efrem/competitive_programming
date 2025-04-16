class Solution:
    def minMutation(self, b: str, e: str, wordList: List[str]) -> int:    
        chars = ['A', 'C', 'G', 'T']
        # dir = [(0, 1),(1, 0), (-1, 0), (0, -1)]
        # print(wordList, 'wordlist')
        wordList  = set(wordList)
        

        distance = 0
        queue = deque()
        queue.append((b, set()))
        while queue:
            distance +=1
            # print(queue)
            size = len(queue)
            for i in range(len(queue)):
                cur, visited = queue.popleft()
                if cur == e:
                    return distance-1
                for j in range(len(cur)):
                    for i in chars:
                        if cur[0:j]+i+cur[j+1:] in wordList and cur[0:j]+i+cur[j+1:] not in visited and cur[0:j]+i+cur[j+1:] != cur:

                            visited.add(cur[0:j]+i+cur[j+1:])
                            queue.append((cur[0:j]+i+cur[j+1:], visited))

        return -1

