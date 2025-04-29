class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        ans = []
        for i in range(k):
            heapq.heappush(arr, -nums[i])
        # print(arr, "first")
        toremove = defaultdict(int)
        cnt = 0
        for j in range(k, len(nums)):
            while True:
                temp =  -1* arr[0]
                if toremove[temp]==0 :
                    # print(temp)
                    break
                temp = heapq.heappop(arr)
                toremove[-temp]-=1
            ans.append(temp)

            heapq.heappush(arr, -1 * nums[j])
            toremove[nums[cnt]]+=1
            cnt+=1
            # print(arr)
            # print("to remove", toremove)

        while True:
                temp =  -1* arr[0]
                if toremove[temp] ==0:
                    print(temp)
                    break
                temp = heapq.heappop(arr)
                toremove[-temp]-=1
        ans.append(temp)


        return ans
