class Solution:
    def calculate(self, s: str) -> int:
        s = "".join(s.split())  # Remove spaces

        def calc(l, r):
            if l > r:
                return 0
            neg = False
            if s[l] == "-":
                neg = True
                l += 1
            first = 0
            if s[l] == "(":  # Handle parentheses
                cnt = 1
                l += 1
                left = l
                while l <= r and cnt > 0:
                    if s[l] == "(":
                        cnt += 1
                    elif s[l] == ")":
                        cnt -= 1
                    l += 1
                first = calc(left, l - 2)  # Solve inside the parentheses
            else:  # Read full number
                num = ""
                while l <= r and s[l].isdigit():
                    num += s[l]
                    l += 1
                first = int(num)
            if neg: first = -first
            while l <= r:
                op = s[l]
                l += 1  # Move past operator

                if s[l] == "(":  # If next is a bracket, recurse
                    cnt = 1
                    l += 1
                    right_start = l
                    while l <= r and cnt > 0:
                        if s[l] == "(":
                            cnt += 1
                        elif s[l] == ")":
                            cnt -= 1
                        l += 1
                    second = calc(right_start, l - 2)
                else:  # Otherwise, read the next number
                    num = ""
                    while l <= r and s[l].isdigit():
                        num += s[l]
                        l += 1
                    second = int(num)

                if op == "-":
                    first -= second
                elif op == "+":
                    first += second

            return first

        return calc(0, len(s) - 1)
