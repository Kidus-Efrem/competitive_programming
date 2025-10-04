class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []
        for i in range(n):
            # if not stack or lst[i] >=stack[-1]:
            while stack and stack[-1] >num[i]  and k >0:
                stack.pop()
                k-=1
            
            stack.append(num[i])
        print('k', k, len(stack)-k)
        i = 0
        while i  <len(stack):
            if stack[i] == '0':
                i+=1
            else:break
        return (''.join(stack[i:len(stack)-k]) if stack[i:len(stack)-k] else '0')